import datetime

from django.test import Client
from django.test import TestCase
from django.utils import timezone

from .models import FTL_User_Activity


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


class ResultsViewTest(TestCase):
    def test_empty_string(self):
        c = Client()
        response = c.post('/ftl_app/results/', {'user_id_list': ''})
        self.assertEqual(400, response.status_code)

    def test_sample_request(self):
        c = Client()
        response = c.post('/ftl_app/results/', {'user_id_list': 'abc'})
        self.assertEqual(200, response.status_code)
