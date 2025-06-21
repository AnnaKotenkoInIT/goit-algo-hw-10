import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sci

def f(x):
    return x ** 2

a = 0 # Lower limit
b = 2 # Upper limit


def mc_algo(a, b, num_test):
    x = np.random.uniform(a, b, num_test)
    y = np.random.uniform(0, f(b), num_test)

    points_in_area = np.sum(y <= f(x))
    area_ratio = points_in_area / num_test

    total_area = (b - a) * f(b)
    
    return total_area * area_ratio

# Main part of solving
if __name__ == "__main__":
    # Standart method 
    numerical_integral, numerical_error = sci.quad(f, a, b)
    print(f'Числовий інтеграл: {numerical_integral} з помилкою {numerical_error} ')

    # Testing
    num_tests = [10, 100, 1000, 10000, 100000]
    for num_test in num_tests:
        mc_result = mc_algo(a, b, num_test)
        print(f"Monte Carlo інтеграл ({num_test} точок): {mc_result}")

# Building the graph
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


