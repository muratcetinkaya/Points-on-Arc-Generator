import math

def get_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def get_points_on_arc(p1, p2, p3, mm_between_points):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    ma = (y2-y1)/(x2-x1)
    mb = (y3-y2)/(x3-x2)
    x = (ma*mb*(y1-y3) + mb*(x1+x2) - ma*(x2+x3))/(2*(mb-ma))
    y = (-1/ma)*(x-(x1+x2)/2) + (y1+y2)/2
    center = (x, y)

    radius = math.sqrt((x1-x)**2 + (y1-y)**2)

    start_angle = math.atan2(y1-y, x1-x)
    end_angle = math.atan2(y2-y, x2-x)
    if start_angle > end_angle:
        end_angle += 2*3.14
    arc_length = radius * (end_angle - start_angle)

    num_points = int(arc_length / mm_between_points)

    step = (end_angle-start_angle)/(num_points-1)

    points = []
    for i in range(num_points):
        angle = start_angle + i*step
        x = center[0] + radius*math.cos(angle)
        y = center[1] + radius*math.sin(angle)
        points.append((x, y))

    return points


p1 = (606.556, 586)
p2 = (415.328, 613.002)
p3 = (223.341, 575.003)
mm_between_points = 30
points_on_arc = get_points_on_arc(p1, p3, p2, mm_between_points)

print(points_on_arc)