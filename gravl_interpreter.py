#!/usr/bin/env python3
"""
GRAVL Interpreter v0.1
A 2D grid-walking virtual machine.
"""
import sys

GRID = 16

def run(program, show_trace=False):
    cells = [[0]*GRID for _ in range(GRID)]
    x, y = 0, 0
    # Directions: 0=East, 1=South, 2=West, 3=North
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    d = 0
    acc = 0
    ip = 0
    output = []

    jump = {}
    stack = []
    for i, c in enumerate(program):
        if c == '[': stack.append(i)
        elif c == ']':
            j = stack.pop(); jump[i] = j; jump[j] = i

    while ip < len(program):
        cmd = program[ip]
        if cmd == '>': d = (d+1)%4
        elif cmd == '<': d = (d-1)%4
        elif cmd == '^': d = (d+2)%4
        elif cmd == '+': cells[y][x] = (cells[y][x]+1)%256
        elif cmd == '-': cells[y][x] = (cells[y][x]-1)%256
        elif cmd == '*': acc = acc ^ cells[y][x]
        elif cmd == '@':
            dx,dy = dirs[d]; x=(x+dx)%GRID; y=(y+dy)%GRID
        elif cmd == '#':
            n=cells[y][x]; dx,dy=dirs[d]
            x=(x+dx*n)%GRID; y=(y+dy*n)%GRID
        elif cmd == '[':
            if acc==0: ip=jump[ip]
        elif cmd == ']':
            if acc!=0: ip=jump[ip]
        elif cmd == '!': output.append(chr(acc%128))
        elif cmd == '~': acc=cells[y][x]
        elif cmd == '&': cells[y][x]=acc
        ip += 1

    return ''.join(output)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: gravl_interpreter.py <file.gravl>")
        sys.exit(1)
    prog = open(sys.argv[1]).read().strip()
    result = run(prog)
    print(result)
