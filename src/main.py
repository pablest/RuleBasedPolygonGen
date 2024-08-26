import generate_fig
import show_figure
import importlib

importlib.reload(generate_fig)
importlib.reload(show_figure)

def generate_rules_name(rules):
    rules_text = "Turn,multiplication = "
    rules_text += ''.join(map(str, rules))
    return rules_text

rules = [(2,0),(4,5)] #rules are defined as an array of tuples formed like (turn,multiplication)
polygon_sides = 5
show_construction = True
pts = generate_fig.generate_increased_polygon_fig(polygon_sides,rules) #points of the poligon, the result is an numpy array of arrays of x and y coordinates
fig_show = show_figure.FigureShower(fig_name = str(polygon_sides),rules_name = generate_rules_name(rules))

if(show_construction):
    fig_show.show_figure_construction(pts)
else:
    fig_show.show_figure(pts)

