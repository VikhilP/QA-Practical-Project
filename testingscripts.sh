#!/bin/bash
source venv/bin/activate

python3 -m pytest service-1/testing/test_service-1.py --cov=.
python3 -m pytest service-2/testing/test_service-2.py --cov=.
python3 -m pytest service-3/testing/test_service-3.py --cov=.
python3 -m pytest service-4/testing/test_service-4.py --cov=. 