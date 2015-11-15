from django.shortcuts import render
from django.http import HttpResponse
from .models import Participant, Week
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    part_list = Participant.objects.order_by('part_name')
    week = Week.objects.order_by('participant_id')
    template = loader.get_template('survivorpool/index.html')
    context = RequestContext(request, {
        'part_list' : part_list,
        'week_list' : week,
        'max_per_week': find_max_per_week(week)
    })

    return HttpResponse(template.render(context))


def find_max_per_week(lst):
        by_week = [0 for x in range(17)]

        for week in range(1,17):
            week_array = []
            for team in lst:
                if team.week == week:
                    week_array += team.team_abbrv
            by_week[week] = week_array

        max_week = []
        curr_week = 1
        for week in by_week:
            max_week[curr_week] = max(set(week), key=week.count)
            curr_week = curr_week + 1


        return max_week
