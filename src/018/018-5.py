# See end of file for information
import colorgram as clr

colors_count = 30
colors = clr.extract('src\/018\/image.jpg', colors_count)
rgb_color_list = [(245, 243, 239), (247, 242, 245), (204, 165, 107), (239, 246, 241), (237, 240, 245), (155, 73, 46), (174, 154, 37), (51, 93, 124), (224, 201, 133), (139, 31, 20), (132, 163, 185), (201, 90, 69), (46, 123, 86), (13, 100, 73), (70, 48, 39), (99, 72, 74), (147, 179, 146), (235, 175, 164), (163, 141, 158), (55, 46, 50), (184, 206, 171), (18, 85, 90), (147, 18, 22), (41, 61, 74), (80, 146, 128), (187, 83, 87), (41, 66, 88), (108, 126, 151), (15, 72, 69), (175, 192, 213)]

def return_color(first_color):
  """returns a random color (RGB)

  Returns:
      tuple: an RGB color
  """
  rgb = first_color.rgb # e.g. (255, 151, 210)
  color_list = []
  red = rgb[0]
  red = rgb.r
  color_list.append(red)
  green = rgb[1]
  green = rgb.g
  color_list.append(green)
  blue = rgb[2]
  blue = rgb.b
  color_list.append(blue)
  new_color = tuple(color_list)
  return new_color

def main():
  global colors_count
  hirst_list = []
  for extracted_color in range(colors_count):
    first_color = colors[extracted_color]
    hirst_list.append(return_color(first_color))
  print(hirst_list)

main()
##===========================================================================================
## Date: .............. 2022-10-23
## Program: ........... 018-5.py
## Website: ........... weburl
## Description: ....... extracts colors from a picture
## Installs to: ....... src/018
## Compatibility: ..... Python3+
## Contact Author: .... github.com/lundeen-bryan
## Copyright © ........ company 2022. All rights reserved.
##
## Notes:
##
##
##===========================================================================================
