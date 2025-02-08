import random
shapes = ["🔼", "🔳", "⚪️", "🧢"]
# shapes = ["triangle", "square", "circle", "hat"]
shapes_count = {i: 0 for i in shapes}
total_counts = [9, 8, 7, 1]
shapes_max_count = dict(zip(shapes, total_counts))

for i in range(25):
    shape = random.choices(population=shapes, weights=total_counts, k=1)[0]
    shapes_count[shape] += 1
    if shapes_count[shape] == shapes_max_count[shape]:
        del total_counts[shapes.index(shape)]
        shapes.remove(shape)
    else:
        total_counts[shapes.index(shape)] -= 1
    if i%5 != 4:
        print(shape, end=" ")
    else:
        print(shape)