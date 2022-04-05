from turtle import *


def draw_branch(branch_length, angle, trunk_thickness):
    if branch_length > 5:
        width(trunk_thickness)
        forward(branch_length)
        right(angle)
        draw_branch(branch_length - 15, angle, trunk_thickness - 1)
        left(2 * angle)
        draw_branch(branch_length - 15, angle, trunk_thickness - 1)
        right(angle)
        backward(branch_length)


def draw_tree(trunk_length, angle, trunk_thickness):
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle, trunk_thickness)
    done()


draw_tree(100, 30, 7)

