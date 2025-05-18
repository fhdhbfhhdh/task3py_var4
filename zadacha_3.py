import numpy as np
import matplotlib.pyplot as plt

def f(x1,x2):
    return -(1+np.cos(12*np.sqrt(x1**2+x2**2)))/(0.5*(x1**2+x2**2)+2)

x1 = np.linspace(-2,2,200)
x2 = np.linspace(-2,2,200)
X1, X2 = np.meshgrid(x1,x2)
Y = f(X1,X2)

x10, x20 = 0, 0
y0 = f(x10,x20)

fig = plt.figure(figsize=(15, 10))

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
surf = ax1.plot_surface(X1, X2, Y, cmap='viridis')
ax1.set_title("Изометрический вид")
ax1.set_xlabel("x1")
ax1.set_ylabel("x2")
ax1.set_zlabel("y=f(x1,x2)")
ax1.scatter(x10, x20, y0, color='r', label='Тестовая точка')
ax1.legend()

ax2 = fig.add_subplot(2, 2, 2)
contour = ax2.contourf(X1, X2, Y, cmap='viridis')
ax2.set_title("Вид сверху (x1-x2)")
ax2.set_xlabel("x1")
ax2.set_ylabel("x2")
ax2.plot(x10, x20, 'ro', label='Тестовая точка')
fig.colorbar(contour, ax=ax2)
ax2.legend()

ax3 = fig.add_subplot(2, 2, 3)
x1_line = np.linspace(-2, 2, 400)
y_line1 = f(x1_line, x20)
ax3.plot(x1_line, y_line1)
ax3.set_title(f"f(x1, x2={x20})")
ax3.set_xlabel("x1")
ax3.set_ylabel("f")
ax3.plot(x10, y0, 'ro')

ax4 = fig.add_subplot(2, 2, 4)
x2_line = np.linspace(-2, 2, 400)
y_line2 = f(x10, x2_line)
ax4.plot(x2_line, y_line2)
ax4.set_title(f"f(x2, x1={x10})")
ax4.set_xlabel("x2")
ax4.set_ylabel("f")
ax4.plot(x20, y0, 'ro')

plt.tight_layout()
plt.show()
