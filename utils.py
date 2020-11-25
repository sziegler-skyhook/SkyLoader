import random

class RequestParser:
    '''Parse location logs and read them into memory'''

    def __init__(self, loc = False, ip_loc = False, tiling = False, rgeo = False):
        LOCATION_FILE = "./logs/LocationRQ.log"
        IP_LOCATION_FILE = "./logs/IPLocationRQ.log"
        TILING_FILE = "./logs/TilingRQ.log"
        RGEO_FILE = "./logs/ReverseGeoRQ.log"
       
        if loc == True:
            with open(LOCATION_FILE, 'r') as f:
                self.loc_rqs = f.readlines()
        else: self.loc_rqs = None

        if ip_loc == True:
            with open(IP_LOCATION_FILE, 'r') as f:
                self.ip_loc_rqs = f.readlines()
        else: self.ip_loc_rqs = None

        if tiling == True:
            with open(TILING_FILE, 'r') as f:
                self.tiling_rqs = f.readlines()
        else: self.tiling_rqs = None
    
        if rgeo == True:
            with open(RGEO_FILE, 'r') as f:
                self.rgeo_rqs = f.readlines()
        else: self.rgeo_rqs = None

    def select_loc_rq(self):
        if self.loc_rqs is None:
            raise ValueError('There is no location bank loaded')
        
        index = random.randrange(0, len(self.loc_rqs))

        return self.loc_rqs[index]
        
    def select_ip_loc_rq(self):
        if self.ip_loc_rqs is None:
            raise ValueError('There is no IP location bank loaded')
        
        index = random.randrange(0, len(self.ip_loc_rqs))

        return self.ip_loc_rqs[index]

    def select_tiling_rq(self):
        if self.tiling_rqs is None:
            raise ValueError('There is no tiling bank loaded')
        
        index = random.randrange(0, len(self.tiling_rqs))

        return self.tiling_rqs[index]

    def select_rgeo_rq(self):
        if self.rgeo_rqs is None:
            raise ValueError('There is no RGeo bank loaded')
        
        index = random.randrange(0, len(self.rgeo_rqs))

        return self.rgeo_rqs[index] 

if __name__ == "__main__":
    request_parser = RequestParser(loc = True, ip_loc = True, tiling = True, rgeo = True)
    print(request_parser.select_loc_rq())
    print(request_parser.select_ip_loc_rq())
    print(request_parser.select_tiling_rq())
    print(request_parser.select_rgeo_rq())
