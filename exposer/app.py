#!/usr/bin/python

from prometheus_client import start_http_server, Summary, Histogram, Gauge, Counter
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

histogram = Histogram('test_histogram', 'Description of histogram')
gauge = Gauge('test_gauge', 'Description of gauge')
counter = Counter('test_counter', 'Description of counter')

# Decorate function with metric.
@REQUEST_TIME.time()

def scaled_random(max_random):
    number = random.random() * max_random
    return number

def generate_random_metrics(histogram, gauge, counter):
    """ Generate Random Metrics to populate our metrics endpoint """
    
    # Generate random Histogram value
    number = scaled_random(11)
    histogram.observe(number)    # Observe 4.7 (seconds in this case)
    
    # Generate random gauge value
    number = scaled_random(500)
    coin_toss = random.random()

    if coin_toss >= 0.5:
        gauge.inc(number)      # Increment by given value
    else:
        gauge.dec(number)    # Decrement by given value

    # Generate random counter value
    number = scaled_random(5)
    counter.inc(number)     # Increment by Random Value

def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        generate_random_metrics(histogram, gauge, counter)
        process_request(random.random())


