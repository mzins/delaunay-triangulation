import csv
import random
import time

import matplotlib.pyplot as plt

from delaunay import delaunay
from point import Point

times = []
sizes = [100, 500, 1000, 5000, 10000, 50000,
         100000, 300000, 500000, 800000, 1000000]
for size in sizes:
    print(size)
    input_list = [[random.randint(0, 20), random.randint(0, 20)]
                  for _ in range(0, size)]

    points = [Point(x[0], x[1]) for x in input_list]

    t0 = time.time()
    result = delaunay(points)
    t1 = time.time()

    times.append(t1 - t0)


plt.plot(sizes, times, linestyle='-', marker='o')
plt.savefig("performance-results/plot.png")

with open("performance-results/data.csv", "w") as f:
    f.write("input_size, time\n")

    for i in range(0, len(sizes)):
        f.write(f"{sizes[i]}, {times[i]}\n")
