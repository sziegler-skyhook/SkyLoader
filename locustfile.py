from locust import task, tag
from locust.contrib.fasthttp import FastHttpUser

headers = {'Content-type': 'text/xml', 'User-Agent': 'SkyLoader/0.0.1' }

class SkyLoader(FastHttpUser):
    @tag('HealthCheck')
    @task
    def HealthCheck(self):
        response = self.client.get("/wps2/probe")


    @tag('LocationRQ')
    @task
    def LocationRQ(self):
        body = """<LocationRQ xmlns='http://skyhookwireless.com/wps/2005' version='2.23' street-address-lookup='none'>
                    <authentication version='2.2'>
                        <key key='eJwNwckNACAIBMC3xZC4gMc-JWpTxt51Bgn5Q4a1dFgndxSK11BpahQti7JsuPcYUIv7AA-hCws' username ='SimonReplay'/>
                    </authentication>
                    <access-point>
                        <mac>0014D1B1403A</mac>
                        <ssid>TRENDnet733_2.4GHz_VRXT</ssid>
                        <signal-strength>-83</signal-strength>
                        <age>84</age>
                    </access-point>
                    <access-point>
                        <mac>2C5D93520708</mac>
                        <ssid>CableWiFi</ssid>
                        <signal-strength>-89</signal-strength>
                        <age>84</age>
                    </access-point>
                </LocationRQ>"""
    
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
