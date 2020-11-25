from locust import task, tag, events
from locust.contrib.fasthttp import FastHttpUser
from utils import RequestParser

headers = {'Content-type': 'text/xml', 'User-Agent': 'SkyLoader/0.0.1' }

class SkyLoader(FastHttpUser):

    @events.init.add_listener
    def on_locust_init(self):
        self.request_parser = RequestParser(self, loc = True, ip_loc = True, tiling = True, rgeo = True)

    @tag('HealthCheck')
    @task
    def HealthCheck(self):
        response = self.client.get("/wps2/probe")


    @tag('LocationRQ')
    @task
    def LocationRQ(self):
        body = self.request_parser.select_loc_rq()
    
        response = self.client.post(path="/wps2/location", headers=headers, data=body)

    @tag('IPLocation')
    @task
    def IPLocation(self):
        response = self.client.post("/wps2/ip-location")
    
    @tag('Tiling')
    @task
    def Tiling(self):
        response = self.client.post("/wps2/tiling")

    @tag('RGeo')
    @task
    def RGeo(self):
        response = self.client.post("/wps2/reverse-geo")
