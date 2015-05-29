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

    #voting app , changed to appreciation app :)
    #votes = Vote.objects.filter(reporter=currentTeamMate).order_by('-date')
    #votingAllowed = False if (votes.count() > 0 and votes[0].date == datetime.date.today()) else True

    form = VoteForm(initial={'levelOfAppreciation': 1})
    appreciated = False
    return render(request, 'votez/voting.html', {'team':currentTeamMate.team,'teamMates':teamMates,'form':form,'appreciated':appreciated})


def vote1(request):
        print "vote triggered"

        currentTeamMate = request.user.teammate_set.all()[0]
        teamMates = currentTeamMate.team.teammate_set.all().exclude(user=currentTeamMate.user)

        teamMate = TeamMate.objects.get(user=User.objects.get(username=request.POST.get('usertoappreciate',None)))
        print request.POST.get('usertoappreciate',None)
        Vote.objects.create(reporter = TeamMate.objects.get(user=request.user),
                            teamMate= teamMate ,
                            levelOfAppreciation = LevelOfAppreciation.objects.get(id = request.POST.get('levelOfAppreciation',None)),
                            wordsOfAppreciation = request.POST.get('wordsOfAppreciation',None),
                            date= datetime.date.today())

        form = VoteForm(initial={'levelOfAppreciation': 1})
        appreciated = True;
        print teamMate



        response_data = {}
        response_data['test'] = 'success'

        return HttpResponse(json.dumps(response_data))

        #return render(request, 'votez/voting.html', {'team':currentTeamMate.team,'teamMates':teamMates,'form':form ,'appreciated':appreciated ,'teamMateApp':teamMate})


def vote(request):
    print "new vote triggered"
    currentTeamMate = request.user.teammate_set.all()[0]
    teamMates = currentTeamMate.team.teammate_set.all().exclude(user=currentTeamMate.user)
    print request.POST['teamMate']
    teamMate = TeamMate.objects.get(user=User.objects.get(username=request.POST['teamMate']))

    Vote.objects.create(reporter = TeamMate.objects.get(user=request.user),
                            teamMate= teamMate ,
                            levelOfAppreciation = LevelOfAppreciation.objects.get(id = request.POST.get('levelOfAppreciation',None)),
                            wordsOfAppreciation = request.POST.get('wordsOfAppreciation',None),
                            date= datetime.date.today())
    print teamMate

    print "new vote triggered"
    response_data = {}
    response_data['test'] = True

    return HttpResponse(json.dumps(response_data))