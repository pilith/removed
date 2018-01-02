from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class playerChar(models.Model):
    """Player character"""

    # Top level attributes
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.CharField(max_length=50)
    charclass = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=100)
    exp = models.PositiveIntegerField(null=True, blank=True)
    gold = models.PositiveSmallIntegerField(null=True, blank=True)
    
    # Atributes
    strength = models.PositiveSmallIntegerField(null=True)
    dex = models.PositiveSmallIntegerField(null=True, blank=True)
    const = models.PositiveSmallIntegerField(null=True, blank=True)
    intel = models.PositiveSmallIntegerField(null=True, blank=True)
    wis = models.PositiveSmallIntegerField(null=True, blank=True)
    char  = models.PositiveSmallIntegerField(null=True, blank=True)
    prof_bonus = models.PositiveSmallIntegerField(null=True, blank=True)
    inspiration = models.PositiveSmallIntegerField(null=True, blank=True)

    # Health
    max_hitpoints = models.PositiveSmallIntegerField(null=True, blank=True)
    cur_hitpoints = models.PositiveSmallIntegerField(null=True, blank=True)
    ac = models.PositiveSmallIntegerField(null=True, blank=True)
    initiative = models.PositiveSmallIntegerField(null=True, blank=True)
    speed = models.PositiveSmallIntegerField(null=True, blank=True)

    # Skills
    acrobatics = models.PositiveSmallIntegerField(null=True, blank=True)
    animal_handling = models.PositiveSmallIntegerField(null=True, blank=True)
    arcana = models.PositiveSmallIntegerField(null=True, blank=True)
    athletics = models.PositiveSmallIntegerField(null=True, blank=True)
    deception = models.PositiveSmallIntegerField(null=True, blank=True)
    history = models.PositiveSmallIntegerField(null=True, blank=True)
    insight = models.PositiveSmallIntegerField(null=True, blank=True)
    intimidation = models.PositiveSmallIntegerField(null=True, blank=True)
    investigation = models.PositiveSmallIntegerField(null=True, blank=True)
    medicine = models.PositiveSmallIntegerField(null=True, blank=True)
    Nature = models.PositiveSmallIntegerField(null=True, blank=True)
    Perception = models.PositiveSmallIntegerField(null=True, blank=True)
    Performance = models.PositiveSmallIntegerField(null=True, blank=True)
    Persuasion = models.PositiveSmallIntegerField(null=True, blank=True)
    religion = models.PositiveSmallIntegerField(null=True, blank=True)
    sleight_of_hand = models.PositiveSmallIntegerField(null=True, blank=True)
    stealth = models.PositiveSmallIntegerField(null=True, blank=True)
    survival = models.PositiveSmallIntegerField(null=True, blank=True)
    

