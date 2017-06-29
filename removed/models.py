from django.db import models

# Create your models here.
class component(models.Model):
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
