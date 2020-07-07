import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import FTL_User, FTL_User_Activity


def index(request):
    template = loader.get_template('ftl_app/index.html')
    context = {
        'title': "FTL APP",
    }
    return HttpResponse(template.render(context, request))


def get_error_json(err_msg):
    error = JsonOutput()
    error.set_error_msg(err_msg)
    return json.dumps(error.__dict__, default=lambda o: o.__dict__, indent=2)


def get_user_activity(user_id_list):
    output = JsonOutput()
    # We could use .select_related() with filter as a JOIN but that makes the for loop complex
    # as the data requested in JSON is not flat
    users = FTL_User.objects.filter(user_id__in=user_id_list)
    for u in users:
        user_activities = FTL_User_Activity.objects.filter(user_id=u.user_id)
        record = ActivityRecord(u.user_id, u.real_name, u.tz)
        for a in user_activities:
            start = a.start_time.strftime("%b %d %Y  %I:%M %p")
            end = a.end_time.strftime("%b %d %Y  %I:%M %p")
            record.activity_periods.append(ActivityPeriod(start, end))
        output.add_member(record)

    # now we have the object. convert it to json
    return json.dumps(output.__dict__, default=lambda o: o.__dict__, indent=2)


def results(request):
    template = loader.get_template('ftl_app/results.html')
    user_id_list = request.POST['user_id_list'].replace(" ", "")
    if user_id_list is None or user_id_list == "":
        response_json = get_error_json("No user id specified. Bad request")
        context = {
            'results': response_json,
        }
        return HttpResponse(template.render(context, request), status=400)

    user_id_list = user_id_list.split(',')

    response_json = get_user_activity(user_id_list)
    context = {
        'results': response_json,
    }
    return HttpResponse(template.render(context, request))


class JsonOutput:
    ok = True
    members = []
    error_msg = ""

    def __init__(self):
        self.ok = True
        self.members = []
        self.error_msg = ""

    def set_error_msg(self, error_string):
        self.ok = False
        self.error_msg = error_string

    def add_member(self, u):
        self.members.append(u)


class ActivityRecord:
    id = ""
    real_name = "NOT_FOUND"
    tz = "NOT_FOUND"
    activity_periods = []

    def __init__(self, id, real_name, tz):
        self.id = id
        self.real_name = real_name
        self.tz = tz
        self.activity_periods = []

    def add_period(self, activity):
        self.activity_periods.append(activity)


class ActivityPeriod:
    start_time = ""
    end_time = ""

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
