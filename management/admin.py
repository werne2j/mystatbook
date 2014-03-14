from django.contrib import admin
from .models import *

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
	list_display = ('coach', 'name')

class SeasonAdmin(admin.ModelAdmin):
	list_display = ('team','year', 'date_added')

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('season', 'first_name', 'last_name', 'class_standing', 'throws', 'hits')

class PositionAdmin(admin.ModelAdmin):
	list_display = ('position',)

class GameAdmin(admin.ModelAdmin):
	list_display = ('season', 'opponent', 'date', 'location', 'time', 'doubleheader', 'conference')

class HitStatsAdmin(admin.ModelAdmin):
	list_display = ('player', 'game', 'at_bats','runs','hits','hr','rbi','walks','strikeouts')

class PitchStatsAdmin(admin.ModelAdmin):
	list_display = ('player', 'game','starting_pitcher','full_innings','part_innings','hits_allowed','runs_allowed','earned_runs','walks_allowed','strikeout_amount', 'wild_pitches', 'hit_by_pitch')

class DepthChartAdmin(admin.ModelAdmin):
	pass


# class IndivPitchStatsAdmin(admin.ModelAdmin):
# 	list_display = ('player', 'innings','hits_allowed','runs_allowed','earned_runs','walks_allowed','strikeouts', 'wild_pitches', 'hit_by_pitch')

admin.site.register(Team, TeamAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(HitterStats, HitStatsAdmin)
admin.site.register(PitcherStats, PitchStatsAdmin)
admin.site.register(DepthChart, DepthChartAdmin)
# admin.site.register(IndivPitchStats, IndivPitchStatsAdmin)
