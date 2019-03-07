# Introduction

This project comprises of three components which together create an interactive demo for using Prometheus. Those three components are:
  - Prometheus
  - Prometheus Exposer
  - Grafana

# Architecture

The three components tie together in the following way. The Prometheus exposer generates sample metrics and publishes them via a web server. Prometheus is configured to scrape the Prometheus Exposer server for metrics. And Grafana connects to Prometheus in order to display the metrics which Prometheus has scraped.



