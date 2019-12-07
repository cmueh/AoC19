f = open('input.txt')
in_memory = [int(x.strip()) for x in f.readline().split(',')]


def get_modes(num, expted_params, memory, ip):
    ret = []
    for i in range(expted_params):
        if num % 10 == 0:
            ret += [memory[memory[ip + i]]]
        else:
            ret += [memory[ip+i]]

        num //= 10

    return ret


def sim(ip, memory, inputs):
    output = []
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
            if(len(inputs) == 0):

                ip -= 1
                return ip,output, False

            memory[memory[ip]] = inputs[0]
            del inputs[0]

            ip += 1

        elif opcode == 4:
            # print to output
            output += [memory[memory[ip]]]

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
            return ip,output,True

        else:
            print("INVALID OPERATION", opcode)
            return


res = 0
for amp_a in range(5,10):
    for amp_b in range(5,10):
        for amp_c in range(5,10):
            for amp_d in range(5,10):
                for amp_e in range(5,10):

                    if len(set([amp_a, amp_b, amp_c,amp_d,amp_e])) != 5:
                        continue

                    amp_a_mem = in_memory.copy()
                    amp_b_mem = in_memory.copy()
                    amp_c_mem = in_memory.copy()
                    amp_d_mem = in_memory.copy()
                    amp_e_mem = in_memory.copy()

                    in_a = [amp_a,0]
                    in_b = [amp_b]
                    in_c = [amp_c]
                    in_d = [amp_d]
                    in_e = [amp_e]

                    ip_a = 0
                    ip_b = 0
                    ip_c = 0
                    ip_d = 0
                    ip_e = 0

                    while True:

                        ip_a,_,c = sim(ip_a, amp_a_mem, in_a)
                        in_b += _

                        ip_b,_,c = sim(ip_b, amp_b_mem, in_b)
                        in_c += _

                        ip_c, _, c = sim(ip_c, amp_c_mem, in_c)
                        in_d += _

                        ip_d, _, c = sim(ip_d, amp_d_mem, in_d)
                        in_e += _

                        ip_e, _, c = sim(ip_e, amp_e_mem, in_e)
                        in_a += _

                        if(c):
                            res = max(res,in_a[0])
                            break

print(res)
