from django.shortcuts import render,HttpResponse
from .models import Vote,LevelOfAppreciation
from teamMatez.models import TeamMate
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required
from forms import VoteForm
import json

# Create your views here.

@login_required
def votingView(request):

    currentTeamMate = request.user.teammate_set.all()[0]
    teamMates = currentTeamMate.team.teammate_set.all().exclude(user=currentTeamMate.user)


    form = VoteForm(initial={'levelOfAppreciation': 1})

    levelsOfAppreciation = LevelOfAppreciation.objects.all().order_by('-weight')

    return render(request, 'votez/voting.html', {'team':currentTeamMate.team,'teamMates':teamMates,'form':form,'levelsOfApp':levelsOfAppreciation})


def vote(request):


    Vote.objects.create(reporter = TeamMate.objects.get(user=request.user),
                            teamMate= TeamMate.objects.get(user=User.objects.get(username=request.POST['teamMate'])),
                            levelOfAppreciation = LevelOfAppreciation.objects.get(description = request.POST.get('levelOfAppreciation',None)),
                            wordsOfAppreciation = request.POST.get('wordsOfAppreciation',None),
                            date= datetime.date.today())

    response_data = {}
    response_data['test'] = True

    return HttpResponse(json.dumps(response_data))