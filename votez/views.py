from django.shortcuts import render,HttpResponse
from .models import Vote
from teamMatez.models import TeamMate
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def votingView(request):

    currentTeamMate = request.user.teammate_set.all()[0]
    teamMates = currentTeamMate.team.teammate_set.all().exclude(user=currentTeamMate.user)
    votes = Vote.objects.filter(reporter=currentTeamMate).order_by('-date')
    votingAllowed = False if (votes.count() > 0 and votes[0].date == datetime.date.today()) else True

    votingAllowed = True
    return render(request, 'votez/voting.html', {'team':currentTeamMate.team,'teamMates':teamMates,"votingAllowed": votingAllowed})


def vote(request):

        Vote.objects.create(reporter = TeamMate.objects.get(user=request.user),
                            teamMate = TeamMate.objects.get(user=User.objects.get(username=request.GET.get('username',None))) ,
                            weight=1,
                            date= datetime.date.today())
        return HttpResponse(request)