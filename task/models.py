from django.db import models
from django.urls import reverse


class TodoTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    alert_time = models.TimeField()
    parent_task_id = models.IntegerField(blank=True, null=True)
    # parent_task_id = models.ForeignKey(
    #             "self",
    #             on_delete=models.CASCADE,
    #             null=True, blank=True)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task', kwargs={'pk': self.pk})
