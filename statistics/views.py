from django.shortcuts import render
from votez.models import Vote

import operator
import json
from django.http import HttpResponse

# Create your views here.



def ranking(request):
    print "ranking"
    currentTeamMate = request.user.teammate_set.all()[0]
    teamMatez =  currentTeamMate.team.teammate_set.all()

    for teamMate in teamMatez:
        teamMate.votesNumber = 0
        teamMate.votesNumber = Vote.objects.filter(teamMate=teamMate).count()

    ordered = sorted(teamMatez, key=operator.attrgetter('votesNumber'),reverse=True)
    print ordered

    return render(request,'statistics/ranking.html',{'team':currentTeamMate.team,'teamMatez':ordered})

def updateLeaderBoard(request):
    print "updateLeaderBoard"
    currentTeamMate = request.user.teammate_set.all()[0]
    teamMatez =  currentTeamMate.team.teammate_set.all()

    for teamMate in teamMatez:
        teamMate.votesNumber = 0
        teamMate.votesNumber = Vote.objects.filter(teamMate=teamMate).count()

    ordered = sorted(teamMatez, key=operator.attrgetter('votesNumber'),reverse=True)
    print ordered

    return render(request,'statistics/leaderboard.html',{'teamMatez':ordered})

def updateRanking(request):
    print "updateRanking"

    currentTeamMate = request.user.teammate_set.all()[0]
    #teams = Team.objects.filter(name=request.path_info.split("/")[-1])
    teamMatez =  currentTeamMate.team.teammate_set.all()

    colors = ["#F7464A","#46BFBD","#FDB45C","#949FB1","#4D5360","#F7464A","#46BFBD","#FDB45C","#949FB1","#4D5360"]
    response_data = []
    idx =0;
    for teamMate in teamMatez:
        print idx

        teamMate.votesNumber = 0
        teamMate.votesNumber = Vote.objects.filter(teamMate=teamMate).count()
        response_data1 = {}
        response_data1['value'] = teamMate.votesNumber
        response_data1['color'] = colors[idx]
        response_data1['label'] = teamMate.user.username
        response_data1['highlight'] = "#5AD3D1"
        response_data.append(response_data1)
        idx+=1


    return HttpResponse(json.dumps(response_data))


