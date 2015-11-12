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
    })

    return HttpResponse(template.render(context))