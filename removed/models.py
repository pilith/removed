from django.db import models

# Create your models here.
class component(models.Model):
    def get_id():
        import time
        year = time.strftime('%Y')[-2:]
        if not component.objects.all().count():
            return year + '-' + str(1)
        last = component.objects.all().last()
        if  year == last.bag_id[:2]:
            return year + '-' + str(int(last.bag_id[3:]) + 1)
        else:
            return year + '-' + str(1)
    board_handling = (
        ('R', 'RMA'),
        ('P', 'Production'),
    )
    entry_date = models.DateField(auto_now=True)
    board = models.CharField(max_length=30)
    part_num = models.PositiveIntegerField()
    serial_num = models.PositiveIntegerField()
    handling = models.CharField(max_length=1, choices=board_handling)
    notes = models.CharField(max_length=100, blank=True)
    user_name = models.CharField(max_length = 30)
    bag_id = models.CharField(max_length = 10, unique=True, default=get_id)

    
class fixed_board(models.Model):
    board_handling = (
       ('R', 'RMA'),
       ('P', 'Production'),
       ('E', 'Engineering'),
    )
    entry_date = models.DateField(auto_now=True)
    board = models.CharField(max_length=30)
    serial_num = models.PositiveIntegerField()
    handling = models.CharField(max_length=1, choices=board_handling)
    notes = models.CharField(max_length=200)
    user_name = models.CharField(max_length = 30)

