import random

x = [0, 100, 50]
y = [0, 0, 50*3**0.5]

for i in range(1000000):
    anchor = random.randint(0, 2)
    new_x = (x[-1] + x[anchor])/2
    new_y = (y[-1] + y[anchor])/2
    x.append(new_x)
    y.append(new_y)

def scatter_plot():
    import matplotlib.pyplot as plt

    x_coordinates = x
    y_coordinates = y

    plt.scatter(x_coordinates, y_coordinates, s=0.1)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Scatter Plot")
    plt.axis('equal')
    plt.show()

scatter_plot()
