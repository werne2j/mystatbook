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
