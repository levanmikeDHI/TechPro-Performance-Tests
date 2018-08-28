__author__ = 'mike.levan'

from random import randint
from common import *
from locust import HttpLocust, TaskSet, task, web

keywordslist=['java','python','sap','javascript','jenkins','hadoop','xml','ruby','html','css','docker']
locationlist=['New+York%2C+NY','Washington%2C+DC','Dallas%2C+TX','Atlanta%2C+GA','Chicago%2C+IL','Houston%2C+TX','Los+Angeles%2C+CA']
statelist=['ca','nj','tx','ny']

class SearchKeywordLocation(TaskSet):

    @task(2)
    def search_by_keyword_location(self):
        keyword = str(keywordslist[randint(0,len(keywordslist)-1)])
        location = str(locationlist[randint(0,len(locationlist)-1)])
        response = self.client.post("/jobs?q=" + keyword + "&l=" + location)

        print "Response status code: ", response.status_code
        print "Response URL: ", response.url

    @task(1)
    def search_by_keyword_location_state_only(self):
        keyword = str(keywordslist[randint(0,len(keywordslist)-1)])
        state = str(locationlist[randint(0,len(statelist)-1)])
        response = self.client.post("/jobs?q=" + keyword + "&l=" + state)

        print "Response status code: ", response.status_code
        print "Response URL: ", response.url


class SearchTasks(TaskSet):

    tasks={SearchKeywordLocation:2}

class SearchLoadTests(HttpLocust):
    task_set = SearchTasks
    stop_timeout = 1200
