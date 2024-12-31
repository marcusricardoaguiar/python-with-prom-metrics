# python-with-prom-metrics
Python application with Prometheus Metrics

## Build python image docker

```
docker build -t python-with-prom-metrics .
```

## Run python image docker

```
docker run -d -p 5000:5000 --name python-with-prom-metrics python-with-prom-metrics
```

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

## Running Prometheus

The following command will spin up a prometheus container to pull metrics from the application:
```
docker run \
    -p 9090:9090 \
    -v $(pwd)/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus
```
note: on Windows, you need to start docker desktop.

## Access Prometheus Deployment

Just try localhost:9090 on your browser

### Queries

```
sum by (status_code) (http_requests_total{endpoint="/client",method="GET"})
rate(http_request_duration_seconds_bucket{endpoint="/client", method="GET", status_code="404"}[1h])
```

## Running Grafana

The following command will spin up a grafana container to show the Prometheus Metrics with custom charts:
```
docker run -d \
    -p 3000:3000 \
    -v $(pwd)/grafana/provisioning:/etc/grafana/provisioning \
    -v $(pwd)/grafana/dashboards:/etc/grafana/dashboards \
    -v $(pwd)/grafana/provisioning/dashboards/dashboard.yml:/etc/grafana/provisioning/dashboards/dashboard.yml \
    -v $(pwd)/grafana/provisioning/datasources/datasources.yml:/etc/grafana/provisioning/datasources/datasources.yml \
    -e GF_SECURITY_ADMIN_PASSWORD='123456' \
    --name=grafana grafana/grafana-enterprise
```
note: on Windows, you need to start docker desktop.

## Access Grafana Deployment

Just try localhost:3000 on your browser and type the following:
 - Username: admin
 - Password: 123456


## Run docker compose

```
docker-compose up
docker-compose down
```

## Running conda environment

This is still not being used. It will be added later on...
```
Set-Alias conda _conda
conda create -n python-with-prom-metrics flask
conda init
conda activate python-with-prom-metrics
```
