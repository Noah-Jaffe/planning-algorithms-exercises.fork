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
from transform_system import *

def construct_star_diagram(A, O):
  sl = build_star(A.get_front_edge(),O.get_front_edge())

  obs_spc = derive_obstacle_space_points(sl)
  return obs_spc

def pygame_transform_voronoi_system_loop(screen, A, O):
  '''
  Driver function interactions between two polygons A and static O
  '''

  lalt = 256
  lshift = 1
  ctrl = 64
  space = 32
  
  while 1:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONUP:
        p = pygame.mouse.get_pos()
        print(p)
        if pygame.key.get_mods() == ctrl:
          clear_frame(screen)
          gradually_rotate_voronoi_system(A, O, p, screen)
        elif pygame.key.get_mods() == lalt:
          clear_frame(screen)
          gradually_translate_voronoi_system(A,O,p, screen)
        elif pygame.key.get_mods() == lshift:
          clear_frame(screen)
          gradually_rotate_voronoi_system(A, O, p, screen)
          gradually_translate_voronoi_system(A,O,p, screen)
          # sanity_check_polygon(screen, A)
          # sanity_check_polygon(screen, O)
        else:
          draw_lines_between_points(screen, construct_star_diagram(A,O), colors["yellow"])
          pygame.display.update()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        ptlist = []
        counter = 0
        while pygame.MOUSEBUTTONUP not in [event.type for event in pygame.event.get()]:
          if not counter % 300:
            ptlist.append(pygame.mouse.get_pos())
            frame_draw_dot(screen, ptlist[-1], colors["yellow"])
            pygame.display.update()
          counter+=1
        time.sleep(1)
        clear_frame(screen)
        
        for p in range(len(ptlist)):
          
          if p % 5:
          # gradually_translate_voronoi_system(A,O,p, screen)
            gradually_rotate_voronoi_system(A, O, ptlist[p], screen)
          gradually_translate_voronoi_system(A,O,ptlist[p], screen)

          

def double_polygon_mod():
  if len(sys.argv) < 3:
    print("provide two files")
    sys.exit()
  
  # polygon construction
  A,O = build_polygon(sys.argv[1]),build_polygon(sys.argv[2])
  if A == None or O == None:
    print("one of the regions is none.")
    sys.exit()
  
  A.color = colors["green"]
  A.v_color = colors["cyan"]
  A.e_color = colors["tangerine"]
  
  O.color = colors["white"]
  O.v_color = colors["yellow"]
  O.e_color = colors["red"]

  pygame.init()
  screen = create_display(1000,1000)
  sanity_check_polygon(screen, A)  
  sanity_check_polygon(screen, O)
  pygame_transform_voronoi_system_loop(screen, A, O)

def main():
  double_polygon_mod()

main()