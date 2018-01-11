from django.db import models
from django.contrib.auth.models import User

# Create your models here.

comp = (
    ('cp', 'Cooperation'),
    ('tm', 'Team vs. Team'),
    ('ev', 'Competitive'))

genre = (
    ('cd', 'Card Game'),
    ('bd', 'Board Game')) 

class boardgame(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    name = models.CharField(max_length=100)
    cover = models.ImageField(help_text='Image size limit = 100kb')    
    
    # min and max players
    p_min = models.PositiveSmallIntegerField(null=True)
    p_max = models.PositiveSmallIntegerField(null=True, blank=True, help_text='Optional')

    age = models.PositiveSmallIntegerField(null=True) 

    time = models.PositiveSmallIntegerField(null=True, help_text='Estimated time per game \n in minutes') 

    # choices fields
    play_style = models.CharField(
        max_length = 2,
        choices = comp)
    game_genre = models.CharField(
        max_length = 2,
        choices = genre)
        
