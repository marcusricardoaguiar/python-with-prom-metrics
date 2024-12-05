# python-with-prom-metrics
Python application with Prometheus Metrics

## Freezing packages and install from requirements.txt

As a best practices, always set all dependencies on requirements.txt file:
```
pip freeze > requirements.txt
pip install -r requirements.txt
```

## Virtual environment

Run the virtual environment to isolate the dependencies:
```
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## Running the application

In order to run the application, use the following command:
```
python3 run.py
```

## Running unit tests

The following command should be used to run unit tests:
```
python -m unittest discover tests
```

## Running linting

The following command should be used to run lint:
```
pylint app tests
```
