from django.contrib import admin

# Register your models here.

from boardgames.models import boardgame

admin.site.register(boardgame)
