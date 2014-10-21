#!/usr/bin/python
from os import path

class Color:
  name = "white"
  rgb= 0xffffff

class Swatch:
  color = Color

# Display output modules:
def displayInTerminal():
  return;
# Enough display output modules

extn = '.colors'  # ".color" files define all the colors in a swatch

#An example
fall = open( 'fall' + extn , 'r')


lines = fall.read()


lines_data = filter(None, lines.split('\n'))

for line in lines_data:
  words = line.split(' ')
  rgb = words[0]
  name = words[1]
  print 'rgb= ' + rgb + ' ' + 'name= ' + name
