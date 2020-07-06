from django.shortcuts import render
from django.http import HttpResponse
from .models import FTL_User


def index(request):
    users = FTL_User.objects.order_by('real_name')
    output = ", ".join([u.real_name for u in users])
    return HttpResponse(output)


def results(request):
    return HttpResponse("This is a API test")
