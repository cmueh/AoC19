f = open('input.txt')
first_wire = f.readline().split(',')
second_wire = f.readline().split(',')


def increment_or_insert(curr_y, curr_x, dict):
    if (curr_y, curr_x) in dict:
        dict[(curr_y, curr_x)] += 1
    else:
        dict[(curr_y, curr_x)] = 1


def generate_all_points(dict,wire):

    #start coordinates doesnt matter. Just the difference is important
    curr_x,curr_y = 0,0

    for s in wire:

        direction = s[0]
        steps = int(s[1:])

        if direction== 'R':
            for dx in range(steps):
                curr_x += 1
                increment_or_insert(curr_y, curr_x, dict)

        elif direction == 'U':
            for dy in range(steps):
                curr_y -= 1
                increment_or_insert(curr_y, curr_x, dict)


        elif direction == 'L':
            for dx in range(steps):
                curr_x -= 1
                increment_or_insert(curr_y, curr_x, dict)

        elif direction == 'D':
            for dx in range(steps):
                curr_y += 1
                increment_or_insert(curr_y, curr_x, dict)
        else:
            print("WRONG DIRECTION")


def manhattan_dist(t):
    return abs(t[0]) + abs(t[1])


dict_1 = {}
dict_2 = {}

generate_all_points(dict_1, first_wire)
generate_all_points(dict_2, second_wire)

intersections = []

for i in dict_1.keys():
    if i in dict_2:
        intersections += [i]

intersections = sorted(intersections, key=lambda x: manhattan_dist(x))

print(abs(manhattan_dist(intersections[0])))