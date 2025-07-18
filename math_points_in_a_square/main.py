import random
import math
import itertools
import time
import matplotlib.pyplot as plt

def scatter_plot(coordinates):
    # Extract x and y coordinates
    x_coordinates = [round(x, 4) for (x, y) in coordinates]
    y_coordinates = [round(y, 4) for (x, y) in coordinates]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the scatter plot
    ax.scatter(x_coordinates, y_coordinates)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Scatter Plot")
    ax.axis('equal')

    # plot square end lines
    ends = [[(0, 0), (0, HEIGHT)], [(0, WIDTH), (HEIGHT, HEIGHT)], [(WIDTH, WIDTH), (HEIGHT, 0)], [(WIDTH, 0), (0, 0)]]
    for x, y in ends:
        plt.plot(x, y, label='Points', color='red', linewidth=0.5)

    # Start a thread to close the plot after 1 second

    # Show the plot
    plt.show()

t1 = time.time()
def debug():
    import pdb
    pdb.set_trace()

NUM_POINTS = 9
WIDTH = 100
HEIGHT = 100
ACCURACY = 0.0001
NUM_BITS = math.ceil(math.log2(max(HEIGHT, WIDTH)/ACCURACY))
POPULATION_SIZE = 10
TOURNAMENT_SIZE = 2
NUM_ELITES = 1
MUTATION_RATE = 0.05
FRACTION_CHECKED = 0.01
NUM_GENERATIONS = 100000 #int(FRACTION_CHECKED*2**(2*NUM_BITS)*NUM_POINTS/POPULATION_SIZE)
print(NUM_GENERATIONS)

def point(num_bits=NUM_BITS):
    return [random.randint(0, 1) for i in range(2*num_bits)]

def positions_list(num_points=NUM_POINTS):
    positions_list = []
    for i in range(num_points):
        positions_list.extend(point())
    return positions_list

def coordinates_of_positions(positions, num_points=NUM_POINTS, num_bits=NUM_BITS):
    coordinates_list = []
    for i in range(num_points):
        positions = [str(bit) for bit in positions]
        x = WIDTH*int("".join(positions[i*num_bits:(i+1)*num_bits]), 2)/(2**NUM_BITS-1)
        y = HEIGHT*int("".join(positions[(i+1)*num_bits:(i+2)*num_bits]), 2)/(2**NUM_BITS-1)
        coordinates_list.append((x, y))
    return coordinates_list

def min_distance(coordinates_list):
    distances = []
    num_points = len(coordinates_list)
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            distance = ((coordinates_list[i][0] - coordinates_list[j][0])**2 + (coordinates_list[i][1] - coordinates_list[j][1])**2)**0.5
            distances.append(distance)
    for i in coordinates_list:
        distances.append(2*min(i[0], WIDTH-i[0], i[1], HEIGHT-i[1]))
    return min(distances) #numpy.prod(distances)**(1/len(distances))



population = []
for i in range(POPULATION_SIZE):
    population.append(positions_list())


def normalize_population(population: list):
    sorted_pop = []
    for chromosome in population:
        n = NUM_BITS*2
        points_split = [chromosome[i:i+n] for i in range(0, len(chromosome), n)]
        points_split_str = []
        for point_bits in points_split:
            point_bits = [str(j) for j in point_bits]
            points_split_str.append(point_bits)
        points_split = [int("".join(point_bits)) for point_bits in points_split_str]
        points_split.sort()
        points_split = [list(str(point_bits)) for point_bits in points_split]
        for point in points_split:
            for i in range(20 - len(point)):
                point.insert(0, "0")
        chrome = list(itertools.chain.from_iterable(points_split))
        sorted_chromosome = []
        for point in chrome:
            sorted_chromosome.extend(point)
        sorted_pop.append(sorted_chromosome)
    return sorted_pop

for gen in range(NUM_GENERATIONS):
    # population = normalize_population(population)
    weightages = [min_distance(coordinates_list=coordinates_of_positions(positions)) for positions in population]
    # print(weightages)
    if gen%100 == 0:
        print(gen)
        print(round(max(weightages), 4))
    mating_pool = random.choices(population=population, k=POPULATION_SIZE, weights=weightages)

    new_pop = []
    while len(new_pop) < POPULATION_SIZE-NUM_ELITES:
        a1 = random.randint(0, POPULATION_SIZE-1)
        a2 = random.randint(0, POPULATION_SIZE-1)
        str1 = mating_pool[a1]
        str2 = mating_pool[a2]
        pos = random.randint(1, len(str1))
        child1 = str1[:pos] + str2[pos:]
        child2 = str2[:pos] + str1[pos:]
        # child1 = str1[pos:] + str2[:pos]
        # child2 = str2[pos:] + str1[:pos]
        new_pop.append(child1)
        new_pop.append(child2)

    elites = []
    for i in range(NUM_ELITES):
        elites.append(population[weightages.index(max(weightages))])
        weightages.remove(max(weightages))
        population.remove(elites[i])
    new_pop = elites + new_pop

    # print(new_pop, len(new_pop))

    for i in range(NUM_ELITES, POPULATION_SIZE):
        for j in range(NUM_POINTS*NUM_BITS*2):
            n = random.random()
            if n < MUTATION_RATE:
                if new_pop[i][j] == 0:
                    new_pop[i][j] = 1
                else:
                    new_pop[i][j] = 0

    population = new_pop


# for gen in range(NUM_GENERATIONS):
#     # population = normalize_population(population)
#     weightages = [min_distance(coordinates_list=coordinates_of_positions(positions)) for positions in population]
#     # print(weightages)
#     if gen%100 == 0:
#         print(gen)
#         print(round(max(weightages), 4))
#         coordinates = coordinates_of_positions(positions=population[weightages.index(max(weightages))])
#     # mating_pool = random.choices(population=population, k=POPULATION_SIZE, weights=weightages)


#     # Tournament Selection
#     new_pop = []
#     while len(new_pop) < POPULATION_SIZE-NUM_ELITES:
#         tournament_selection_candidate_ids = [random.randint(0, POPULATION_SIZE-1) for k in range(TOURNAMENT_SIZE)]
#         tournament_winner_a = population[weightages.index(max([weightages[tournament_candidate_id] for tournament_candidate_id in tournament_selection_candidate_ids]))]
#         tournament_selection_candidate_ids = [random.randint(0, POPULATION_SIZE-1) for k in range(TOURNAMENT_SIZE)]
#         tournament_winner_b = population[weightages.index(max([weightages[tournament_candidate_id] for tournament_candidate_id in tournament_selection_candidate_ids]))]
#         pos = random.randint(1, len(tournament_winner_a))
#         child1 = tournament_winner_a[:pos] + tournament_winner_b[pos:]
#         child2 = tournament_winner_b[:pos] + tournament_winner_a[pos:]
#         # child1 = str1[pos:] + str2[:pos]
#         # child2 = str2[pos:] + str1[:pos]
#         new_pop.append(child1)
#         new_pop.append(child2)

#     elites = []
#     for i in range(NUM_ELITES):
#         elites.append(population[weightages.index(max(weightages))])
#         weightages.remove(max(weightages))
#         population.remove(elites[i])
#     new_pop = elites + new_pop

#     # print(new_pop, len(new_pop))

#     for i in range(NUM_ELITES, POPULATION_SIZE):
#         for j in range(NUM_POINTS*NUM_BITS*2):
#             n = random.random()
#             if n < MUTATION_RATE:
#                 if new_pop[i][j] == 0:
#                     new_pop[i][j] = 1
#                 else:
#                     new_pop[i][j] = 0

#     population = new_pop

weightages = [min_distance(coordinates_list=coordinates_of_positions(positions)) for positions in population]
print(population[weightages.index(max(weightages))])


t2 = time.time()

print(t2 - t1)

coordinates = coordinates_of_positions(positions=population[weightages.index(max(weightages))])
scatter_plot(coordinates=coordinates)
