# filepath: /Users/pulkit/Desktop/projects/Task Management Application/locustfile.py
from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def home(self):
        self.client.get("/")

    @task(2)
    def about(self):
        self.client.get("/about")

    @task(3)
    def contact(self):
        self.client.get("/contact")

    @task(4)
    def login(self):
        self.client.get("/login")

    @task(5)
    def register(self):
        self.client.get("/register")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)