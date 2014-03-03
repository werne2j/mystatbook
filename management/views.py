from django.shortcuts import render_to_response, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.base import View, TemplateView
from braces.views import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from registration.backends.simple.views import RegistrationView
from .models import *
from .views import *
from .forms import *

# Create your views here.
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def login_page(request):
    if request.POST:
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse('coach_portal', kwargs={'username': username }))

    else:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('coach_portal', kwargs={'username': request.user.username }))
    return render_to_response('management/login.html', {}, context_instance=RequestContext(request))

class Homepage(LoginRequiredMixin, TemplateView):
    
    template_name = 'management/index.html'

    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)

        context['teamlist'] = Team.objects.filter(coach=self.request.user)

        return context


class SeasonDetail(LoginRequiredMixin, TemplateView):
    
    template_name = 'management/season_detail.html'

    login_url = '/login/'

    def post(self, request, **kwargs):
        if 'update_modal' in request.POST:
            object_pk = request.POST.get("pk", "")
            position = DepthChart.objects.filter(season__team__name=self.kwargs.get("name")).get(season__year=self.kwargs.get("year"))
            this_form = PositionForm(self.request.POST, instance=position)
            if this_form.is_valid():
                this_form.save()
                return HttpResponseRedirect(reverse('season_detail', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))
            else:
                print "Form Not Valid"
            return HttpResponseRedirect(reverse('season_detail', kwargs={'username': username , 'name': name}))

    def get_context_data(self, **kwargs):
        context = super(SeasonDetail, self).get_context_data(**kwargs)


        try:
            season = Season.objects.filter(team__name=self.kwargs.get("name")).get(year=self.kwargs.get("year"))
        except:
            team = Team.objects.filter(coach=self.request.user).get(name=self.kwargs.get("name"))
            season = Season.objects.create(team=team ,year=self.kwargs.get("year"))

        try:
            depthchart = DepthChart.objects.filter(season__team__name=self.kwargs.get("name")).get(season__year=self.kwargs.get("year"))
        except:
            season = Season.objects.filter(team__name=self.kwargs.get("name")).get(year=self.kwargs.get("year"))
            depthchart = DepthChart.objects.create(season=season)

        this_form = PositionForm(instance=depthchart)

        context['form'] = this_form
        context['teamlist'] = Season.objects.filter(team__coach=self.request.user)
        context['teams'] = Team.objects.filter(coach=self.request.user)
        context['players'] = Player.objects.filter(season__team__name=self.kwargs.get("name")).filter(season__year=self.kwargs.get("year"))
        context['seasons'] = Season.objects.filter(team__name=self.kwargs.get("name")).order_by("-year")
        
        return context

class PlayerList(LoginRequiredMixin, TemplateView):

    template_name = 'management/roster_list.html'

    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(PlayerList, self).get_context_data(**kwargs)

        context['players'] = Player.objects.filter(season__team__name=self.kwargs.get("name")).filter(season__year=self.kwargs.get("year"))

        return context

class GameList(LoginRequiredMixin, TemplateView):

    template_name = 'management/game_list.html'

    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(GameList, self).get_context_data(**kwargs)

        context['games'] = Game.objects.filter(season__team__name=self.kwargs.get("name")).filter(season__year=self.kwargs.get("year"))

        return context

class PlayerStats(LoginRequiredMixin, TemplateView):

    template_name = 'management/player_stats.html'

    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(PlayerStats, self).get_context_data(**kwargs)

        players = Player.objects.filter(season__team__name=self.kwargs.get("name")).filter(season__year=self.kwargs.get("year"))
        batters = []
        pitchers = []
        for player in players:
            if player.plate_apperances() > 0:
                batters.append(player)
            if player.pitch_totals().get('full_innings__sum') > 0:
                pitchers.append(player)    

        context['batters'] = batters
        context['pitchers'] = pitchers

        return context

class Depth_Chart(LoginRequiredMixin, TemplateView):

    template_name = 'management/depth_chart.html'

    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(Depth_Chart, self).get_context_data(**kwargs)

        try:
            depthchart = DepthChart.objects.filter(season__team__name=self.kwargs.get("name")).get(season__year=self.kwargs.get("year"))
        except:
            season = Season.objects.filter(team__name=self.kwargs.get("name")).get(year=self.kwargs.get("year"))
            depthchart = DepthChart.objects.create(season=season)

        context['depth'] = depthchart
        context['players'] = Player.objects.filter(season__team__name=self.kwargs.get("name")).filter(season__year=self.kwargs.get("year"))

        return context

class UserRegistration(RegistrationView):
    def get_success_url(self, request, user):   
        return reverse('coach_portal', kwargs={'username': request.user.username })

class AddTeam(LoginRequiredMixin, TemplateView):

    template_name = 'management/add_team.html'

    login = '/login/'

    def post(self, request, **kwargs):
        if request.POST:
            form = AddTeamForm(self.request.POST)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect(reverse('season_detail', kwargs={'username': request.user.username, 'name': request.POST['name'], 'year': request.POST['year']}))
            else: 
                print "form not valid"
            return HttpResponseRedirect(reverse('season_detail', kwargs={'username': request.user.username,'name': request.POST['name'], 'year': request.POST['year']}))

    def get_context_data(self, **kwargs):
        context = super(AddTeam, self).get_context_data(**kwargs)

        form = AddTeamForm()
        form2 = SeasonForm()

        context['teams'] = Team.objects.filter(coach=self.request.user)
        context['form'] = form
        context['form2'] = form2

        return context



