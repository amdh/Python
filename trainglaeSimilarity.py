from math import sqrt


def areTrianglesSimilar(coordinates):
    # get sides fo traingles
    # find the angles between sides
    #  verify that angles match
    #   if match reutrn true else false

    dist1 = getDist(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
    dist2 = getDist(coordinates[0], coordinates[1], coordinates[4], coordinates[5])
    dist3 = getDist(coordinates[4], coordinates[5], coordinates[2], coordinates[3])

    dist4 = getDist(coordinates[6], coordinates[7], coordinates[8], coordinates[9])
    dist5 = getDist(coordinates[6], coordinates[7], coordinates[10], coordinates[11])
    dist6 = getDist(coordinates[8], coordinates[9], coordinates[10], coordinates[11])

    if dist1 == dist4:
        if dist2 == dist5:
            if dist3 == dist6:
                return "true"

    else:
        return "false"


def getDist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)