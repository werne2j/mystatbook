from django.contrib import admin
from .models import *

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
	list_display = ('coach', 'name', 'year')

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('team', 'first_name', 'last_name', 'class_standing', 'throws', 'hits')

class PositionAdmin(admin.ModelAdmin):
	list_display = ('position',)

class GameAdmin(admin.ModelAdmin):
	list_display = ('team', 'opponent', 'date', 'location', 'time', 'doubleheader')

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Game, GameAdmin)