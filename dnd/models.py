from django.db import models
from django.contrib.auth.models import User

from multiselectfield import MultiSelectField as msf

# Create your models here.

skill_choices = (
    ('acr', 'Acrobatics'),
    ('anm', 'Animal Handling'),
    ('arc', 'Arcana'),
    ('ath', 'Athletics'),
    ('dec', 'Deception'),
    ('his', 'History'),
    ('ins', 'Insight'),
    ('int', 'Intimidation'),
    ('inv', 'Investigation'),
    ('med', 'Medicine'),
    ('nat', 'Nature'),
    ('per', 'Perception'),
    ('pfm', 'Performance'),
    ('psn', 'Persuasion'),
    ('rel', 'Religion'),
    ('soh', 'Slight of Hand'),
    ('sth', 'Stealth'),
    ('sur', 'Survival'))


class playerChar(models.Model):
    """Player character"""

    # Top level attributes
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')
    race = models.CharField(max_length=50)
    charclass = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=100, unique=True)
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
    skills = msf(choices=skill_choices)    

