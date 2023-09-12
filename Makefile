install:
	pip install -U pip && \
		pip install -r requirements.txt

test:
	python -m pytest --vv --cov=quickstart.py 

lint:
	pylint --disable=R,C *.py 

format: 
	black *.py

all: install test lint format
