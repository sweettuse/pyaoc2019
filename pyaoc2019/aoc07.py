from itertools import repeat, permutations

from pyaoc2019.interpreter import Instructions, parse_instruction, parse_file, parse_data

__author__ = 'acushner'


def process_amps(instructions: Instructions):
    while instructions.valid:
        inst = parse_instruction(instructions)
        inst.run()
        if inst.opcode.code == 4:
            yield True

    yield instructions


def _input_stream(inp):
    yield inp
    while True:
        yield Instructions._output_register


def feedback(fn_or_data, inputs, as_data=True):
    Instructions._output_register = 0
    f = parse_data if as_data else parse_file
    amps = 'ABCDE'
    amp_map = {}
    inputs = iter(inputs)
    endless_amps = (a for amps in repeat(amps) for a in amps)

    for a in endless_amps:
        try:
            proc = amp_map[a]
        except KeyError:
            proc = amp_map[a] = process_amps(f(fn_or_data, _input_stream(next(inputs))))
        if next(proc) is not True and a == 'E':
            break
    print()
    return Instructions._output_register


def get_best(input_range):
    return max(feedback(7, perm, as_data=False) for perm in permutations(input_range))


def __main():
    feedback('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0', [4, 3, 2, 1, 0])
    feedback('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0', reversed([4, 3, 2, 1, 0]))
    feedback('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5', [9, 8, 7, 6, 5])


if __name__ == '__main__':
    __main()
