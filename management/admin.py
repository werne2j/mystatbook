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

class PlayerStatsAdmin(admin.ModelAdmin):
	list_display = ('player', 'game', 'at_bats','runs','hits','hr','rbi','walks','strikeouts','innings','hits_allowed','runs_allowed','earned_runs','walks_allowed','strikeout_amount', 'wild_pitches', 'hit_by_pitch')

# class IndivPitchStatsAdmin(admin.ModelAdmin):
# 	list_display = ('player', 'innings','hits_allowed','runs_allowed','earned_runs','walks_allowed','strikeouts', 'wild_pitches', 'hit_by_pitch')

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(PlayerStats, PlayerStatsAdmin)
# admin.site.register(IndivPitchStats, IndivPitchStatsAdmin)