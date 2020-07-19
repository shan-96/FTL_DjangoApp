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
        json_str = ''''{
	"ok": true,
	"members": [{
			"id": "W012A3CDE",
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "W07QCRPA4",
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]
}'''
        self.input_data = json.loads(json_str)
        FTL_User.save(**self.input_data)

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
