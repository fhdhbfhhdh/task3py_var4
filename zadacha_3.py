import numpy as np
import matplotlib.pyplot as plt

#задаём функцию при помощи numpy
def f(x1,x2):
    return -(1+np.cos(12*np.sqrt(x1**2+x2**2)))/(0.5*(x1**2+x2**2)+2)

#делаем сетку значений для x1 и x2, затем для них получаем значение функции 
x1 = np.linspace(-2,2,200)
x2 = np.linspace(-2,2,200)
X1, X2 = np.meshgrid(x1,x2)
Y = f(X1,X2)

#создаём тестовую точку с заданными согласно варианту координатами 
x10, x20 = 0, 0
y0 = f(x10,x20)

#создаём окно в которые будут выводиться графики 
fig = plt.figure(figsize=(16, 10))

#график 3х мерной поверхности в изометрическом ввиде 
ax1 = fig.add_subplot(2, 2, 1, projection='3d')#добавляем 3х мерный график 
surf = ax1.plot_surface(X1, X2, Y, cmap='viridis')#строим график поверхности с указанными координатами на ранее добавленном графике
ax1.set_title("Изометрический вид")
ax1.set_xlabel("x1")
ax1.set_ylabel("x2")
ax1.set_zlabel("y=f(x1,x2)")
ax1.scatter(x10, x20, y0, color='r', label='Тестовая точка')#добавляем тестовую точку на график
ax1.legend()

#график 3х мерной поверхности, вид сверху
ax2 = fig.add_subplot(2, 2, 2)
contour = ax2.contourf(X1, X2, Y, cmap='viridis')#создаём вид сверху на 3х мерную плоскость 
ax2.set_title("Вид сверху (x1-x2)")
ax2.set_xlabel("x1")
ax2.set_ylabel("x2")
ax2.plot(x10, x20, 'ro', label='Тестовая точка')#добавляем тестовую точку на график
ax2.legend()

#графика функции y = f(x1) при x2 = x20
ax3 = fig.add_subplot(2, 2, 3)
x1_line = np.linspace(-4, 4, 400)#создаём 1д массив из 400 равномерных точек
y_line1 = f(x1_line, x20)#вычисляем значения функции при разных x1 и фиксированном x2 = x20 = 0
ax3.plot(x1_line, y_line1)
ax3.set_title(f"f(x1, x2=x20)")
ax3.set_xlabel("x1")
ax3.set_ylabel("f")
ax3.plot(x10, y0, 'ro')#добавляем тестовую точку на график

#графика функции y = f(x1) при x2 = x20
ax4 = fig.add_subplot(2, 2, 4)
x2_line = np.linspace(-4, 4, 400)#создаём 1д массив из 400 равномерных точек
y_line2 = f(x10, x2_line)#вычисляем значения функции при разных x2 и фиксированном x1 = x10 = 0
ax4.plot(x2_line, y_line2)
ax4.set_title(f"f(x2, x1={x10})")
ax4.set_xlabel("x2")
ax4.set_ylabel("f")
ax4.plot(x20, y0, 'ro')#добавляем тестовую точку на график

plt.tight_layout()#настраивает размеры подграфиков
plt.show()#отображает все графики на экране
