from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
	username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
	password1 = forms.CharField(label=_("Password"),
		widget=forms.PasswordInput)
	password2 = forms.CharField(label=_("Password confirmation"),
		widget=forms.PasswordInput,
		help_text=_("Enter the same password as above, for verification."))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class AddTeamForm(forms.ModelForm):
	class Meta:
		model = Team

class SeasonForm(forms.ModelForm):
	class Meta:
		model = Season
		fields = ('year',)

class PositionForm(forms.ModelForm):
	class Meta:
		model = DepthChart

class PlayerForm(forms.ModelForm):
	class Meta:
		model = Player
		fields = ('season', 'first_name', 'last_name', 'position', 'class_standing', 'throws', 'hits')

class HitStatsForm(forms.ModelForm):
	class Meta:
		model = PlayerStats
		fields = ('player','at_bats', 'runs', 'hits', 'doubles', 'triples', 'hr', 'rbi', 'walks', 'hbp', 'sacrafice', 'strikeouts')

class PitchStatsForm(forms.ModelForm):
	class Meta:
		model = PlayerStats
		fields = ('player','starting_pitcher', 'full_innings', 'part_innings', 'hits_allowed', 'runs_allowed', 'earned_runs', 'walks_allowed', 'strikeout_amount', 'wild_pitches', 'hit_by_pitch', 'win', 'loss', 'sv')