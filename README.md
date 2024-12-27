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

## Checking tests coverage

The following command should be used to check tests coverage:
```
coverage run -m unittest discover
coverage report
coverage report --format=total
```

## Running linting

The following command should be used to run lint:
```
pylint app tests
```

## Running conda environment

This is still not being used. It will be added later on...
```
Set-Alias conda _conda
conda create -n python-with-prom-metrics flask
conda init
conda activate python-with-prom-metrics
```