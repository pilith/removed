from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class playerChar(models.Model):
    """Player character"""

    # Top level attributes
    user = models.ForeignKey(User)
    race = models.CharField(max_length=50)
    charclass = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField
    name = models.CharField(max_length=100)
    exp = models.PositiveIntegerField
    gold = models.PositiveSmallIntegerField
    
    # Atributes
    strength = models.PositiveSmallIntegerField
    dex = models.PositiveSmallIntegerField
    const = models.PositiveSmallIntegerField
    intel = models.PositiveSmallIntegerField
    wis = models.PositiveSmallIntegerField
    char  = models.PositiveSmallIntegerField
    prof_bonus = models.PositiveSmallIntegerField
    inspiration = models.PositiveSmallIntegerField

    # Health
    max_hitpoints = models.PositiveSmallIntegerField 
    cur_hitpoints = models.PositiveSmallIntegerField
    ac = models.PositiveSmallIntegerField
    initiative = models.PositiveSmallIntegerField
    speed = models.PositiveSmallIntegerField

    # Skills
    acrobatics = models.PositiveSmallIntegerField
    animal_handling = models.PositiveSmallIntegerField
    arcana = models.PositiveSmallIntegerField
    athletics = models.PositiveSmallIntegerField
    deception = models.PositiveSmallIntegerField
    history = models.PositiveSmallIntegerField
    insight = models.PositiveSmallIntegerField
    intimidation = models.PositiveSmallIntegerField
    investigation = models.PositiveSmallIntegerField
    medicine = models.PositiveSmallIntegerField
    Nature = models.PositiveSmallIntegerField
    Perception = models.PositiveSmallIntegerField
    Performance = models.PositiveSmallIntegerField
    Persuasion = models.PositiveSmallIntegerField
    religion = models.PositiveSmallIntegerField
    sleight_of_hand = models.PositiveSmallIntegerField
    stealth = models.PositiveSmallIntegerField
    survival = models.PositiveSmallIntegerField
    

    def __str__(self):
        """Returns string representation of model"""
        return self.txt
