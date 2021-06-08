#!/bin/bash
source venv/bin/activate
#pip3 install -r requirements.txt
python3 -m pytest service-1/testing/test_service-1.py --cov=application
python3 -m pytest service-2/testing/test_service-2.py --cov=app
python3 -m pytest service-3/testing/test_service-3.py --cov=app
python3 -m pytest service-4/testing/test_service-4.py --cov=app