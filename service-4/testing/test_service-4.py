from flask_testing import TestCase
from flask import url_for
from app import app, calculatedraftround

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_service_4(self):
        position = "SS"
        pick = 35
        senditems = {"dnum": pick, "pos": position}
        info = self.client.post(url_for("calculatedraftround"), json=senditems).json
        print(info)
        print("Testing variables")
        #infos = info.json()
        
        self.assertIn("'draft_round': 2",str(info))
    
    def test_service4_again(self):
        position = "SS"
        pick = 32
        senditems = {"dnum": pick, "pos": position}
        info = self.client.post(url_for("calculatedraftround"), json=senditems).json
        
        
        self.assertIn("'round_pick': 32",str(info))
       