# Introduction

This project comprises of three components which together create an interactive demo for using Prometheus. Those three components are:
  - Prometheus
  - Prometheus Exposer
  - Grafana

# Getting Started

The deployment scripts are designed to run in Linux

To run the demo, just follow these steps:

1. git clone the repository to a local Linux environment 
2. copy .env.example to .env and configure it by exposing available ports, etc.
3. run `./build.sh` from the terminal. If you do not create a .env file, .env.example will be used

The Grafana main dashboard can be reached by visiting the url of the service ie. http://localhost:3000 by default.

The default user and admin are

- User: admin
- Password: 1234

The default Test dashboard is named "Test Dashboard" and assuming you deployed to your localhost can be reached by default here:

http://localhost:3000/d/3yCkNeCmkdd/test-dashboard?orgId=1&refresh=2s

When you are finished testing, you can purge the volumes that have been created by this demo by running `./purge.sh`

# Architecture

The three components tie together in the following way. The Prometheus exposer generates sample metrics and publishes them via a web server. Prometheus is configured to scrape the Prometheus Exposer server for metrics. And Grafana connects to Prometheus in order to display the metrics which Prometheus has scraped.

# Container Connections

docker-compose automatically creates a docker network for the containers to communicate on. Links/host aliases are created for every service in the docker-compose, so that for example grafana can reach the prometheus service by name (in backend mode).

# Grafana Service

Grafana's service is based on the official Grafana image and listens on port 3000 by default. It is configured via the Grafana service dashboard, or by automatically provisioning resources by providing configuring files via the provisioning directory which is volume mounted into the container.

The Grafana main dashboard can be reached by visiting the url of the service ie. http://localhost:3000

The default user and admin are

- User: admin
- Password: 1234

## Ensuring Persistence

A data volume is created for the service in order to persist Grafana data after the container is removed.

## Provisioning Resources

Grafana datasources and dashboards can be automatically provisioned by adding them to the grafana/provisioning directory which is volume mounted into the container. 

New Dashboards can be exported via the Grafana ui and the json files placed in grafana/provisioning/dashboards

# Prometheus Service

The prometheus service is based on the official prometheus image and listens on port 9090 by default. It is configured via prometheus.yml file which is volume mounted into the container.

The default Prometheus dashboard can be reached by visiting the `/graph` path of the service ie. http://localhost:9090/graph

## Ensuring Persistence

A data volume is created for the service in order to persist prometheus data after the container is removed.

## Configuring Endpoints

Prometheus endpoints (ie metrics endpoints of exposers/exporters) can be configured in prometheus/prometheus.yml via new jobs.

```
  - job_name: 'prometheus-exporter'

    # Override the global default and scrape targets from this job every 5 seconds.
    scrape_interval: 5s

    # which path to scrape
    metrics_path: '/metrics'

    static_configs:
      - targets: ['my-expoerter-host:80']
        labels:
            group: 'my_group'
```

# Exposer Service

The exposer service is based on a python library `client_python` and exposes 3 kinds of test metrics:

1. Histogram 
2. Gauge
3. Counter

The service serves metrics to the root path (/) and listens on port 8000 by default

It is built to an image within the ./exposer context where the Dockerfile is located. 

# Code Credits

Thanks to https://github.com/vegasbrianc/prometheus.git for providing guidance on how to automatically provision Grafana dashboards

https://github.com/prometheus/client_python was used to create an example exposer/exporter service.
 
