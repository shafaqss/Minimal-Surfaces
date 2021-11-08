from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
"""
u = np.linspace(0, 2*np.pi, 32)
v = np.linspace(0, 2*np.pi, 32)
U, V = np.meshgrid(u,v)
a, r = 1.0, 0.25;

X = (a + r*np.cos(U))*np.cos(V)
Y = (a + r*np.cos(U))*np.sin(V)
Z = r*np.sin(U)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');
#plt.axis('off')

plt.show()
"""
u = np.linspace(0, 2*np.pi, 32)
v = np.linspace(-1.2, 1.2, 40)
U, V = np.meshgrid(u,v)
a = 2.

X = a * np.cosh(V)*np.cos(U)
Y = a * np.cosh(V)*np.sin(U)
Z = a*V

fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.set_xlim3d(-1, 1)
#ax.set_ylim3d(-1, 1)
#ax.set_zlim3d(-1, 1)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface catenoid');
#plt.axis('off')


u = np.linspace(-10, 10, 50)
v = np.linspace(-10, 10, 50)
U, V = np.meshgrid(u,v)

X = U - (U**3)/3 + U*(V**2)
Y = V - (V**3)/3 + V*(U**2)
Z = U**2 - V**2

fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.set_xlim3d(-1, 1)
#ax.set_ylim3d(-1, 1)
#ax.set_zlim3d(-1, 1)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface enneper');


u = np.linspace(0, 2*np.pi, 32)
v = np.linspace(-1, 1, 40)
U, V = np.meshgrid(u,v)
a = 2.

X = V *np.cos(U)
Y = V*np.sin(U)
Z = a*U

fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.set_xlim3d(-1, 1)
#ax.set_ylim3d(-1, 1)
#ax.set_zlim3d(-1, 1)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface helicoid');
plt.show()
