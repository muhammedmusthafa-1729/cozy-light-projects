import math 
import random
import matplotlib.pyplot as plt

NEEDLE_LENGTH = 0.8
GAP = 1 
NUM_NEEDLES = 100
GRID_WIDTH = 40
GRID_HEIGHT = 40

LINE_X_POINTS = [] 
for i in range(int(GRID_WIDTH/GAP) + 1): 
    LINE_X_POINTS.append(i * GAP )

x_y = [] 
for i in range(NUM_NEEDLES): 
    x = random.random() * GRID_WIDTH 
    y = random.random() * GRID_HEIGHT 
    x_y.append((x, y)) 


def find_second_point(first_point_tuple: tuple, distance): 
    angle = random.random() * 2 * math.pi 
    x = first_point_tuple[0] + distance * math.cos(angle) 
    y = first_point_tuple[1] + distance * math.sin(angle) 
    return (x, y) 


all_points = [] # list of tuples - each tuple having two tuples as the coordinates of first and second point of the line segment
for first_point in x_y: 
    second_point = find_second_point(first_point_tuple=first_point, distance=NEEDLE_LENGTH) 
    all_points.append((first_point, second_point)) 


def if_segment_touching_lines(line_points: tuple): # Works as long as width is 1
    x1 = line_points[0][0] 
    x2 = line_points[1][0] 
    if math.ceil(x1) == math.ceil(x2): 
        return False 
    else: 
        return True 


line_touching = 0 
line_not_touching = 0 
for line_points in all_points: 
    if if_segment_touching_lines(line_points=line_points): 
        line_touching += 1 
    else: 
        line_not_touching += 1 


print(line_touching, line_not_touching) 
approximate_pi = 2 * (NEEDLE_LENGTH / GAP) * (NUM_NEEDLES / line_touching) 
print("approximate_pi = ", approximate_pi)


def plot_lines(all_points, gap, width):
    
    line_segments = all_points
    for coordinates in line_segments:
        # print(coordinates)
        # Example data: Replace this with your own list of (x, y) coordinate tuples
        # coordinates = ((1, 2), (2, 3))

        # Unpack the tuples using zip
        x_coordinates, y_coordinates = zip(*coordinates)

        # Plotting the points
        plt.plot(x_coordinates, y_coordinates, label='Points', color='black', linewidth=0.5)

    # Adding labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot of Points')
    plt.axis('equal')
    
    for i in range(int(width/gap) + 1): 
        # Plotting a vertical line at x = 5
        plt.axvline(x=i * GAP, color='red', linestyle='-', label=f'x = {i*GAP}', linewidth=0.5)

    # Display the plot
    plt.show()

plot_lines(all_points=all_points, gap=GAP, width=GRID_WIDTH)
