#!/usr/bin/python3

import numpy as np
from support.Line import *

class World:
  '''
  Abstract idea that a world has rules that can dictate boundries and behaviors.
  '''
  
  def __init__(self):
    self.boundries = [] # the edges of the world, 4 = rectangle like, 3 = triangle like, etc... acts like an obsticle, but everything happens inside of it, or wraps around it
    self.edge_types = {} # for each edge, starting on polar 0, stores what kind of edge it is, infinite, closed, wrapped, etc...
    # should edge_types look like {(p1,p2):<val>}? is that efficent?
    self.obsticles = [] # the points for the obsticles
    self.robot_index = -1 # is this needed? what if we want more than 1 moving object? is this possible?
  
  """
  def create_half_plane(self, p1, p2):
    self.half_planes.append(create_edge(p1, p2))
  
  def test_plane(self, p1, hp_id = 0):
    if len(self.half_planes) == 0:
      print("there are no half planes to test!")
      return None
    val = self.half_planes[hp_id].test_point(p1)
    print(val)
    return val
  
  def test_set_of_planes(self, p1):
    f = 0
    for i in range(len(self.half_planes)):
      f = self.half_planes[i].test_point(p1)
      if f != 1:
        return f
    return f
    """
