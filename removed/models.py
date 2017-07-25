from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class component(models.Model):
    board_handling = (
        ('RMA', 'RMA'),
        ('Production', 'Production'),
    )
    entry_date = models.DateField(auto_now=True)
    board = models.CharField(max_length=30)
    part_num = models.CharField(max_length=15, validators=[RegexValidator(r'^.{8,}$',
        'Must be at least 8 characters')])
    serial_num = models.PositiveIntegerField(validators=[RegexValidator(r'^\d{8}$',
        'Must be 8 digit Serial Number','Invalid Number')])
    handling = models.CharField(max_length=10, choices=board_handling)
    notes = models.CharField(max_length=100, blank=True)
    user_name = models.CharField(max_length = 30)
    ref_des = models.CharField(max_length = 150)
    bag_id = models.CharField(max_length = 10, unique=True)

    
class fixed_board(models.Model):
    board_handling = (
       ('RMA', 'RMA'),
       ('Production', 'Production'),
       ('Engineering', 'Engineering'),
    )
    entry_date = models.DateField(auto_now=True)
    board = models.CharField(max_length=30)
    serial_num = models.PositiveIntegerField(validators=[RegexValidator(r'^\d{8}$',
        'Must be 8 digit Serial Number','Invalid Number')])
    handling = models.CharField(max_length=11, choices=board_handling)
    notes = models.TextField()
    user_name = models.CharField(max_length = 30)

