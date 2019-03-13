# Introduction

This project comprises of three components which together create an interactive demo for using Prometheus. Those three components are:
  - Prometheus
  - Prometheus Exposer
  - Grafana

# Getting Started

The deployment scripts are designed to run in Linux

To run the demo, just git clone the repository to a local Linux environment and run `./build.sh` from the terminal.

When you are finished testing, you can purge the volumes that have been created by this demo by running `./purge.sh`

# Architecture

The three components tie together in the following way. The Prometheus exposer generates sample metrics and publishes them via a web server. Prometheus is configured to scrape the Prometheus Exposer server for metrics. And Grafana connects to Prometheus in order to display the metrics which Prometheus has scraped.

# Container Connections

docker-compose automatically creates a docker network for the containers to communicate on. Links/host aliases are created for every service in the docker-compose, so that for example grafana can reach the prometheus service by name (in backend mode).

# Grafana Provisioning

Grafana datasources and dashboards are automatically provisioned by volume mounting the grafana/provisioning files. 

New Dashboards can be exported via the Grafana ui and the json files placed in grafana/provisioning/dashboards

# Prometheus Endpoints

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
 
