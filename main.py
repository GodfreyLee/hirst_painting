# import colorgram
# colors = colorgram.extract('sample_image.jpg', 30)
# color_list = []
#
# for i in range(30):
#     selected_color = colors[i]
#     rgb = selected_color.rgb # e.g. (255, 151, 210)
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     color_list.append((r, g, b))

import turtle
import random




rgb_color = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]



t = turtle.Turtle()
turtle.colormode(255)



for o in range(-5,5):
    y = o * 40
    for i in range(-10,10):
        x = i * 40
        t.teleport(x,y)
        t.color(random.choice(rgb_color))
        t.dot(20)



screen = turtle.Screen()
t.screen.exitonclick()


