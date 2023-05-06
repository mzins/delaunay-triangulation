
# L. Guibas and J. Stolfi's Divide-and-Conquer Algorithm

This project is a Python implemetation of L. Guibas and J. Stolfi's Divide and Conquer Algorithm for Delaunay Triangulation using the Quad Edge data structure.

Submitted for my graduate Computational Geometry course final project.
## Run Locally

Clone the project

```bash
  git clone git@github.com:mzins/delaunay-triangulation.git
```

Go to the project directory

```bash
  cd delaunay-triangulation
```

Calculate Delaunay Triangulation using a randomly generated set of points

```bash
  python delaunay.py
```

Call the delaunay function 

```python
from point import Point

input_list = <your list of x,y coords here>
points = [Point(x[0], x[1]) for x in input_list]

delaunay(points)
```

Run algorithm performance metrics 

```bash
  python plot_performance.py
```

## Lessons Learned

Implmenting the quad edge data structure is a gigantic pain and someone with more time should really standardize it for Python users :)

I need a better way to capture a list of edges of the triangulation in the data structure so that plotting the results are easier. 

## Acknowledgements

 - [Primitives for the Manipulation of General Subdivisions and the Computation of Voronoi Diagrams](https://dl.acm.org/doi/pdf/10.1145/282918.282923) 

 - [Quad Edge Data Structure](https://www.cs.cmu.edu/afs/andrew/scs/cs/15-463/2001/pub/src/a2/quadedge.html)

