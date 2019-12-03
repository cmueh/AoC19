f = open('input.txt')
first_wire = f.readline().split(',')
second_wire = f.readline().split(',')

#testcase #1
#first_wire = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')
#second_wire = "U62,R66,U55,R34,D71,R55,D58,R83".split(',')

#testcase #2
#first_wire = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')
#second_wire = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')


def increment_or_insert(curr_y, curr_x, dict, total_steps):
    if not (curr_y, curr_x) in dict:
        # only memorize the first intersection
        dict[(curr_y, curr_x)] = total_steps


def generate_all_points(dict,wire):


    #start coordinates doesnt matter. Just the difference is important
    curr_x,curr_y = 0,0
    total_steps = 0
    for s in wire:

        direction = s[0]
        steps = int(s[1:])

        if direction== 'R':
            for dx in range(steps):
                curr_x += 1
                total_steps+=1
                increment_or_insert(curr_y, curr_x, dict, total_steps)

        elif direction == 'U':
            for dy in range(steps):
                curr_y -= 1
                total_steps+=1
                increment_or_insert(curr_y, curr_x, dict, total_steps)


        elif direction == 'L':
            for dx in range(steps):
                curr_x -= 1
                total_steps+=1
                increment_or_insert(curr_y, curr_x, dict, total_steps)

        elif direction == 'D':
            for dx in range(steps):
                curr_y += 1
                total_steps+=1
                increment_or_insert(curr_y, curr_x, dict, total_steps)
        else:
            print("WRONG DIRECTION")


dict_1 = {}
dict_2 = {}

generate_all_points(dict_1, first_wire)
generate_all_points(dict_2, second_wire)

intersections = []

for i in dict_1.keys():
    if i in dict_2:
        intersections += [(i, dict_1[i] + dict_2[i])]


intersections = sorted(intersections, key=lambda x: x[1])

print(intersections[0])


