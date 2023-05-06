from quad_edge import org, dest


def inCircle(A, B, C, D):
    """
    Calculate the determinant to check if
    point is in circle
    """
    c1 = A.x - D.x
    c2 = B.x - D.x
    c3 = C.x - D.x

    u1 = A.y - D.y
    u2 = B.y - D.y
    u3 = C.y - D.y

    v1 = c1 ** 2 + u1 ** 2
    v2 = c2 ** 2 + u2 ** 2
    v3 = c3 ** 2 + u3 ** 2

    term_1 = (c1 * ((u2 * v3) - (v2 * u3)))
    term_2 = (c2 * ((u1 * v3) - (v1 * u3)))
    term_3 = (c3 * ((u1 * v2) - (v1 * u2)))

    determinant = term_1 - term_2 + term_3

    is_in_circle = True if determinant < 0 else False

    return is_in_circle


def ccw(s1, s2, s3):
    """
    Calculate the determinant to check if
    points are counter clockwise
    """
    det = (s1.x - s2.x) * (s3.y - s2.y) - (s3.x - s2.x) * (s1.y - s2.y)
    is_ccw = True if det < 0 else False

    return is_ccw


def leftOf(X, e):
    """
    Check if point is left of X
    using ccw
    """
    return ccw(X, org(e), dest(e))


def rightOf(X, e):
    """
    Check if point is right of X
    using ccw
    """
    return ccw(X, dest(e), org(e))


def valid(e, basel):
    """
    Verify edge is valid by checking rightOf
    and ccs
    """
    is_right_of = rightOf(dest(e), basel)
    is_ccs = ccw(dest(e), dest(basel), org(basel))

    is_valid = is_right_of and is_ccs
    return is_valid
