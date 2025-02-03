from z3 import *

desired = [ 0x41, 0x29, 0xd9, 0x65, 0xa1, 0xf1, 0xe1, 0xc9, 0x19, 0x09, 0x93, 0x13, 0xa1, 0x09, 0xb9, 0x49, 0xb9, 0x89, 0xdd, 0x61, 0x31, 0x69, 0xa1, 0xf1, 0x71, 0x21, 0x9d, 0xd5, 0x3d, 0x15, 0xd5, 0x00 ]

inp = []

zolv = Solver()
for i in range(len(desired)):
    b = BitVec(desired[i], 16)
    inp.append(b)

for i in (range(len(inp))):
    b = inp[i]

    x = ((b >> 1) & 0x55) | ((b & 0x55) * 2)
    y = ((x >> 2) & 0x33) | ((x & 0x33) << 2)
    z = (y >> 4) | (y << 4)

    z = ~z
    z = z & 0xff

    zolv.add(z == desired[i])

if zolv.check() == sat:
    print("Constraints can be satisfied!")
    sol = zolv.model()
    flag = ""
    for i in range(len(sol)):
        flag += (chr(int(str(sol[inp[i]]))))
    print(flag[::-1])
