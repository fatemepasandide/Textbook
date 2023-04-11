from django.test import TestCase
import requests


class TestCourseListView(TestCase):
    def setUp(self) -> None:
        self.url = "course/"
        return super().setUp()
    
    def test_corse_list_returns_200(self):
        response = requests.get(self.url)
        self.assertEqual(response,200)


