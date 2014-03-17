from django.shortcuts import render_to_response, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.views.generic.base import View, TemplateView
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from registration.backends.simple.views import RegistrationView
from django.forms.models import modelformset_factory
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


class UserRegistration(RegistrationView):
    def get_success_url(self, request, user):
        return reverse('add_team', kwargs={'username': request.user.username })

class Settings(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = 'management/settings.html'

    login_url = '/login/'

    def test_func(self, user):
        if self.kwargs['username'] != user.username:
            raise Http404
        else:
            return True

    def get_context_data(self, **kwargs):
        context = super(Settings, self).get_context_data(**kwargs)

        context['teams'] = Team.objects.filter(coach=self.request.user)

        return context

class Front(TemplateView):

    template_name = 'management/front2.html'

class Homepage(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = 'management/index.html'

    login_url = '/login/'

    def test_func(self, user):
        if self.kwargs['username'] != user.username:
            raise Http404
        else:
            return True

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)

        context['teamlist'] = Team.objects.filter(coach=self.request.user)

        return context


class SeasonDetail(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = 'management/season_detail.html'

    login_url = '/login/'

    def test_func(self, user):
        if self.kwargs['username'] != user.username:
            raise Http404
        else:
            return True

    def get_context_data(self, **kwargs):
        context = super(SeasonDetail, self).get_context_data(**kwargs)

        try:
            season = Season.objects.filter(team__name=self.kwargs.get("name")).get(year=self.kwargs.get("year"))
        except:
            team = Team.objects.filter(coach=self.request.user).get(name=self.kwargs.get("name"))
            season = Season.objects.create(team=team ,year=self.kwargs.get("year"))

        context['teamlist'] = Season.objects.filter(team__coach=self.request.user)
        context['teams'] = Team.objects.filter(coach=self.request.user)
        context['players'] = Player.objects.filter(season__team__name=self.kwargs.get("name")).filter(season__year=self.kwargs.get("year"))
        context['seasons'] = Season.objects.filter(team__name=self.kwargs.get("name")).order_by("-year")

        return context

class PlayerList(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'management/roster_list.html'

    login_url = '/login/'

    def test_func(self, user):
        if self.kwargs['username'] != user.username:
            raise Http404
        else:
            return True

    def post(self, request, **kwargs):
        if 'delete' in request.POST:
            p = Player.objects.get(pk=request.POST['delete'])
            p.delete()
            return HttpResponseRedirect(reverse('player_list', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))
        else:
            player_form = PlayerForm(self.request.POST)
            if player_form.is_valid():
                player_form.save()
                return HttpResponseRedirect(reverse('player_list', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))
            else:
                print player_form.errors
        return HttpResponseRedirect(reverse('player_list', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))


    def get_context_data(self, **kwargs):
        context = super(PlayerList, self).get_context_data(**kwargs)

        player_form = PlayerForm()

        context['form'] = player_form
        context['team'] = Season.objects.get(team__name=self.kwargs.get("name"), year=self.kwargs.get("year"))
        context['players'] = Player.objects.filter(season__team__name=self.kwargs.get("name")).filter(season__year=self.kwargs.get("year")).order_by('last_name')
        context['teams'] = Team.objects.filter(coach=self.request.user)
        context['seasons'] = Season.objects.filter(team__name=self.kwargs.get("name")).order_by("-year")

        return context

class GameList(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = 'management/game_list.html'

    login_url = '/login/'

    def test_func(self, user):
        if self.kwargs['username'] != user.username:
            raise Http404
        else:
            return True

    def post(self, request, **kwargs):
        if 'delete' in request.POST:
            g = Game.objects.get(pk=request.POST['delete'])
            g.delete()
            return HttpResponseRedirect(reverse('game_list', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))
        else:
            game_form = AddGameForm(self.request.POST)
            game_form2 = None
            qset2 = self.request.POST.copy()
            time2 = qset2.pop('time2', None)[0]
            if time2:
                qset2['time'] = time2
                game_form2 = AddGameForm(qset2)
            if game_form.is_valid() and game_form2 is None:
                game_form.save()
                return HttpResponseRedirect(reverse('game_list', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))
            elif game_form.is_valid() and game_form2.is_valid():
                game_form.save()
                game_form2.save()
                return HttpResponseRedirect(reverse('game_list', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))
            else:
                print game_form.errors
                print game_form2.errors
        return HttpResponseRedirect(reverse('season_detail', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))

    def get_context_data(self, **kwargs):
        context = super(GameList, self).get_context_data(**kwargs)

        game_form = AddGameForm()

        context['form'] = game_form
        context['games'] = Game.objects.filter(season__team__name=self.kwargs.get("name")).filter(season__year=self.kwargs.get("year")).order_by('date')
        context['season'] = Season.objects.filter(team__name=self.kwargs.get("name")).get(year=self.kwargs.get("year"))
        context['teams'] = Team.objects.filter(coach=self.request.user)
        context['seasons'] = Season.objects.filter(team__name=self.kwargs.get("name")).order_by("-year")

        return context

class PlayerStats(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = 'management/player_stats.html'

    login_url = '/login/'

    def test_func(self, user):
        if self.kwargs['username'] != user.username:
            raise Http404
        else:
            return True

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

        totals = HitterStats.objects.filter(player__season__team__name=self.kwargs.get("name")).filter(player__season__year=self.kwargs.get('year')).aggregate(atbats=Sum('at_bats'),
            hits=Sum('hits'), runs=Sum('runs'), doubles=Sum('doubles'), triples=Sum('triples'), hr=Sum('hr'), rbi=Sum('rbi'),
            walks=Sum('walks'), hbp=Sum('hbp'), strikeouts=Sum('strikeouts'), sacrafice=Sum('sacrafice'))

        if HitterStats.objects.filter(player__season__team__name=self.kwargs.get("name")).filter(player__season__year=self.kwargs.get('year')):
            totals['plate_apperances'] = totals['atbats']+totals['walks']+totals['hbp']+totals['sacrafice']
            totals['games'] = Game.objects.filter(season__team__name=self.kwargs.get('name')).count() - Game.objects.filter(season__team__name=self.kwargs.get('name'), hitterstats__isnull=True).count()
            totals['average'] = round(float(totals['hits']) / float(totals['atbats']),3)
            totals['onbase'] = round(float(totals['hits'] + totals['walks'] + totals['hbp']) / float(totals['atbats']+totals['walks']+totals['hbp']+totals['sacrafice']),3)
            totals['single'] = totals['hits']-(totals['doubles']+totals['triples']+totals['hr'])
            totals['slugging'] = round(float(totals['single']+(2*totals['doubles'])+(3*totals['triples'])+(4*totals['hr']))/totals['atbats'],3)
        else:
            totals = 0

        pitch = PitcherStats.objects.filter(player__season__team__name=self.kwargs.get("name")).filter(player__season__year=self.kwargs.get('year')).aggregate(starts=Count('starting_pitcher'), full=Sum('full_innings'),part=Sum('part_innings'),
            hits=Sum('hits_allowed'),runs=Sum('runs_allowed'), earned=Sum('earned_runs'), walks=Sum('walks_allowed'), k=Sum('strikeout_amount'),wp=Sum('wild_pitches'),
            hbp=Sum('hit_by_pitch'), w=Sum('win'), l=Sum('loss'), sv=Sum('sv'))

        if PitcherStats.objects.filter(player__season__team__name=self.kwargs.get("name")).filter(player__season__year=self.kwargs.get('year')):
            pitch['innings'] = str(((pitch['full']*3)+pitch['part']) / 3) + "." + str(((pitch['full']*3)+pitch['part']) % 3)
            pitch['era'] = round(float(pitch['earned']) / (pitch['full']+(pitch['part']/3.0)) * 9.0 ,2)
            pitch['games'] = Game.objects.filter(season__team__name=self.kwargs.get('name')).count() - Game.objects.filter(season__team__name=self.kwargs.get('name'), pitcherstats__isnull=True).count()
        else: 
            pitch = 0
            
        context['totals'] = totals
        context['pitch'] = pitch
        context['batters'] = sorted(batters, key=lambda x: x.average(), reverse=True)
        context['pitchers'] = sorted(pitchers, key=lambda x: x.era())
        context['teams'] = Team.objects.filter(coach=self.request.user)
        context['seasons'] = Season.objects.filter(team__name=self.kwargs.get("name")).order_by("-year")

        return context

class Depth_Chart(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = 'management/depth_chart.html'

    login_url = '/login/'

    def test_func(self, user):
        if self.kwargs['username'] != user.username:
            raise Http404
        else:
            return True

    def post(self, request, **kwargs):
        if request.POST:
            object_pk = request.POST.get("pk", "")
            position = DepthChart.objects.filter(season__team__name=self.kwargs.get("name")).get(season__year=self.kwargs.get("year"))
            this_form = PositionForm(self.request.POST, instance=position)
            if this_form.is_valid():
                this_form.save()
                return HttpResponseRedirect(reverse('depth_chart', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))
            else:
                print this_form.errors
        return HttpResponseRedirect(reverse('depth_chart', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))

    def get_context_data(self, **kwargs):
        context = super(Depth_Chart, self).get_context_data(**kwargs)

        try:
            depthchart = DepthChart.objects.filter(season__team__name=self.kwargs.get("name")).get(season__year=self.kwargs.get("year"))
        except:
            season = Season.objects.filter(team__name=self.kwargs.get("name")).get(year=self.kwargs.get("year"))
            depthchart = DepthChart.objects.create(season=season)

        this_form = PositionForm(instance=depthchart)

        context['form'] = this_form
        context['depth'] = depthchart
        context['players'] = Player.objects.filter(season__team__name=self.kwargs.get("name")).filter(season__year=self.kwargs.get("year"))
        context['teams'] = Team.objects.filter(coach=self.request.user)
        context['seasons'] = Season.objects.filter(team__name=self.kwargs.get("name")).order_by("-year")

        return context

class AddTeam(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = 'management/add_team.html'

    login = '/login/'

    def test_func(self, user):
        if self.kwargs['username'] != user.username:
            raise Http404
        else:
            return True

    def post(self, request, **kwargs):
        if request.POST:
            form = AddTeamForm(self.request.POST, user=request.user.username)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect(reverse('season_detail', kwargs={'username': request.user.username, 'name': request.POST['name'], 'year': request.POST['year']}))
            else:
                print form.errors
        return HttpResponseRedirect(reverse('season_detail', kwargs={'username': request.user.username,'name': request.POST['name'], 'year': request.POST['year']}))

    def get_context_data(self, **kwargs):
        context = super(AddTeam, self).get_context_data(**kwargs)

        form = AddTeamForm(user=self.request.user)
        form2 = SeasonForm()

        context['teamlist'] = Team.objects.filter(coach=self.request.user)
        context['form'] = form
        context['form2'] = form2

        return context

class AddSeason(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = 'management/add_season.html'

    login = '/login/'

    def test_func(self, user):
        if self.kwargs['username'] != user.username:
            raise Http404
        else:
            return True

    def post(self, request, **kwargs):
        if request.POST:
            form = AddSeasonForm(self.request.POST, coach=request.user)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect(reverse('season_detail', kwargs={'username': request.user.username, 'name': self.kwargs.get("name"), 'year': request.POST['year']}))
            else:
                print "form not valid"
        return HttpResponseRedirect(reverse('season_detail', kwargs={'username': request.user.username,'name': self.kwargs.get("name"), 'year': request.POST['year']}))

    def get_context_data(self, **kwargs):
        context = super(AddSeason, self).get_context_data(**kwargs)

        form = AddSeasonForm(coach=self.request.user)
        context['teams'] = Team.objects.filter(coach=self.request.user)
        context['seasons'] = Season.objects.filter(team__name=self.kwargs.get("name")).order_by("-year")
        context['form'] = form

        return context


class GameStats(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = 'management/game_stats.html'

    login = '/login/'

    def test_func(self, user):
        if self.kwargs['username'] != user.username:
            raise Http404
        else:
            return True

    # HitStatsFormSet = modelformset_factory(HitterStats, form=HitStatsForm, extra=9)
    # PitchStatsFormSet = modelformset_factory(PitcherStats, form=PitchStatsForm)

    # hit_formset = HitStatsFormSet(queryset=game, prefix='hit')
    # pitch_formset = PitchStatsFormSet(queryset=game, prefix='pitch')

    def post(self, request, **kwargs):
        hit = HitterStats.objects.filter(game__pk=self.kwargs.get("pk"))
        pitch = PitcherStats.objects.filter(game__pk=self.kwargs.get("pk"))
        HitStatsFormSet = modelformset_factory(HitterStats, form=HitStatsForm)
        PitchStatsFormSet = modelformset_factory(PitcherStats, form=PitchStatsForm)
        hit_formset = HitStatsFormSet(request.POST, request.FILES, queryset=hit, prefix='hit')
        pitch_formset = PitchStatsFormSet(request.POST, request.FILES, queryset=pitch, prefix='pitch')
        if hit_formset.is_valid():
            hit_formset.save()
        else:
            print hit_formset.errors
        if pitch_formset.is_valid():
            pitch_formset.save()
        else:
            print pitch_formset.errors
        return HttpResponseRedirect(reverse('season_detail', kwargs={'username': request.user.username , 'name': self.kwargs.get("name"), 'year': self.kwargs.get("year")}))

    def get_context_data(self, **kwargs):
        context = super(GameStats, self).get_context_data(**kwargs)
        season = Season.objects.filter(team__name=self.kwargs.get("name")).get(year=self.kwargs.get("year"))
        game = Game.objects.filter(season=season).get(pk=self.kwargs.get("pk"))
        hit = HitterStats.objects.filter(game__pk=self.kwargs.get("pk"))
        pitch = PitcherStats.objects.filter(game__pk=self.kwargs.get("pk"))

        HitStatsFormSet = modelformset_factory(HitterStats, form=HitStatsForm, extra=9-len(hit))
        PitchStatsFormSet = modelformset_factory(PitcherStats, form=PitchStatsForm, extra=1-len(pitch))

        hit_formset = HitStatsFormSet(initial=[{'game': game,}], queryset=hit, prefix='hit')
        pitch_formset = PitchStatsFormSet(initial=[{'game': game,}], queryset=pitch, prefix='pitch')

        context['game'] = game
        context['players'] = Player.objects.filter(season=season)
        context['formset'] = hit_formset
        context['formset2'] = pitch_formset

        return context
