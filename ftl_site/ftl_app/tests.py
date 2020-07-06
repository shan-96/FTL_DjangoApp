from django.test import TestCase
from django.utils import timezone
from .models import FTL_User_Activity
import datetime


class UserActivityTests(TestCase):

    def test_start_date_should_be_less_than_end_date(self):
        """
        we have constraint while saving start and end date. lets test that
        """
        start = timezone.now()
        end = start - datetime.timedelta(minutes=30)
        activity = FTL_User_Activity()
        activity.start_time = start
        activity.end_time = end
        self.assertRaises(ValueError, activity.save, "start time should be less than or equal to end time")
