from django.db import models

# Create your models here.
class component(models.Model):
    board_handling = (
        ('R', 'RMA'),
        ('P', 'Production'),
    )
    entry_date = models.DateField()
    board = model.CharField(max_length=30)
    part_num = model.PositiveIntegerField()
    serial_num = model.PositiveIntegerField()
    handling = model.CharField(max_length=1, choices=board_handling)
    notes = model.CharField(max_length=100, blank=True)
    user_name = model.CharField(max_length = 30)
