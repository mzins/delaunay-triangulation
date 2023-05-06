import random

from point import Point
from quad_edge import make_edge, splice, delete_edge, connect, org, dest, sym, onext, lnext, oprev, rprev, rnext

from algebra import leftOf, rightOf, inCircle, ccw, valid
from visuals.plot_delaunay import plot


def delaunay(S):
    S.sort(key=lambda x: x.x)

    if len(S) == 2:
        # Let s1 and s2 be the two sites, in sorted order.
        # Create an edge a from s2 to s2

        s1 = S[0]
        s2 = S[1]

        a = make_edge(s1, s2)

        a.org = s1
        a.dest = s2

        return [a, sym(a)]

    if len(S) == 3:
        # Let s1, s2, s3 be the three sites, in sorted order.
        # Create edge a connecting s1 to s2 and b connecting s2 to s3

        s1 = S[0]
        s2 = S[1]
        s3 = S[2]

        a = make_edge(s1, s2)
        b = make_edge(s2, s3)

        splice(sym(a), b)

        # Now close the triangle:
        if ccw(s1, s2, s3):
            c = connect(b, a)
            return [a, sym(b)]

        elif ccw(s1, s3, s2):
            c = connect(b, a)
            return [sym(c), c]

        else:
            return [a, sym(b)]
    else:
        # len(S) >= 4. Let L and R be the left and right values of S
        L = S[:len(S)//2]
        R = S[len(S)//2:]

        ldo, ldi = delaunay(L)
        rdi, rdo = delaunay(R)

        # Compute lower common tangent of both meshes
        while True:
            if leftOf(org(rdi), ldi):
                ldi = lnext(ldi)
            elif rightOf(org(ldi), rdi):
                rdi = rprev(rdi)
            else:
                break

        # Create a first cross edge base1 from rdi.Org to ldi.Org
        basel = connect(sym(rdi), ldi)

        if org(ldi) == org(ldo):
            ldo = sym(basel)
        if org(rdi) == org(rdo):
            rdo = basel

        # This is the merge loop
        # Locate the first L point (lcand.Dest) to be encountered by the rising bubble,
        # and delete L edges out of basel. Dest that fail the circle test.
        while True:
            lcand = onext(sym(basel))
            if valid(lcand, basel):
                while inCircle(dest(basel), org(basel), dest(lcand), dest(onext(lcand))):
                    t = onext(lcand)
                    delete_edge(lcand)
                    lcand = t
            rcand = oprev(basel)
            if valid(rcand, basel):
                while inCircle(dest(basel), org(basel), dest(rcand), dest(oprev(rcand))):
                    t = oprev(rcand)
                    delete_edge(rcand)
                    rcand = t
            # If both lcand and rcand are invalid, then basel is the upper common tangent
            if not valid(lcand, basel) and not valid(rcand, basel):
                break

            if not valid(lcand, basel) or (valid(rcand, basel) and inCircle(dest(lcand), org(lcand), org(rcand), dest(rcand))):
                basel = connect(rcand, sym(basel))
            else:
                basel = connect(sym(basel), sym(lcand))
        return [ldo, rdo]


if __name__ == "__main__":
    input_list = [[random.randint(0, 20), random.randint(0, 20)]
                  for _ in range(0, 20)]

    points = [Point(x[0], x[1]) for x in input_list]
    results = delaunay(points)

    print(results)
