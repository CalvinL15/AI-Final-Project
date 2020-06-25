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

import initialize
import Player_Pedestrians

def main(argv=()):
  initialize.level
  initialize.pedestrian_move_case
  initialize.algorithm_case
  initialize.level = int(argv[1]) if len(argv) > 1 else 0

  #PEDESTRIAN_MOVE_CASE:
  #0 = NOT MOVING
  #1 = MOVING RANDOMLY
  #2 = All pedestrians moving to the direction of the origin position of the player 
  initialize.pedestrian_move_case = int(argv[2]) if len(argv) > 2 else 1

  #Lists of algorithms implemented:
  #0 = Manually play with arrow keys!
  #1 = Use algorithm!
  initialize.algorithm_case = int(argv[3]) if len(argv) > 1 else 1

  # Build the game.
  game = initialize.make_game(initialize.level)
  croppers = initialize.make_croppers(initialize.level)
  ui = human_ui.CursesUi(
      keys_to_actions={curses.KEY_UP: 0, curses.KEY_DOWN: 1, curses.KEY_LEFT: 2, curses.KEY_RIGHT: 3, -1: 4,'q': 5, 'Q': 5},
      delay=100, colour_fg=initialize.COLOUR_FG,
      croppers=croppers)
  ui.play(game)

if __name__ == '__main__':
  main(sys.argv)