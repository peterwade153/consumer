from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Consumer


class ConsumerTestCase(APITestCase):

    def setUp(self):
        Consumer.objects.create(
            consumer_id="0",
            street="707 2nd Cir",
            status="active",
            previous_jobs_count=2,
            amount_due=1058,
            geometry=Point(-112.1981605, 33.59107182)
        )
        Consumer.objects.create(
            consumer_id="1",
            street="45 2nd Vis",
            status="collected",
            previous_jobs_count=3,
            amount_due=1000,
            geometry=Point(-112.1981235, 33.77107182)
        )
        Consumer.objects.create(
            consumer_id="2",
            street="448 Bush Ave",
            status="in_progress",
            previous_jobs_count=2,
            amount_due=758,
            geometry=Point(-112.1981605, 33.59107182)
        )
        Consumer.objects.create(
            consumer_id="3",
            street="448 Bush Ave",
            status="in_progress",
            previous_jobs_count=4,
            amount_due=7589,
            geometry=Point(-112.9981605, 33.59107182)
        )

    def test_list_consumers(self):
        response = self.client.get('/api/consumers', format='json')
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 4)

    def test_list_consumers_by_min_and_max_previous_jobs_count_param(self):
        response = self.client.get('/api/consumers?min_previous_jobs_count=2&max_previous_jobs_count=3', format='json')
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 3)

    def test_list_consumers_by_previous_jobs_count(self):
        response = self.client.get('/api/consumers?previous_jobs_count=3', format='json')
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 1)
    
    def test_list_consumers_by_status(self):
        response = self.client.get('/api/consumers?status=active', format='json')
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 1)
