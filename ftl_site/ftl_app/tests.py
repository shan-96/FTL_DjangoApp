import datetime
import json
from django.test import Client
from django.test import TestCase
from django.utils import timezone

from .models import FTL_User_Activity, FTL_User


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
    def setUp(self):
        input_data = {
            'user_id': 'ae2945df',
            'real_name': 'John Wick',
            'tz': 'Asia/Kolkata'}
        ftl_user = FTL_User(user_id=input_data['user_id'], real_name=input_data['real_name'], tz=input_data['tz'])
        FTL_User.save(ftl_user)
        input_data = {
            'user_id': 'ae2945df',
            'start_time': '2020-02-01 13:33',
            'end_time': '2020-02-01 13:54'}
        ftl_user_activity = FTL_User_Activity(user_id=ftl_user, start_time=input_data['start_time'],
                                              end_time=input_data['end_time'])
        FTL_User_Activity.save(ftl_user_activity)

    def test_empty_string(self):
        c = Client()
        response = c.post('/ftl_app/results/', {'user_id_list': ''})
        self.assertEqual(400, response.status_code)

    def test_sample_request(self):
        c = Client()
        response = c.post('/ftl_app/results/', {'user_id_list': 'abc'})
        self.assertEqual(200, response.status_code)

    def test_request_response_logic(self):
        c = Client()
        response = c.post(path='/ftl_app/results/', data={'user_id_list': 'abc'}, follow=True)
        result = json.loads(response.context['results'])
        self.assertEqual(True, result['ok'])
        self.assertEqual(0, len(result['members']))
        self.assertEqual('', result['error_msg'])

    def test_request_output(self):
        c = Client()
        response = c.post(path='/ftl_app/results/', data={'user_id_list': 'ae2945df'}, follow=True)
        result = json.loads(response.context['results'])
        self.assertEqual(True, result['ok'])
        self.assertEqual(1, len(result['members']))
        self.assertEqual('', result['error_msg'])
