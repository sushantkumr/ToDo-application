from task.models import Task
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.api import Api
from tastypie.validation import Validation
from tastypie import fields
from django.utils import timezone
from datetime import datetime, timedelta


class UpdateValidation(Validation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'message': 'Incorrect request'}

        for key, value in bundle.data.items():
            if key not in ['status', 'pk', 'deleted']:
                return {'message': 'Only status/deleted status of task can be updated'}


# Gets list of tasks and to search based on title and different time periods
# http://0.0.0.0:8080/api/v1/task/?title__contains=123
# http://0.0.0.0:8080/api/v1/task/?period=overdue
# http://0.0.0.0:8080/api/v1/task/1
# http://0.0.0.0:8080/api/v1/task/?title__contains=Qwerty&period=overdue
class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.order_by('due_date').filter(deleted=False)
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put']
        limit = 50
        filtering = {
            'title': ['exact', 'startswith', 'endswith', 'contains'],
            'parent_task_id_id': ['exact']
        }

    # If query contains "period" override get_object_list()
    def get_object_list(self, request):
        if "period" in (request.GET):
            if(request.GET["period"] == "overdue"):
                return super(TaskResource, self) \
                            .get_object_list(request) \
                            .filter(due_date__lte=timezone.now())
            elif(request.GET["period"] == "today"):
                tomorrow = datetime.now().date() + timedelta(days=1)
                return super(TaskResource, self) \
                    .get_object_list(request) \
                    .filter(due_date__range=(timezone.now(), tomorrow))
            elif(request.GET["period"] == "thisweek"):
                days_till_sunday = 7 - datetime.today().weekday()
                end_of_week = datetime.now().date() + timedelta(days=days_till_sunday)
                return super(TaskResource, self) \
                    .get_object_list(request) \
                    .filter(due_date__range=(timezone.now(), end_of_week))
            elif(request.GET["period"] == "nextweek"):
                days_till_sunday = 7 - datetime.today().weekday()
                start_of_next_week = datetime.now().date() + timedelta(days=days_till_sunday)
                end_of_next_week = start_of_next_week + timedelta(days=7)
                return super(TaskResource, self) \
                    .get_object_list(request) \
                    .filter(due_date__range=(start_of_next_week, end_of_next_week))
        else:
            return super(TaskResource, self).get_object_list(request)


# Creating sub tasks for a particular task
class CreateTaskResource(ModelResource):
    id = fields.ToManyField('self', 'parent_task_id', null=True, full=True)
    parent_task_id_id = fields.ToOneField('self', 'id', null=True, full=True)

    class Meta:
        queryset = Task.objects.all()
        authorization = Authorization()
        allowed_methods = ['post', 'get']
        resource_name = "create_task"


v1_api = Api(api_name='v1')
v1_api.register(TaskResource())
v1_api.register(CreateTaskResource())
