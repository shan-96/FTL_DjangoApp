from django.db import models


class FTL_User(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=100)

    def __str__(self):
        obj = "User\nid = " + str(self.user_id) + " real_name = " + str(self.real_name) + " tz = " + str(self.tz)
        return obj


class FTL_User_Activity(models.Model):
    user_id = models.ForeignKey(FTL_User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end_time')

    # end_time >= start_time always
    def save(self, *args, **kwargs):
        if self.start_time > self.end_time:
            raise ValueError("Start Time cannot be greater than End Time")

        super().save(*args, **kwargs)

    def __str__(self):
        obj = "User_Activity\nid = " + str(self.user_id) + " start_time = " + str(self.start_time) + " end_time = " + str(
            self.end_time)
        return obj
