f = open('input.txt')
in_memory = [int(x.strip()) for x in f.readline().split(',')]


def simulate(memory):
    ip = 0  # instruction pointer
    while ip < len(memory):

        op_code = memory[ip]
        param_a = memory[memory[ip + 1]]
        param_b = memory[memory[ip + 2]]
        param_c = memory[ip + 3]

        if op_code == 1:
            memory[param_c] = param_a + param_b
            ip += 4

        elif op_code == 2:
            memory[param_c] = param_a * param_b
            ip += 4

        elif op_code == 99:
            # halt reached
            break;
        else:
            # as stated in the task statement... this should not happen
            print("SOMETHING WENT WRONG!")


# quick look at the input file reveals that its not big, 150 integers.
# so a trivial solution by just running the whole simulation is feasible for
# each of the [0..99] x [0..99] possibilities
for noun in range(100):
    for verb in range(100):

        curr_memory = in_memory.copy()
        curr_memory[1] = noun
        curr_memory[2] = verb

        simulate(curr_memory)

        if curr_memory[0] == 19690720:
            print(str(100 * noun + verb))




