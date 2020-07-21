from django.urls import path

from . import views

app_name = 'ftl_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    # path('pump/', views.pump, name='pump'),
]
