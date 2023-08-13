install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest  test_search.py

format:
	black *.py
	black mylib/*.py

lint:
	pylint --disable=R,C,W0108,W0621,E1120 mylib/*.py
	

#all: install lint test
all: install lint test format