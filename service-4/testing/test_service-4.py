from flask_testing import TestCase
from flask import url_for
from app import app, calculatedraftround

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_service_4(self):
        position = "QB"
        pick = 224
        senditems = {"dnum": pick, "pos": position}
        info = self.client.post(url_for("calculatedraftround"), json=senditems).json
        print(info)
        print("Testing variables")
        #infos = info.json()
        
        self.assertIn("'draft_round': 7",str(info))

        position = "QB"
        pick = 1
        senditems = {"dnum": pick, "pos": position}
        info = self.client.post(url_for("calculatedraftround"), json=senditems).json
        print(info)
        print("Testing variables")
        #infos = info.json()
        
        self.assertIn("'draft_round': 1",str(info))

        position = "QB"
        pick = 33
        senditems = {"dnum": pick, "pos": position}
        info = self.client.post(url_for("calculatedraftround"), json=senditems).json
        print(info)
        print("Testing variables")
        #infos = info.json()
        
        self.assertIn("'draft_round': 2",str(info))

        position = "QB"
        pick = 65
        senditems = {"dnum": pick, "pos": position}
        info = self.client.post(url_for("calculatedraftround"), json=senditems).json
        print(info)
        print("Testing variables")
        #infos = info.json()
        
        self.assertIn("'draft_round': 3",str(info))

        position = "QB"
        pick = 97
        senditems = {"dnum": pick, "pos": position}
        info = self.client.post(url_for("calculatedraftround"), json=senditems).json
        print(info)
        print("Testing variables")
        #infos = info.json()
        
        self.assertIn("'draft_round': 4",str(info))

        position = "QB"
        pick = 165
        senditems = {"dnum": pick, "pos": position}
        info = self.client.post(url_for("calculatedraftround"), json=senditems).json
        print(info)
        print("Testing variables")
        #infos = info.json()
        
        self.assertIn("'draft_round': 6",str(info))