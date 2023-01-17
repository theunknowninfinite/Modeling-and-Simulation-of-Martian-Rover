from sympy import *
from sympy import pprint as pp
def H(alpha, t, d, a):
    A = Matrix([[cos(t), -sin(t)*cos(alpha), sin(t)*sin(alpha), a*cos(t)],
                   [sin(t), cos(t)*cos(alpha), -cos(t)*sin(alpha), a*sin(t)],
                   [0, sin(alpha), cos(alpha), d],
                   [0, 0, 0, 1]])
    return A
t1 = Symbol("theta_1")
t2 = Symbol("theta_2")
d3 = Symbol("d_3")
t4 = Symbol("theta_4")

A1 = H(-90*(pi/180), t1, 0.222, 0)

A2 = H(90*(pi/180), t2, 0, 0.6553)

A3 = H(0, 0, d3, 0)

A4 = H(0, t4, 0, 0)

# t5 = Symbol("theta5")
# A5 = H(90*(pi/180), t5, 0.3840, 0)

# t6 = Symbol("theta6")
# A6 = H(-90*(pi/180), t6, 0, 0.0880)

# t7 = Symbol("theta7")
# A7 = H(0, t7, -0.1070, 0)

print('T\u2081=\n')
pp(A1)
print('\n')

print('T\u2082=\n')
pp(A2)
print('\n')

print('T\u2083=\n')
pp(A3)
print('\n')

print('T\u2084=\n')
pp(A4)
print('\n')

# print('T\u2085=\n')
# pp(A5)
# print('\n')

# print('T\u2086=\n')
# pp(A6)
# print('\n')

# print('T\u2087=\n')
# pp(A7)

print('T=\n')
pp(A1*A2*A3*A4)
