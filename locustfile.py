# -*- coding: utf-8 -*-

import os
import time

from locust import HttpUser, between, events, task

from common.example_functions import choose_random_page
import requests

default_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

@events.request.add_listener
def my_request_handler(request_type, name, response_time, response_length, response,
                       context, exception, **kwargs):
    events.request.fire(request_type, name, response_time, response_length, response,
                       context, exception)

class WebsiteUser(HttpUser):
    wait_time = between(0, 1) 
    host = "https://www.google.com"



    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
         response = requests.get("https://www.google.com", headers=default_headers)
      #   events.request.fire(request_type='http', name=response.url, response_time=response.elapsed.total_seconds(), response_length=len(request.content), response=response, exception=response.exception)
    #   if (response.status_code<=300):
    #     events.request_success.fire(request_type='http', name=response.url, response_time=response.elapsed.total_seconds(), response_length=len(response.content))
    #   else:
    #     events.request_failure.fire(request_type='http', name=response.url, response_time=response.elapsed.total_seconds() , response_length=len(response.content))
        
    @task
    def do_the_job(self):
        pass

    @events.test_stop.add_listener
    def on_test_start(environment, **kwargs):
       
        response = requests.get("https://www.google.com", headers=default_headers)
   
    
        if response.status_code < 400 and response.status_code >= 200:
            events.request_success.fire(request_type='http', name=response.url, response_time=response.elapsed.total_seconds(), response_length=len(response.content))
        else:
            events.request_failure.fire(request_type='http', name=response.url, response_time=response.elapsed.total_seconds() , response_length=len(response.content))
        
