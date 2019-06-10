from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


class HomePageTest(TestCase):

    #    previous two tests have been combined into one and simplified using 
    #    django's built-in test client.   
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    #    Rather than testing hard coded 'constants' this now tests our implementation.

