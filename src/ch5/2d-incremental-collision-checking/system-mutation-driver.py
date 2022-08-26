#!/usr/bin/python3

from support.unit_norms import *
from support.Polygon import *
from support.Line import *
from support.Point import *
from support.World import *
from support.star_algorithm import *
from support.doubly_connected_edge_list import *
from pygame_rendering.pygame_loop_support import *
from pygame_rendering.render_support import *
from voronoi_regions import *
from feature_markers import *
from polygon_debugging import *
from region_tests import *
from file_loader import *
from transform_polygon import *

def pygame_transform_loop(screen, P):
  lalt = 256
  lshift = 1
  ctrl = 64
  OPList = [P]
  while 1:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONUP:
        p = pygame.mouse.get_pos()
        print(p)
        if pygame.key.get_mods() == ctrl:
          clear_frame(screen)
          gradually_rotate_system(OPList, 0, p, screen)
          # sanity_check_polygon(screen, P)
        elif pygame.key.get_mods() == lalt:
          clear_frame(screen)
          gradually_translate_polygon(P, p)
          sanity_check_polygon(screen, P)
        elif pygame.key.get_mods() == lshift:
          clear_frame(screen)
          sanity_check_polygon(screen, P)
        else:
          print(p)

def get_step_rotation_matrix(P, t):
  rad_theta = compute_rotation(P.get_front_edge(), t)
  deg = abs(rad_theta * 180 / np.pi)
  step_rad = rad_theta / deg
  r_mat = get_cc_rotation_matrix(step_rad)
  return deg,r_mat

def gradually_rotate_system(OPList, P_index, t, screen = None):
  steps, r_mat = get_step_rotation_matrix(OPList[P_index], t)
  for step in range(int(steps)):
    rotate_polygon(OPList[P_index], r_mat)
    clear_frame(screen)
    for i in range(len(OPList)):
      sanity_check_polygon(screen, OPList[i])

def single_polygon_mod():
  if len(sys.argv) < 2:
    print("provide a file")
    sys.exit()
  # if sys.argv[-1] == '-v':
  #   rf = lambda P, p, screen : find_vertex_region(P, p, screen)
  # elif sys.argv[-1] == '-e':
  #   rf = lambda P, p, screen : find_edge_region(P, p, screen)
  # else:
  #   rf = lambda P, p, screen : find_all_region(P, p, screen)
  
  filename = sys.argv[1]
  
  A = build_polygon(filename)
  if A == None:
    print("the polygon is invalid. exiting...")
    sys.exit()
  A.color = colors["white"]
  A.v_color = colors["cyan"]
  A.e_color = colors["tangerine"]
  pygame.init()
  screen = create_display(1000,1000)
  sanity_check_polygon(screen, A)
  pygame_transform_loop(screen, A)

def main():
  single_polygon_mod()

main()
