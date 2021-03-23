import numpy as np
import matplotlib.pyplot as plt
from math import pi 
from celluloid import Camera

numberfile = 0

fig = plt.figure(figsize = (10,10))

camera = Camera(fig)

g = 9.81

l = 1.

gamma = 0.5

t = range(0,10000)

dt = 1e-3

print('dt =', dt)

theta_ddot = np.zeros(len(t))
theta_dot  = np.zeros(len(t))
theta      = np.zeros(len(t))
x          = np.zeros(len(t))
y          = np.zeros(len(t))

theta[0] = pi/4.

for ti in range(len(t)-1):

    theta_ddot[ti] = - (g / l) * np.sin(theta[ti]) - 2 * gamma * theta_dot[ti]

    theta_dot[ti+1]  = theta_dot[ti] + dt * theta_ddot[ti]

    #print(theta_dot[ti])

    theta[ti+1]      = theta[ti] + dt * theta_dot[ti]

    #print(theta[ti])

    x[ti]            = -l * np.sin(theta[ti])
    y[ti]            = -l * np.cos(theta[ti])

    plt.scatter(x[ti], y[ti], color = 'red')

    x_values = [0, x[ti]]
    y_values = [0, y[ti]]

    plt.plot(x_values, y_values)

    camera.snap()

  
animation = camera.animate()
animation.save('simple_pendulum.gif')