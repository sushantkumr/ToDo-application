from background_task import background


@background(schedule=1)  # Delete subsequent every day
def hard_delete_records():
    print("hello world")
    # queryset = TodoTask.objects.filter(deleted=True)
    # queryset.delete()
