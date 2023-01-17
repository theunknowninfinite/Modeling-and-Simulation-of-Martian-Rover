from sympy import * 
import matplotlib.pyplot as plt
from sympy import pprint as pp
import numpy as np


def H(alpha, t, d, a):                         # Function definition for Transformation matrices 

    A = Matrix([[cos(t), -sin(t)*cos(alpha), sin(t)*sin(alpha), a*cos(t)],
                [sin(t), cos(t)*cos(alpha), -cos(t)*sin(alpha), a*sin(t)],
                [0, sin(alpha), cos(alpha), d],
                [0, 0, 0, 1]])
    return A

t1_i = Symbol('theta1')                         # Initializing theta1 as a symbol
t2_i = Symbol('theta2')                         # Initializing theta2 as a symbol
q3_i = Symbol('q3')                             # Joint 3 is locked, theta3 = 0
t4_i = Symbol('theta4')                         # Initializing theta4 as a symbol

A1 = H(-90*(pi/180), t1_i, 0.222, 0)

A2 = H(90*(pi/180), t2_i, 0, 0.6553)

A3 = H(0, 0, q3_i, 0)

A4 = H(0, t4_i, 0, 0)

T1 = A1                                         # Homogeneous Transformation matrix (0-1)
T2 = T1*A2                                      # Homogeneous Transformation matrix (0-2)
T3 = T2*A3                                      # Homogeneous Transformation matrix (0-4)
T4 = T3*A4

Z1 = Matrix([[T1[2]], [T1[6]], [T1[10]]])       # Z1 matrix from T1
Z2 = Matrix([[T2[2]], [T2[6]], [T2[10]]])       # Z2 matrix from T2
Z3 = Matrix([0, 0, 0])                          # Z3 matrix from T3
Z4 = Matrix([[T4[2]], [T4[6]], [T4[10]]])
XP = Matrix([[T3[3]], [T3[7]], [T3[11]]])

Xp1 = diff(XP, t1_i)                            # The postion matrix from T6 differentiated by theta1
Xp2 = diff(XP, t2_i)                            # The postion matrix from T6 differentiated by theta2
Xp3 = diff(XP, q3_i)
Xp4 = diff(XP, t4_i)                            # The postion matrix from T6 differentiated by theta4

J1 = Matrix([[Xp1], [Z1]])                      # Jacobian matrix for T1
J2 = Matrix([[Xp2], [Z2]])                      # Jacobian matrix for T2
J3 = Matrix([[Xp3], [Z3]])                      # Jacobian matrix for T3
J4 = Matrix([[Xp4], [Z4]])
J = Matrix([[J1, J2, J3, J4]])                  # Final 6 x 6 Jacobian matrix
# pprint(J)

t1 = 0                                          # Initial values for theta1
t2 = 0                                          # Initial values for theta2
q3 = 1
t4 = 0                                          # Initial values for theta4
pp(T4)

Three_D_plot = plt.figure(figsize=(4,4))
circle = Three_D_plot.add_subplot(111, projection='3d')

x = []                                          # List for storing X-component of the Xp matrix (T6_F[3])
y = []                                          # List for storing Y-component of the Xp matrix (T6_F[7])
z = []                                          # List for storing Z-component of the Xp matrix (T6_F[11])

for t in np.linspace(90, 450, num=50):
    Vx = 0                                      # Derivative of x = 67.9 w.r.t time
    Vy = -0.1*2*(pi/5)*sin(t*(pi/180))          # Derivative of y = rcosθ w.r.t time
    Vz = 0.1*2*(pi/5)*cos(t*(pi/180))           # Derivative of x = rsinθ w.r.t time
    Wx = 0                                      # Angular velocities of the end effector (x)
    Wy = 0                                      # Angular velocities of the end effector (y)
    Wz = 0                                      # Angular velocities of the end effector (z)

    X_dot = Matrix([[Vx], [Vy], [Vz], [Wx], [Wy], [Wz]])    # Velocity matrix (6 x 1)
    J_f = J.subs({t1_i : t1, t2_i : t2, q3_i : q3, t4_i : t4})      # Subtituting the theta values in the final jacobian matrix J
    J_1 = J_f.pinv()                                                                                # Jacobian inverse 
    T4_F = T4.subs({t1_i : t1, t2_i : t2, q3_i : q3, t4_i : t4})    # Subtituting the theta values in the transformation matrix T6
    # pp(T4_F)
    x.append(T4_F[3])                           # Appending X-component to the list                   
    y.append(T4_F[7])                           # Appending Y-component to the list
    z.append(T4_F[11])                          # Appending Z-component to the list
    circle.scatter(T4_F[3], T4_F[7],T4_F[11])   # Scatter plotting the x,y,z values
    plt.xlim(0, 1)                              # X -axis limits
    plt.ylim(0.05, -0.05)                       # Y -axis limits
    plt.pause(0.5)
    circle.set_xlabel('X-axis')
    circle.set_ylabel('Y-axis')
    circle.set_zlabel('Z-axis')
    circle.set_title('Circular Trajectory of the end effector', fontsize = 14, fontweight ='bold')

    Q_dot = J_1*X_dot                           # Finding Q_dot
    t1_dot = Q_dot[0]                           # First element of the Q_dot matrix
    t2_dot = Q_dot[1]                           # Second element of the Q_dot matrix
    q3_dot = Q_dot[2]                           # Third element of the Q_dot matrix    
    t4_dot = Q_dot[3]                           # Fourth element of the Q_dot matrix

    T = 5                                       # Total Time
    N = 50                                      # Number of data points
    dt = T/N
    t1 = t1 + (t1_dot*dt)                       # Numerical integration for q1(theta1)
    t2 = t2 + (t2_dot*dt)                       # Numerical integration for q2(theta2)
    q3 = q3 + (q3_dot*dt)                       # Numerical integration for q4(theta4)    
    t4 = t4 + (t4_dot*dt)                       # Numerical integration for q5(theta5)
    
    t1 = t1.evalf()                             # Simplifying the value of q1
    t2 = t2.evalf()                             # Simplifying the value of q2                             
    q3 = q3.evalf()                             # Simplifying the value of q4
    t4 = t4.evalf()

plt.show()
