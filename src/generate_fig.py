import numpy as np
import math

def generate_general_increased_fig(original_pts,rules):

    #firstly we made preprocesing to make easier to draw the lines

    num_original_pts = len(original_pts)
    num_new_points = num_original_pts
    patterns = {}
    for turn,multi in rules:
        patterns[turn] = multi
        num_new_points = math.lcm(num_new_points,turn) #its the only way you cant pass it an array :(
        
    #then we calculate the new points

    new_pts = [original_pts[0]]
    last_point = original_pts[0]

    #for all the turns
    for turn in range(1,num_new_points+1):

        #calculate the length of the new line to draw
        line_length = 1
        for pattern_turn in patterns.keys():
            if turn%pattern_turn == 0:
                line_length += patterns[pattern_turn]-1 #thats how it works, if multiple rules overlap

        #we calculate the new point and append a new line 
        actual_point = last_point + (original_pts[turn%num_original_pts] - original_pts[(turn-1)%num_original_pts])*line_length
        last_point = actual_point
        new_pts.append(actual_point)

    new_pts.append(original_pts[0])
    return np.array(new_pts)

def generate_increased_polygon_fig(n_sides,rules):
    #const for drawing a polygon
    radius = 100
    #calculate angle between sides
    angle = 2 * np.pi / n_sides
    coordinates = []
    for i in range(n_sides):
        x = radius * np.cos(i * angle)
        y = radius * np.sin(i * angle)
        coordinates.append([x, y])
        
    coordinates = np.array(coordinates,np.int32)
    pts =  generate_general_increased_fig(coordinates,rules) 
    return pts