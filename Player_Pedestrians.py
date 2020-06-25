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

steps = 0
flag = 0
north = 0
east = 0
west = 0
south = 0 

class PlayerSprite(prefab_sprites.MazeWalker):
  def __init__(self, corner, position, character):
    """Constructor: just tells `MazeWalker` we can't walk through walls."""
    super(PlayerSprite, self).__init__(
        corner, position, character, impassable='#')

  def update(self, actions, board, layers, backdrop, things, the_plot):
    initialize.algorithm_case = 1
    if initialize.algorithm_case != 0 and actions != 5:
      actions = 20

    if initialize.algorithm_case == 1:
      if initialize.level < 6 and initialize.level != 0:
        row, col = self.position
        rowA, colA = things['a'].position
        rowB, colB = things['b'].position
        rowC, colC = things['c'].position
        rowD, colD = things['d'].position
        rowE, colE = things['e'].position
        global flag
        global steps
        if abs(row-rowA) + abs(col-colA) >= 6 and abs(row-rowB) + abs(col-colB) >= 6 and abs(row-rowC) + abs(col-colC) >= 4 and abs(row-rowD) + abs(col-colD) >= 6 and abs(row-rowE) + abs(col-colE) >= 6:
          flag = random.choice([0, 1])
          if layers['#'][row-1, col]: 
            steps = steps + 1
            self._east(board, the_plot)
          elif layers['#'][row, col+1]:
            steps = steps + 1
            self._east(board, the_plot)    
          elif flag == 0:
              flag = random.choice([0, 1]) #made it that it is more likely for flag = 1       
          if flag == 0:
            steps = steps + 1
            self._north(board, the_plot)
          else:
            steps = steps + 1
            self._east(board, the_plot)
        elif abs(row-1-rowA) + abs(col-colA) >= 5 and abs(row-1-rowB) + abs(col-colB) >= 5 and abs(row-1-rowC) + abs(col-colC) >= 3 and abs(row-1-rowD) + abs(col-colD) >= 5 and abs(row-1-rowE) + abs(col-colE) >= 5:  
          if layers[' '][row-1, col] or layers['*'][row-1, col]: 
            steps = steps + 1
            self._north(board, the_plot)
          elif abs(row-rowA) + abs(col+1-colA) >= 5 and abs(row-rowB) + abs(col+1-colB) >= 5 and abs(row-rowC) + abs(col+1-colC) >= 3 and abs(row-rowD) + abs(col+1-colD) >= 5 and abs(row-rowE) + abs(col+1-colE) >= 5:
            if layers[' '][row, col+1] or layers['*'][row, col+1]: 
              steps = steps + 1
              self._east(board, the_plot)  
        elif abs(row-rowA) + abs(col+1-colA) >= 5 and abs(row-rowB) + abs(col+1-colB) >= 5 and abs(row-rowC) + abs(col+1-colC) >= 3 and abs(row-rowD) + abs(col+1-colD) >= 5 and abs(row-rowE) + abs(col+1-colE) >= 5:
          if layers[' '][row, col+1] and layers['*'][row, col+1]: 
            steps = steps + 1
            self._east(board, the_plot)  
          else: 
            steps = steps + 1
            self._east(board, the_plot)
        elif abs(row-rowA) + abs(col-colA) >= 4 and abs(row-rowB) + abs(col-colB) >= 4 and abs(row-rowC) + abs(col-colC) >= 2 and abs(row-rowD) + abs(col-colD) and abs(row-rowE) + abs(col-colE) >= 4:
          if abs(row-rowA) + abs(col+1-colA) >= 5 and abs(row-rowB) + abs(col+1-colB) >= 5 and abs(row-rowC) + abs(col+1-colC) >= 3 and abs(row-rowD) + abs(col+1-colD) >= 5 and abs(row-rowE) + abs(col+1-colE) >= 5: 
            if layers['#'][row, col+1]: 
              if layers[' '][row-1, col] and layers['*'][row-1, col] and abs(row-1-rowA) + abs(col-colA) >= 5 and abs(row-1-rowB) + abs(col-colB) >= 5 and abs(row-1-rowC) + abs(col-colC) >= 3 and abs(row-1-rowD) + abs(col-colD) >= 5 and abs(row-1-rowE) + abs(col-colE) >= 5:
                steps = steps + 1
                self._north(board, the_plot)
              elif layers[' '][row+1, col] and layers['*'][row+1, col]and abs(row+1-rowA) + abs(col-colA) >= 5 and abs(row+1-rowB) + abs(col-colB) >= 5 and abs(row+1-rowC) + abs(col-colC) >= 3 and abs(row+1-rowD) + abs(col-colD) >= 5 and abs(row+1-rowE) + abs(col-colE) >= 5:  
                steps = steps + 1
                self._south(board, the_plot)
              elif layers[' '][row, col-1] and layers['*'][row, col-1] and abs(row-rowA) + abs(col-1-colA) >= 5 and abs(row-rowB) + abs(col-1-colB) >= 5 and abs(row-rowC) + abs(col-1-colC) >= 3 and abs(row-rowD) + abs(col-1-colD) >= 5 and abs(row-rowE) + abs(col-1-colE) >= 5: 
                steps = steps + 1
                self._west(board, the_pot)  
            else: self._east(board, the_plot)
          elif abs(row-1-rowA) + abs(col-colA) >= 5 and abs(row-1-rowB) + abs(col-colB) >= 5 and abs(row-1-rowC) + abs(col-colC) >= 3 and abs(row-1-rowD) + abs(col-colD) >= 5 and abs(row-1-rowE) + abs(col-colE) >= 5:
            if layers['#'][row-1, col]:
              if layers[' '][row+1, col] and layers['*'][row+1, col] and abs(row+1-rowA) + abs(col-colA) >= 5 and abs(row+1-rowB) + abs(col-colB) >= 5 and abs(row+1-rowC) + abs(col-colC) >= 3 and abs(row+1-rowD) + abs(col-colD) >= 5 and abs(row+1-rowE) + abs(col-colE) >= 5:
                steps = steps + 1
                self._south(board, the_plot)
              elif layers[' '][row, col-1] and layers['*'][row, col-1] and abs(row-rowA) + abs(col-1-colA) >= 5 and abs(row-rowB) + abs(col-1-colB) >= 5 and abs(row-rowC) + abs(col-1-colC) >= 3 and abs(row-rowD) + abs(col-1-colD) >= 5 and abs(row-rowE) + abs(col-1-colE) >= 5: 
                steps = steps + 1
                self._west(board, the_plot)                 
            else: 
              steps = steps + 1
              self._north(board, the_plot)
          elif abs(row+1-rowA) + abs(col-colA) >= 5 and abs(row+1-rowB) + abs(col-colB) >= 5 and abs(row+1-rowC) + abs(col-colC) >= 3 and abs(row+1-rowD) + abs(col-colD) >= 5 and abs(row+1-rowE) + abs(col-colE) >= 5:
            if layers['#'][row+1, col]: 
              if layers[' '][row, col-1] and layers['*'][row, col-1] and abs(row-rowA) + abs(col-1-colA) >= 5 and abs(row-rowB) + abs(col-1-colB) >= 5 and abs(row-rowC) + abs(col-1-colC) >= 3 and abs(row-rowD) + abs(col-1-colD) >= 5 and abs(row-rowE) + abs(col-1-colE) >= 5: 
                steps = steps + 1
                self._west(board, the_plot)     
            else: 
              steps = steps + 1
              self._south(board, the_plot)
          elif abs(row-rowA) + abs(col-1-colA) >= 5 and abs(row-rowB) + abs(col-1-colB) >= 5 and abs(row-rowC) + abs(col-1-colC) >= 3 and abs(row-rowD) + abs(col-1-colD) >= 5 and abs(row-rowE) + abs(col-1-colE) >= 5: 
            if layers['#'][row, col-1]: 
              #steps = steps + 1
              self._stay(board, the_plot)
            else: 
              steps = steps + 1
              self._west(board, the_plot)  
     
      elif level == 0:
        row, col = self.position
        rowA, colA = things['a'].position
        if abs(row-rowA) + abs(col-colA) >= 6:
          flag = random.choice([0, 1])
          if flag == 0 and layers[' '][row, col+1] or layers['*'][row, col+1]: 
              steps = steps + 1
              self._east(board, the_plot)
          else: 
            steps = steps + 1
            self._north(board, the_plot)
        elif abs(row-1-rowA) + abs(col-colA) >= 5:
          if layers[' '][row-1, col]: 
            steps = steps + 1
            self._north(board, the_plot)
          elif abs(row-rowA) + abs(col+1-colA) >= 5 and layers[' '][row, col+1]: 
            steps = steps + 1
            self._east(board, the_plot)
        elif abs(row-rowA) + abs(col+1-colA) >= 5:
          if layers[' '][row, col+1]: 
            steps = steps + 1
            self._east(board, the_plot)
        elif abs(row-rowA) + abs(col-colA) >= 4:
          if abs(row-1-rowA) + abs(col-colA) >= 5 and layers[' '][row-1, col]: 
            steps = steps + 1
            self._north(board, the_plot)
          elif abs(row-rowA) + abs(col+1-colA) >= 5 and layers[' '][row, col+1]: 
            steps = steps + 1
            self._east(board, the_plot)
          elif abs(row-rowA) + abs(col-1-colA) >= 5 and layers[' '][row, col-1]:
            steps = steps + 1
            self._west(board, the_plot)
          elif abs(row+1-rowA) + abs(col-colA) >= 5 and layers[' '][row+1, col]:
            steps = steps + 1
            self._south(board, the_plot)
          else: 
            #steps = steps + 1
            self._stay(board, the_plot)      
     #   if abs(row-rowA) + abs(col-colA) >= 6 and abs(row-rowB) + abs(col-colB) >= 6 and abs(row-rowD) + abs(col-colD) >= 6 and abs(row-rowD) + abs(col-colD) and abs(row-rowE) + abs(col-colE):

                           
    if actions == 0:    # go upward
      steps = steps + 1
      self._north(board, the_plot)
    elif actions == 1:  # go downward
      steps = steps + 1
      self._south(board, the_plot)
    elif actions == 2:  # go leftward
      steps = steps + 1
      self._west(board, the_plot)
    elif actions == 3:  # go rightward
      steps = steps + 1
      self._east(board, the_plot)
    elif actions == 4:  # stay put
      steps = steps + 1
      self._stay(board, the_plot)
    elif actions == 5:    # just quit
      the_plot.terminate_episode()
    else:
      steps = steps + 1
      self._stay(board, the_plot)


class PedSprite(prefab_sprites.MazeWalker):
 
  def __init__(self, corner, position, character):
    """Constructor: list impassables, initialise direction."""
    super(PedSprite, self).__init__(
        corner, position, character, impassable='#')
    # Choose our initial direction based on our character value.
    # self._initialState = ord(character)%2
    self._initialState = 0

  def update(self, actions, board, layers, backdrop, things, the_plot):
    global north
    global east
    global west
    global south

    if initialize.pedestrian_move_case == 0:
      self._stay(board, the_plot)      
      if self.position == things['P'].position:
        original_stdout = sys.stdout
        with open('out.txt', 'a+') as f:
          sys.stdout = f 
          print("Success!", int(steps/2))
          sys.stdout = original_stdout 
        print("Success!") 
        the_plot.terminate_episode()

    if initialize.pedestrian_move_case == 2:
      if self.character != '*':
        row, col = self.position
        rowP, colP = things['P'].position   
        if abs(row-rowP) + abs(col-colP) <= 3 and (row != 0 and col != 0): 
          the_plot.terminate_episode()
          original_stdout = sys.stdout
          with open('out.txt', 'a+') as f:
            sys.stdout = f 
            print("FAILURE!")
            sys.stdout = original_stdout
          print("FAILURE!")  
        elif self.position == things['P'].position:
          the_plot.terminate_episode()
        global flag   
        flag = random.choice([0, 1])
        if layers['#'][row-1, col]: 
          if layers[' '][row, col-1]:
            self._west(board, the_plot)
        elif flag == 0:
          flag = random.choice([0, 1]) #made it that it is more likely for flag = 1       
        if flag == 0:
          if layers[' '][row+1, col]:
            self._south(board, the_plot)
        else:
          if layers[' '][row, col-1]:
            self._west(board, the_plot)
      if self.position == things['P'].position:
          original_stdout = sys.stdout
          with open('out.txt', 'a+') as f:
            sys.stdout = f 
            print("Success!", int(steps/2))
            sys.stdout = original_stdout 
          print('Success!')
          the_plot.terminate_episode()                     

    if initialize.pedestrian_move_case == 1:
      if self.character != '*':

       # if the_plot.frame % 2:
       #   self._stay(board, the_plot) 
       #   return

          # If there is a wall next to us, we ought to switch direction.
        row, col = self.position
        # C wears a mask so social distancing can be decreaased
        rowC, colC = things['c'].position
        rowP, colP = things['P'].position
        if row != rowC or col != colC:
          flg = 0
          if abs(row-rowP) + abs(col-colP) <= 3 and (row != 0 and col != 0):     
            the_plot.terminate_episode()
            original_stdout = sys.stdout
            with open('out.txt', 'a+') as f:
              sys.stdout = f 
              print("FAILURE!")
              sys.stdout = original_stdout
            print("FAILURE!")
        else:
          if abs(row-rowP) + abs(col-colP) <= 1 and (row != 0 and col != 0): 
            the_plot.terminate_episode()
            original_stdout = sys.stdout
            with open('out.txt', 'a+') as f:
              sys.stdout = f 
              print("FAILURE!")
              sys.stdout = original_stdout
            print("FAILURE!")

        # if layers['#'][row, col-1]: self._initialState = True
        # if layers['#'][row, col+1]: self._initialState = False


        if layers['*'][row-1, col] or layers['*'][row+1, col] or layers['*'][row, col-1] or layers['*'][row, col+1]:
          if(layers[' '][row+1, col]):
            self._south(board, the_plot)

        if not layers['#'][row-1, col] and not layers['#'][row+1, col] and not layers['#'][row, col-1] and not layers['#'][row, col+1]:
          randnum = random.choice([1, 2, 3, 4, 5])
          if(randnum == 1):
            if(layers[' '][row, col-1]):
              self._west(board, the_plot)
          elif(randnum == 2):
            if(layers[' '][row, col+1]):
              self._east(board, the_plot)
          elif(randnum == 3):
            if(layers[' '][row-1, col]):
              self._north(board, the_plot)
          elif(randnum == 4):
            if(layers[' '][row+1, col]):
              self._south(board, the_plot)
          else:
            self._stay(board, the_plot)  

        else:
          if layers['#'][row-1, col] and layers['#'][row, col+1]:
            # print("hi")
            # self._south(board, the_plot)
            if not layers['#'][row+1, col+1]:
              if layers[' '][row+1, col]:
                self._south(board, the_plot)
            elif not layers['#'][row-1, col-1]:
              if layers[' '][row, col-1]:
                self._west(board, the_plot)
            else:
              randnum = random.choice([1, 2])
              if(randnum == 1):
                if layers[' '][row+1, col]:
                  self._south(board, the_plot)
              else:
                if layers[' '][row, col-1]:
                  self._west(board, the_plot)

          elif layers['#'][row+1, col] and layers['#'][row, col+1]:
            # self._west(board, the_plot)
            if not layers['#'][row+1, col-1]:
              if layers[' '][row, col-1]:
                self._west(board, the_plot)
            elif not layers['#'][row-1, col+1]:
              if layers[' '][row-1, col]:
                self._north(board, the_plot)
            else:
              randnum = random.choice([1, 2])
              if(randnum == 1):
                if layers[' '][row, col-1]:
                  self._west(board, the_plot)
              else:
                if layers[' '][row-1, col]:
                  self._north(board, the_plot)

          elif layers['#'][row+1, col] and layers['#'][row, col-1]:
            # self._north(board, the_plot)
            if not layers['#'][row-1, col-1]:
              if layers[' '][row-1, col]:
                self._north(board, the_plot)
            elif not layers['#'][row+1, col+1]:
              if layers[' '][row, col+1]:
                self._east(board, the_plot)
            else:
              randnum = random.choice([1, 2])
              if(randnum == 1):
                if layers[' '][row-1, col]:
                  self._north(board, the_plot)
              else:
                if layers[' '][row, col+1]:
                  self._east(board, the_plot)

          elif layers['#'][row-1, col] and layers['#'][row, col-1]:
            # self._east(board, the_plot)
            if not layers['#'][row-1, col+1]:
              if layers[' '][row, col+1]:
                self._east(board, the_plot)
            elif not layers['#'][row+1, col-1]:
              if layers[' '][row+1, col]:
                self._south(board, the_plot)
            else:
              randnum = random.choice([1, 2])
              if(randnum == 1):
                if layers[' '][row, col+1]:
                  self._east(board, the_plot)
              else:
                if layers[' '][row+1, col]:
                  self._south(board, the_plot)

          elif (north == 0 and layers['#'][row, col-1]) and (not layers['#'][row-1, col] or not layers['*'][row-1, col]):
            if layers[' '][row, col+1]:
              self._east(board, the_plot)
            # print("first")
            # north = 20
            # self._initialState = 1
          elif (east == 0 and layers['#'][row-1, col]) and (not layers['#'][row, col+1] or not layers['*'][row, col+1]):
            if layers[' '][row+1, col]:
              self._south(board, the_plot)
            # print("second")
            # east = 20
          elif (south == 0 and layers['#'][row, col+1]) and (not layers['#'][row+1, col] or not layers['*'][row+1, col]):
            if layers[' '][row, col-1]:
              self._west(board, the_plot)
            # print("third")
            # south = 20
          elif (layers['#'][row+1, col]) and (not layers['#'][row, col-1] or not layers['*'][row, col-1]):
            # if west != 0:
            #   randnum = random.choice([1, 2, 3, 4, 5])
            #   if(randnum == 1):
            #     self._west(board, the_plot)
            #   elif(randnum == 2):
            #     self._east(board, the_plot)
            #   elif(randnum == 3):
            #     self._north(board, the_plot)
            #   elif(randnum == 4):
            #     self._south(board, the_plot)
            #   else:
            #     self._stay(board, the_plot)
            # else:
            if layers[' '][row-1, col]:
              self._north(board, the_plot)
            # print("fourth")
            # west = 10
          # else:
          #   self._stay(board, the_plot)

          # print(north)
          if north > 0:
            north -= 1
          if east > 0:
            east -= 1
          if south > 0:
            south -= 1
          if west > 0:
            west -= 1


        # randnum = random.choice([1, 2, 3, 4, 5])
        # if(randnum == 1):
        #   self._west(board, the_plot)
        # elif(randnum == 2):
        #   self._east(board, the_plot)
        # elif(randnum == 3):
        #   self._north(board, the_plot)
        # elif(randnum == 4):
        #   self._south(board, the_plot)
        # else:
        #   self._stay(board, the_plot)       
      #  (self._east if self._initialState else self._west)(board, the_plot)
      #  if self.position == things['P'].position: the_plot.terminate_episode()
      else:
        if self.position == things['P'].position: 
          original_stdout = sys.stdout
          with open('out.txt', 'a+') as f:
            sys.stdout = f 
            print("Success!", int(steps/2))
            sys.stdout = original_stdout
          print('Success!')
          the_plot.terminate_episode()
