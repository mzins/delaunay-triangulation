"""
Referenced from: https://www.cs.cmu.edu/afs/andrew/scs/cs/15-463/2001/pub/src/a2/cell/edge.hh
"""


class QuadEdge:
    def __init__(self, org=None, dest=None, rot=None, onext=None, left=None, right=None):
        """
        * A directed edge from one vertex to another, adjacent to two faces.
        * Based on Dani Lischinski's code from Graphics Gems IV.
        * Original quad-edge data structure due to Guibas and Stolfi (1985).
        """
        self.org = org
        self.dest = dest
        self.left = left
        self.right = right
        self.rot = rot
        self.onext = onext

    def __str__(self):
        return f"{self.org} - {dest(self)}"


def org(e):
    """
    the vertex of origin for the edge;
    null if currently unknown
    """
    return e.org


def dest(e):
    return org(sym(e))


def rot(e):
    """
    Return the dual of this edge, directed from its left to its right.
    """
    return e.rot


def invrot(e):
    """
    Return the edge from the destination to the origin of this edge.
    """
    return rot(sym(e))


def sym(e):
    """
    Return the next ccw edge around (from) the origin of this edge.
    """
    return rot(rot(e))


def onext(e):
    """
    Return the next cw edge around (from) the origin of this edge.
    """
    return e.onext


def oprev(e):
    """
    Return the next ccw edge around (into) the destination of this edge.
    """
    return rot(onext(rot(e)))


def dnext(e):
    """
     Return the next cw edge around (into) the destination of this edge.
    """
    return sym(onext(sym(e)))


def dprev(e):
    """
    Return the ccw edge around the left face following this edge.
    """
    return invrot(onext(invrot(e)))


def lnext(e):
    """
    Return the ccw edge around the left face before this edge.
    """
    return rot(onext(invrot(e)))


def lprev(e):
    """
    Return the edge around the right face ccw following this edge.
    """
    return sym(onext(e))


def rnext(e):
    """
    Return the edge around the right face ccw before this edge.
    """
    return invrot(onext(rot(e)))


def rprev(e):
    """
    Return the edge around the right face ccw before this edge.
    """
    return onext(sym(e))


def make_edge(a, b):
    e1 = QuadEdge()
    e2 = QuadEdge()
    e3 = QuadEdge()
    e4 = QuadEdge()

    e3.org = b
    e2.rot = e3
    e3.rot = e4
    e4.rot = e1
    e2.onext = e4
    e3.onext = e3
    e4.onext = e2

    e1.org = a
    e1.dest = b
    e1.rot = e2
    e1.onext = e1

    return e1


def splice(a, b):
    temp = a.onext.rot.onext
    a.onext.rot.onext = b.onext.rot.onext
    b.onext.rot.onext = temp
    temp = a.onext
    a.onext = b.onext
    b.onext = temp


def connect(a, b):
    c = make_edge(dest(a), org(b))
    splice(c, lnext(a))
    splice(sym(c), b)
    return c


def delete_edge(e):
    splice(e, oprev(e))
    splice(sym(e), oprev(sym(e)))
    del_a = rot(sym(e))
    del_b = rot(e)
    del_c = sym(e)
    del e, del_a, del_b, del_c
