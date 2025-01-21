"""
Environment for rrt_2D
@author: huiming zhou
"""
import json
import pymap3d as pm
import copy
from shapely import Polygon, LineString
import os 

class Env:
    def __init__(self):

        # Load the data from the pickle file
        file_name_list = ['Sampling_based_Planning','data','seachart.json']
        file_name = os.path.join(*file_name_list)
        with open(file_name, 'r') as f:
            land_polygons = json.load(f)
        land_polygons = land_polygons["land"]

        x0, y0 = 999,999
        xn, yn = 0,0
        for polygon in land_polygons:
            polygon_ne = []
            for x,y in polygon["polygon"]:
                if x < x0:
                    x0 = copy.deepcopy(x)
                if y < y0:
                    y0 = copy.deepcopy(y)
                if xn < x:
                    xn = copy.deepcopy(x)
                if yn < y:
                    yn = copy.deepcopy(y)

        self.polygon_lists_ne = []
        for polygon in land_polygons:
            polygon_ne = []
            for x,y in polygon["polygon"]:
                n,e = self.lat_lon_to_north_east(x,y,x0,y0)
                polygon_ne.append((n,e))
            self.polygon_lists_ne.append(Polygon(polygon_ne))

        xn,yn = self.lat_lon_to_north_east(xn,yn,x0,y0)

        self.x_range = (0, xn-x0)
        self.y_range = (0, yn-y0)
        self.boundary_polygon = Polygon([(0,0), (xn-x0,0), (xn-x0, yn-x0), (0, yn-x0)])
        self.boundary = LineString([(0,0), (xn-x0,0), (xn-x0, yn-x0), (0, yn-x0), (0,0)])

        #self.obs_boundary = self.obs_boundary()
        #self.obs_circle = self.obs_circle()
        #self.obs_rectangle = self.obs_rectangle()

    @staticmethod
    def lat_lon_to_north_east(lat: float, lon: float, lat0: float, lon0: float) -> (float, float):
        """ Converts a point in (latitude, logitude) into (North, East) w.r.t. a reference point (lat_0, lon_0)

        Args:
            lat: North component of the point
            lon: East component of the point
            lat0: Latitude of the reference point
            lon0: Longitude of the reference point

        Returns:
            north, east: North and East of the point
        """
        north, east, _ = pm.geodetic2ned(lat=lat, lon=lon, h=0, lat0=lat0, lon0=lon0, h0=0)
        return north, east
    