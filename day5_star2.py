f = open('input.txt')
in_memory = [int(x.strip()) for x in f.readline().split(',')]


def get_modes(num, exptedParams, memory, ip):
    ret = []
    for i in range(exptedParams):
        if num % 10 == 0:
            ret += [memory[memory[ip + i]]]
        else:
            ret += [memory[ip+i]]

        num //= 10

    return ret


def simulate(memory, inputs):
    ip = 0  # instruction pointer
    in_ptr = 0 # position in the input stream

    while ip < len(memory):
        val = memory[ip]
        opcode = val % 100
        val //= 100

        ip += 1

        if opcode == 1:
            # addition
            params = get_modes(val,2,memory, ip)
            memory[memory[ip + 2]]= params[0] + params[1]
            ip += 3

        elif opcode == 2:
            # multiplication
            params = get_modes(val, 2, memory, ip)
            memory[memory[ip + 2]] = params[0] * params[1]
            ip += 3

        elif opcode == 3:
            # read from input stream
            memory[memory[ip]] = inputs[in_ptr]
            in_ptr += 1
            ip += 1

        elif opcode == 4:
            # print to output
            print("output " + str(memory[memory[ip]]))
            ip += 1

        elif opcode == 5:
            # jump if true
            param = get_modes(val,2,memory, ip)
            if param[0] != 0:
                ip = param[1]
            else:
                ip += 2

        elif opcode == 6:
            # jump if false
            param = get_modes(val, 2, memory, ip)
            if param[0] == 0:
                ip = param[1]
            else:
                ip += 2

        elif opcode == 7:
            # less than
            param = get_modes(val, 3, memory, ip)

            if param[0] < param[1]:
                memory[memory[ip+2]] = 1
            else:
                memory[memory[ip+2]] = 0

            ip += 3

        elif opcode == 8:
            # equals
            param = get_modes(val, 2, memory, ip)

            if param[0] == param[1]:
                memory[memory[ip+2]] = 1
            else:
                memory[memory[ip+2]] = 0

            ip += 3

        elif opcode == 99:
            return
        else:
            print("INVALID OPERATION", opcode)

simulate(in_memory, [5])
