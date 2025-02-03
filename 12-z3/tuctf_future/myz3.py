from z3 import *
inp = []
for i in range(25):
	inp.append(BitVec(str(i), 8))


# genMatrix()
# print(mat)
mat = [[0 for x in range(5)] for y in range(5)]
print(mat)

for i in range(25):
	m = (i * 2) % 25
	f = (i * 7) % 25
	mat[m//5][m%5] = inp[f]

# genAuthString()
auth = [0] * 19
auth[0] = mat[0][0] + mat[4][4];
auth[1] = mat[2][1] + mat[0][2];
auth[2] = mat[4][2] + mat[4][1];
auth[3] = mat[1][3] + mat[3][1];
auth[4] = mat[3][4] + mat[1][2];
auth[5] = mat[1][0] + mat[2][3];
auth[6] = mat[2][4] + mat[2][0];
auth[7] = mat[3][3] + mat[3][2] + mat[0][3];
auth[8] = mat[0][4] + mat[4][0] + mat[0][1];
auth[9] = mat[3][3] + mat[2][0];
auth[10] = mat[4][0] + mat[1][2];
auth[11] = mat[0][4] + mat[4][1];
auth[12] = mat[0][3] + mat[0][2];
auth[13] = mat[3][0] + mat[2][0];
auth[14] = mat[1][4] + mat[1][2];
auth[15] = mat[4][3] + mat[2][3];
auth[16] = mat[2][2] + mat[0][2];
auth[17] = mat[1][1] + mat[4][1];

s = Solver()
desired = [0x8b, 0xce, 0xb0, 0x89, 0x7b, 0xb0, 0xb0, 0xee, 0xbf, 0x92, 0x65, 0x9d, 0x9a, 0x99, 0x99, 0x94, 0xad, 0xe4]

for i in range(len(desired)):
	s.add(auth[i] == desired[i])

for i, c in enumerate("TUCTF{"):
	s.add(ord(c) == inp[i])
s.add(inp[24] == 125)

print(s.check())
if s.check() == sat:
	sol = s.model()
	flag = ''
	for i in inp:
		flag += chr(int(str(sol[i])))
	print(flag)
