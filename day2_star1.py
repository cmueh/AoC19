f = open('input.txt')
in_memory = [int(x.strip()) for x in f.readline().split(',')]

in_memory[1] = 12
in_memory[2] = 2


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


simulate(in_memory)
[print(str(x) , end=",") for x in in_memory]
