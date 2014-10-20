#!/usr/bin/python
from os import path

class Color:
  name = "white"
  rgb= 0xffffff 

class Swatch:
  color = Color



extn = '.colors'  # ".color" files define all the colors in a swatch

#An example
fall = open( 'fall' + extn , 'r')
print( fall.read() ) 




