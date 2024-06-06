import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definimos los parámetros para las distribuciones
mu_0, mu_1 = 0, 2
sigma = 1

# Rango de valores en el eje x
x = np.linspace(-3, 5, 1000)

# Función para crear las distribuciones
def create_distribution(mu, sigma, x):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Inicializar la figura
fig, ax = plt.subplots()

def animate(n):
    ax.clear()
    sigma_n = sigma / np.sqrt(n)
    
    # Distribuciones H0 y Ha
    y0 = create_distribution(mu_0, sigma_n, x)
    y1 = create_distribution(mu_1, sigma_n, x)
    
    ax.plot(x, y0, label='$H_0$', color='blue')
    ax.plot(x, y1, label='$H_a$', color='red')
    
    # Definición de las áreas de error tipo 1 y tipo 2
    critical_value = mu_0 + 1.96 * sigma_n  # valor crítico para alfa = 0.05
    
    x_fill_1 = np.linspace(critical_value, 5, 1000)
    y_fill_1 = create_distribution(mu_0, sigma_n, x_fill_1)
    ax.fill_between(x_fill_1, y_fill_1, alpha=0.3, color='blue', label='Error Tipo 1 ($\\alpha$)')
    
    x_fill_2 = np.linspace(-3, critical_value, 1000)
    y_fill_2 = create_distribution(mu_1, sigma_n, x_fill_2)
    ax.fill_between(x_fill_2, y_fill_2, alpha=0.3, color='red', label='Error Tipo 2 ($\\beta$)')
    
    ax.axvline(x=critical_value, color='black', linestyle='--', label='Valor crítico')
    
    ax.set_title(f'Tamaño de la muestra (N) = {n}')
    ax.set_ylim(0, 0.6)
    ax.legend()

# Crear la animación
ani = animation.FuncAnimation(fig, animate, frames=np.arange(1, 51), repeat=True)

# Guardar el GIF
gif_path = "/mnt/data/errores_tipo1_tipo2.gif"
ani.save(gif_path, writer='imagemagick')
gif_path
