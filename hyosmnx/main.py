#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/3/19 13:53
# Reference: https://towardsdatascience.com/making-artistic-maps-with-python-9d37f5ea8af0
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
###############################################################################
#                          1. Importing Libraries                             #
###############################################################################
# To make maps
import PIL
import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.lines import Line2D

# To add text and a border to the map
from PIL import Image, ImageOps, ImageColor, ImageFont, ImageDraw




###############################################################################
#                              2. Version Check                              #
###############################################################################
print(f"The NetworkX package is version {nx.__version__}")
print(f"The OSMNX package is version {ox.__version__}")
print(f"The Request package is version {requests.__version__}")
print(f"The PIL package is version {PIL.__version__}")




###############################################################################
#                                3. Get Data                                  #
###############################################################################
# Define city/cities
places = ["Lawrence, Kansas, USA"]

# Get data for places
G = ox.graph_from_place(places, network_type = "all", simplify = True)