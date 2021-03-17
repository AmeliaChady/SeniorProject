from collections import namedtuple

Coordinates = namedtuple('Coordinates', ['x', 'y'])
Line = namedtuple('Line', ['a', 'b', 'x_start', 'x_end'])
Error = namedtuple('Error', ['error', 'line'])
C = 0


def find_line_meeting(line1, line2):
    pass


def least_squares(coordinate_list):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_xsq = 0
    n = len(coordinate_list)

    for i in range(n):
        coord = coordinate_list[i]
        sum_x += coord.x
        sum_y += coord.y
        sum_xy += coord.x * coord.y
        sum_xsq += coord.x ** 2

    try:
        a = (n * sum_xy - sum_x * sum_y)/(n * sum_xsq - sum_x ** 2)
    except ZeroDivisionError:
        return None
    b = (sum_y - a * sum_x)/n
    return Line(a, b, coordinate_list[0].x, coordinate_list[-1].x)


def least_squares_error(coordinate_list):
    line = least_squares(coordinate_list)
    if line is None:
        return None
    if len(coordinate_list) < 2:
        return None
    error = 0
    for i in range(len(coordinate_list)):
        coord = coordinate_list[i]
        error += (coord.y - line.a * coord.x - line.b)**2
    return Error(error, line)

depth = 0
def find_minimized_error(error_list, minimum_x):
    global depth
    err_len = len(error_list)
    if err_len < 2:
        return None
    depth += 1
    #print(len(error_list[0]), err_len)
    er = error_list[0][err_len-2]
    if er is None:
        return None
    minimum_error = er.error
    minimum_error_list = [er.line]
    end_y = er.line.x_end
    j = len(error_list)-1
    for i in range(err_len):
        try:
            if not(j-i-1 < 0):
                error_tuple = error_list[i][j-i-1]
            else:
                error_tuple = None
        except IndexError:
            error_tuple = None

        if error_tuple is not None:
            error_tuple_minimized = None
            if not i-1 < 0:
                error_tuple_minimized = find_minimized_error(error_list[:i-1], minimum_x)
            if error_tuple_minimized is not None:
                if error_tuple_minimized[0] != -1:
                    error = error_tuple.error + C + error_tuple_minimized[0]
                    if (error < minimum_error or minimum_error == -1) \
                            and error_tuple_minimized[1][0].x_start == minimum_x\
                            and (error_tuple_minimized[1][-1].x_end == end_y
                                or error_tuple.line.x_end == end_y):
                        #print("tick", error)
                        minimum_error_list = error_tuple_minimized[1]
                        minimum_error_list.append(error_tuple.line)
                        minimum_error = error
                else:
                    error = error_tuple.error + C
                    if (error < minimum_error or minimum_error == -1) \
                            and error_tuple.line.x_start == minimum_x\
                            and error_tuple.line.x_end == end_y:
                        #print("tick", error)
                        minimum_error_list = [error_tuple.line]
                        minimum_error = error

    return minimum_error, minimum_error_list


'''
Takes in a set of points and returns a set of points marking the ends of each line segment in the solutions
'''
def segmented_least_squares(coordinate_list):
    length = len(coordinate_list)

    minimum_x = coordinate_list[0].x
    # getting errors
    error_list = []
    for i in range(length):
        inner_error_list = []
        for j in range(i+1, length):
            inner_error_list.append(least_squares_error(coordinate_list[i:j]))
        error_list.append(inner_error_list)

    # getting subsets
    found = find_minimized_error(error_list, minimum_x)[1]
    line_coords = []
    if len(found) > 0:
        line = found[0]
        line_coords.append(Coordinates(line.x_start, line.a*line.x_start + line.b))
        for i in range(1, len(found)):
            iline = found[i]
            line_coords.append(Coordinates(iline.x_start, iline.a*iline.x_start + iline.b))
            line_coords.append(Coordinates(iline.x_end, iline.a*iline.x_end + iline.b))
        line = found[-1]
        line_coords.append(Coordinates(line.x_end, line.a*line.x_end + line.b))
    return line_coords

    '''line = least_squares(coordinate_list)
    start_coords = Coordinates(coordinate_list[0].x, line.a * coordinate_list[0].x + line.b)
    end_coords = Coordinates(coordinate_list[-1].x, line.a * coordinate_list[-1].x + line.b)
    return [start_coords, end_coords]'''



