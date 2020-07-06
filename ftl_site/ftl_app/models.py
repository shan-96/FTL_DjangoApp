from django.db import models


class FTL_User(models.Model):
    id = models.CharField(max_length=200, unique=True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=100)
    # pub_date = models.DateTimeField('date published')


class FTL_User_Activity(models.Model):
    id = models.ForeignKey(FTL_User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end_time')
