import generate_fig
import show_figure
import importlib

#delete this 2 lines, they are used to reload the libraries if editing
importlib.reload(generate_fig)
importlib.reload(show_figure)

def generate_rules_name(rules):
    rules_text = "Turn,multiplication = "
    rules_text += ''.join(map(str, rules))
    return rules_text

def rules_str_to_int_duples(rules_string):
    # input_string is a strin like this turnx,multiplicationx turny,multiplicationy Example:2,2 3,2
    # Split the input string into individual rules
    individual_rules = rules_string.split()
    rules = []

    # Iterate over each operation in the list
    for individual_rule in individual_rules:
        turn_str, multiplication_str = individual_rule.split(',')

        turn = int(turn_str)
        multiplication = int(multiplication_str)

        # Append the tuple (turn, multiplication) to the rules list
        rules.append((turn, multiplication))

    return rules


#Variables to draw the new polygon
rules = [(2,2)] #rules are defined as an array of tuples formed like (turn,multiplication)
polygon_sides = 4
show_construction = True
change_colors = False

#inputs to modify the variables to draw the new polygon. If None is entered, then it will use the values of the code
first_input = input("Enter the number of sides of the regular polygon you want to modify ")
if(first_input != ""):
    polygon_sides = int(first_input)
    rules_str = input("Enter the rules of the constructed polygon in pairs turnx,multiplicationx turny,multiplicationy Example:2,2 3,2\n") 
    rules = rules_str_to_int_duples(rules_str)
    show_construction = input("Do you want to see the process of construction of the polygon? y/n ").lower() == 'y'
    if(show_construction):
        change_colors = input("Do you want sides of the polygon to change color when it is being built? y/n ").lower() == 'y'

pts = generate_fig.generate_increased_polygon_fig(polygon_sides,rules) #points of the polygon, the result is an numpy array of arrays of x and y coordinates
fig_show = show_figure.FigureShower(fig_name = str(polygon_sides),rules_name = generate_rules_name(rules))

if(show_construction):
    fig_show.show_figure_construction(pts,change_colors)
else:
    fig_show.show_figure(pts)

