from celery import shared_task

@shared_task()
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"