from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys
import random

from pycolab import ascii_art
from pycolab import cropping
from pycolab import human_ui
from pycolab import things as plab_things
from pycolab.prefab_parts import sprites as prefab_sprites

from Player_Pedestrians import *

pedestrian_move_case = None
algorithm_case = None
testres = 0
flag = 0
level = None
north = 0
east = 0
west = 0
south = 0
steps = 0

# pylint: disable=line-too-long
MAZES_ART = [
    # Legend:
    #     '#': impassable walls.           
    #     'a - Y (excluding P)': pedestrians.
    #     'P': player starting location.
    #     ' ': boring old maze floor.
    #
    # Maze #0:
    ['#################',
     '#              *#',
     '#               #',
     '#               #',
     '#               #',
     '#    a          #',
     '#               #',
     '#               #',
     '#               #',
     '#P              #',
     '#################'],

    ['#################',
     '#              *#',
     '#               #',
     '#               #',
     '#            c  #',
     '#    a          #',
     '#               #',
     '#               #',
     '#               #',
     '#P              #',
     '#################'],

    ['#############################################',
     '#                                          *#',
     '#                     ######                #',
     '#                                           #',
     '#      #######                              #',
     '#                                           #',
     '#                                           #',
     '#                          #########        #',
     '#                   b                       #',
     '#        #                       a          #',
     '#        #                                  #',
     '#        #                  #          #    #',
     '#        #######            #          #    #',
     '#                           #          #    #',
     '#                                      #    #',
     '#                                           #',
     '#                                           #',
     '#P                                          #',
     '#############################################'],

    ['#############################################',
     '#                                          *#',
     '#                     ######                #',
     '#                                           #',
     '#      #######        b                     #',
     '#           a                               #',
     '#                                           #',
     '#                          #########        #',
     '#                                           #',
     '#        #                       d          #',
     '#        #                                  #',
     '#        #                  #          #    #',
     '#        #######            #          #    #',
     '#                           #          #    #',
     '#                                      #    #',
     '#         c                                 #',
     '#                                           #',
     '#P                                          #',
     '#############################################'],

    ['###################################################################################################',
     '#                                                                                                *#',
     '#                                                                                                 #',
     '#                                                                                                 #',
     '#                           ##########                                                            #',
     '#                                                                 ##################              #',
     '#                                                                                                 #',
     '#                                                               d                                 #',
     '#                                                                                                 #',
     '#                                                                                                 #',
     '#            #                                                                                    #',
     '#            #                                                                                    #',
     '#            #                                                                                    #',
     '#            #             #################                                                      #',
     '#            #                                                                  #                 #',
     '#            #                                                                  #        e        #',
     '#            #                                                                  #                 #',
     '#            #                                       #                          #                 #',
     '#                                  a                 #                          #                 #',
     '#                                                    #######                    #                 #',
     '#                                                                               #                 #',
     '#                                                                               #                 #',
     '#                                                                               #                 #',
     '#      ##############                                                           #                 #',
     '#      #                                                                                          #',
     '#      #                                                                                          #',
     '#                                                                                                 #',
     '#P                                                                                                #',
     '###################################################################################################'],

    ['###################################################################################################',
     '#                                                                                                *#',
     '#                                                                                                 #',
     '#                                                                                                 #',
     '#                           ##########                                                            #',
     '#                                                                 ##################              #',
     '#                                                                                                 #',
     '#                                                               d                                 #',
     '#                                   c                                                             #',
     '#                                                                                                 #',
     '#            #                                                                                    #',
     '#            #                                                                                    #',
     '#            #                                                                                    #',
     '#            #             #################                                                      #',
     '#     b      #                                                                  #           e     #',
     '#            #                                                                  #                 #',
     '#            #                                                                  #                 #',
     '#            #                                       #                          #                 #',
     '#                                  a                 #                          #                 #',
     '#                                                    #######                    #                 #',
     '#                                                                               #                 #',
     '#                                                                               #                 #',
     '#                                                                               #                 #',
     '#      ##############                                                           #                 #',
     '#      #                                                                                          #',
     '#      #                                                                                          #',
     '#                                                                                                 #',
     '#P                                                                                                #',
     '###################################################################################################'],
]

# For dramatic effect, none of the levels start the game with the first
# observation centred on the player; instead, the view in the window is shifted
# such that the player is this many rows, columns away from the centre.
STARTER_OFFSET = [(0, 0),  # For level 0
                  (0, 0),    # For level 1
                  (0, 0),    # For level 2
                  (0, 0),
                  (0, 0),    # For level 2
                  (0, 0)]    # For level 3


# These colours are only for humans to see in the CursesUi.
COLOUR_FG = {' ': (0, 0, 0),        # Default black background
             '@': (999, 862, 110),  # Shimmering golden coins
             '#': (950, 500, 200),    # Walls of the maze
             'a': (900, 100, 700),    
             'b': (900, 100, 700),  
             'c': (222, 623, 999),
             'd': (900, 100, 700),
             'e': (900, 100, 700),
             # 'f': (999, 0, 780),  
             # 'g': (987, 623, 145),
             # 'h': (999, 0, 780),
             # 'i': (999, 0, 780),
             # 'j': (999, 0, 780),  
             # 'k': (987, 623, 145),
             # 'l': (999, 0, 780),
             # 'm': (999, 0, 780),
             # 'n': (999, 0, 780),  
             # 'o': (987, 623, 145),
             # 'p': (999, 0, 780),
             # 'q': (999, 0, 780),
             # 'r': (999, 0, 780),  
             # 's': (987, 623, 145),
             # 't': (999, 0, 780),
             # 'u': (999, 0, 780),
             # 'v': (999, 0, 780),  
             # 'w': (987, 623, 145),
             # 'x': (999, 0, 780),
             # 'y': (999, 0, 780),
             # 'z': (999, 0, 780),  
             # 'A': (987, 623, 145),
             # 'B': (999, 0, 780),
             # 'C': (999, 0, 780),
             # 'D': (999, 0, 780),  
             # 'E': (987, 623, 145),
             # 'F': (987, 623, 145),
             # 'G': (999, 0, 780),
             # 'H': (999, 0, 780),
             # 'I': (999, 0, 780),  
             # 'J': (987, 623, 145),
             # 'K': (987, 623, 145),
             # 'L': (999, 0, 780),
             # 'M': (999, 0, 780),
             # 'N': (999, 0, 780),  
             # 'O': (987, 623, 145),
             # 'Q': (987, 623, 145),
             # 'R': (999, 0, 780),
             # 'S': (999, 0, 780),
             # 'T': (999, 0, 780),  
             # 'U': (987, 623, 145),
             # 'V': (987, 623, 145),
             # 'W': (999, 0, 780),
             # 'X': (999, 0, 780),
             # 'Y': (999, 0, 780),
            #'*': (300, 300, 300),  
             } 

         
def make_game(level):
  """Builds and returns a Better Scrolly Maze game for the selected level."""
  return ascii_art.ascii_art_to_game(
      MAZES_ART[level], what_lies_beneath=' ',
      sprites={
          'P': PlayerSprite,
          'a': PedSprite,
          'b': PedSprite,
          'c': PedSprite,
          'd': PedSprite,
          'e': PedSprite,
          '*': PedSprite,
          # 'f': PedSprite,
          # 'g': PedSprite,
          # 'h': PedSprite,
          # 'i': PedSprite,
          # 'j': PedSprite,
          # 'k': PedSprite,
          # 'l': PedSprite,
          # 'm': PedSprite,
          # 'n': PedSprite, 'o': PedSprite, 'p': PedSprite, 'q': PedSprite, 'r': PedSprite, 's': PedSprite,
          # 't': PedSprite, 'u': PedSprite, 'v': PedSprite, 'w': PedSprite, 'x': PedSprite, 'y': PedSprite,
          # 'z': PedSprite, 'A': PedSprite, 'B': PedSprite, 'C': PedSprite, 'D': PedSprite, 'E': PedSprite,
          # 'F': PedSprite, 'G': PedSprite, 'H': PedSprite, 'I': PedSprite, 'J': PedSprite, 'K': PedSprite,
          # 'L': PedSprite, 'M': PedSprite, 'N': PedSprite, 'O': PedSprite, 'Y': PedSprite, 'Q': PedSprite,
          # 'R': PedSprite, 'S': PedSprite, 'T': PedSprite, 'U': PedSprite, 'V': PedSprite,
          # 'W': PedSprite, 'X': PedSprite, 'Y': PedSprite, '*': PedSprite
          },
      update_schedule=['P', 'a', 'b', 'c', 'd', 'e', '*'],
      #, 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'P', '*'],
      z_order='Pabcde*')
  #fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOQRSTUVWXY*


def make_croppers(level):

  if level == 0:
    return [
        # The player view.
        cropping.ScrollingCropper(rows=11, cols=17, to_track=['P'], initial_offset=STARTER_OFFSET[level])]
  elif level == 1:
    return [cropping.ScrollingCropper(rows=11, cols=17, to_track=['P'], initial_offset=STARTER_OFFSET[level])]
  elif level == 2:
    return [cropping.ScrollingCropper(rows=19, cols=45, to_track=['P'], initial_offset=STARTER_OFFSET[level])]
  elif level == 3:
    return [cropping.ScrollingCropper(rows=19, cols=45, to_track=['P'], initial_offset=STARTER_OFFSET[level])]
  elif level == 4:
    return [cropping.ScrollingCropper(rows=29, cols=99, to_track=['P'], initial_offset=STARTER_OFFSET[level])]
  elif level == 5:
    return [cropping.ScrollingCropper(rows=29, cols=99, to_track=['P'], initial_offset=STARTER_OFFSET[level])]  
  # elif level == 3:
  #   return [cropping.ScrollingCropper(rows=29, cols=106, to_track=['P'], initial_offset=STARTER_OFFSET[level])]  
