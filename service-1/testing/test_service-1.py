from flask_testing import TestCase
from flask import url_for
import requests
from requests_mock import mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        app.config['SECRET_KEY'] = "dfs"
        return app

class TestResponse(TestBase):
    def test_index(self):
        with mock() as m:
            m.get('http://service-2:5000/getpositions', text='QB')
            m.get('http://service-3:5000/getpickorder', json=35)
            m.post('http://service-4:5000/calculatedraftround', json={'draft_number': 35, 'draft_round': 2, 'position': 'QB', 'round_pick': 3})
            

            response = self.client.get(url_for("home"))
            a = "You had selected a: QB"
            
            


        self.assertIn(a, response.data.decode())

