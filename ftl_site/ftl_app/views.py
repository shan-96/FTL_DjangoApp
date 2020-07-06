from django.http import HttpResponse
from django.template import loader
from .models import FTL_User


def index(request):
    users = FTL_User.objects.order_by('real_name')
    template = loader.get_template('ftl_app/index.html')
    context = {
        'user_list': users,
    }
    return HttpResponse(template.render(context, request))


def results(request):
    return HttpResponse("This is a API test")
