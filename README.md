# AI-Final-Project

This repository contains the related codes of Group 34's final project for Artificial Intelligence course taught by Prof. Jane Hsu (NTU, Spring 2020).

Before running the code, pycolab and curses have to first be installed into your python. It can be easily done with the pip command. Recommendation: run it in Ubuntu

The code takes 3 additional arguments: level [determine the map and how many pedestrians], the way pedestrians move, the algorithm used

For the first arguments, the valid inputs are: 0-5.
For the second arguments, the valid inputs are: 0-2, and for the third arguments, the valid inputs are: 0-1 
[More details can be seen in the final report slides]

Example to run the code: "python main.py 5 1 1" 

To run the code multiple times, run the shellscript. However, to adjust how many times you want to run the code and what arguments you want to run, you would have to change the script by yourself (line 6 and 9).

To exit the program while it is still simulating, press "q".

Everytime the program finishes a simulation, it will write its output into a text file "out.txt" in the format:

FAILURE! => if player fails to reach the destination without violating the rule

Success! "x" => if player successfully reaches the destination within the constaints, where x = number of steps taken. 
