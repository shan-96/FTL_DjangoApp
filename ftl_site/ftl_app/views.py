import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import FTL_User


def index(request):
    users = FTL_User.objects.order_by('real_name')
    template = loader.get_template('ftl_app/index.html')
    context = {
        'user_list': users,
    }
    return HttpResponse(template.render(context, request))


def get_error_json():
    error = JsonOutput()
    error.set_error_msg("BAD API REQUEST")
    return json.dumps(error.__dict__, default=lambda o: o.__dict__, indent=2)


def get_user_activity(user_id_list):
    # TODO: implement this !!
    output = JsonOutput()
    for user in user_id_list:
        record = ActivityRecord(user, "FULL_NAME_{}".format(user), "TZ")
        output.add_member(record)

    return json.dumps(output.__dict__, default=lambda o: o.__dict__, indent=2)


def results(request):
    template = loader.get_template('ftl_app/results.html')
    user_id_list = request.POST['user_id_list']
    if user_id_list is None or user_id_list == "":
        return render(request, 'ftl_app/results.html', {
            'error_message': "No user ID specified",
            'results': get_error_json(),
        })

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
