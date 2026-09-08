import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. RUTA MAGICA: Detecta automáticamente la carpeta 'sorting' sin importar desde dónde se ejecute
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

N = [10**1, 10**3, 10**5, 10**7] 
T = ["ascendente", "descendente", "aleatorio"]
D = ["D1", "D7"]
M = ["a", "b", "c"]
algoritmos = ["mergesort", "patiencesort", "quicksort", "sort"]

print("Recolectando datos de los CSV de ordenamiento...\n")
datos = []

for n in N:
    for t in T:
        for d in D:
            for m in M:
                nombre_archivo = f"{n}_{t}_{d}_{m}"
                for algo in algoritmos:
                    if algo == "mergesort":
                        carpeta = "Time merge"
                    elif algo == "patiencesort":
                        carpeta = "Time patience"
                    elif algo == "quicksort":
                        carpeta = "Time quick"
                    elif algo == "sort":
                        carpeta = "Time sort"
                    
                    # 2. Aplicamos la ruta absoluta a prueba de balas
                    ruta_tiempo = os.path.join(BASE_DIR, "data", "measurements", carpeta, f"{nombre_archivo}_{algo}_time.csv")
                    
                    try:
                        with open(ruta_tiempo, 'r') as file:
                            linea = file.readline().strip()
                            
                            # Validamos si está el timeout de nuestro script
                            if "3600" in linea:
                                tiempo_num = 3600000000.0 # Tope visual en microsegundos
                            else:
                                # Leemos el número que dejó C++
                                tiempo_num = float(linea.split()[0])
                                
                                # EL CAPEO DE SEGURIDAD (Si el archivo pasó la hora)
                                if tiempo_num > 3600000000.0:
                                    tiempo_num = 3600000000.0
                            
                            datos.append({
                                'N': n,
                                'Tipo': t,
                                'Dominio': d,
                                'Muestra': m,
                                'Algoritmo': algo.capitalize(),
                                'Tiempo_us': tiempo_num
                            })
                    except FileNotFoundError:
                        pass # Ignora si falta un CSV y sigue buscando

print("Generando DataFrame...")
df = pd.DataFrame(datos)

# Seguro de vida por si las rutas fallaran (que ya no lo harán)
if df.empty:
    print("¡Alerta! No se encontraron datos. Verifica que los CSV existan en data/measurements/")
    exit()

# 3. Aplicamos la ruta absoluta a la carpeta de salida
ruta_plots = os.path.join(BASE_DIR, "data", "plots")
os.makedirs(ruta_plots, exist_ok=True)

print("Generando gráficas de Sorting...")

# ==============================================================================
# GRÁFICO 1: Tiempo vs N (Solo para arreglos Aleatorios y dominio D7)
# ==============================================================================
df_aleatorio = df[(df['Tipo'] == 'aleatorio') & (df['Dominio'] == 'D7')]
promedios_aleatorio = df_aleatorio.groupby(['N', 'Algoritmo'])['Tiempo_us'].mean().unstack()

plt.figure(figsize=(10, 6))
promedios_aleatorio.plot(kind='line', marker='o', ax=plt.gca(), linewidth=2, markersize=8)

plt.title('Crecimiento del Tiempo vs Tamaño del Arreglo (Tipo: Aleatorio)', fontsize=14)
plt.xlabel('Tamaño del Arreglo (N)', fontsize=12)
plt.ylabel('Tiempo Promedio (Microsegundos)', fontsize=12)
plt.xscale('log', base=10) # Base 10 porque tus N son potencias de 10
plt.yscale('log')
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend(title='Algoritmo')

ruta_img1 = os.path.join(ruta_plots, "sorting_tiempo_vs_n.png")
plt.savefig(ruta_img1, bbox_inches='tight')
plt.clf()

# ==============================================================================
# GRÁFICO 2: Comparación por Distribución (Para el tamaño más grande N=10^7)
# ==============================================================================
df_grande = df[(df['N'] == 10**7) & (df['Dominio'] == 'D7')]

if not df_grande.empty:
    promedios_tipo = df_grande.groupby(['Tipo', 'Algoritmo'])['Tiempo_us'].mean().unstack()

    plt.figure(figsize=(10, 6))
    promedios_tipo.plot(kind='bar', ax=plt.gca(), edgecolor='black')

    plt.title('Rendimiento según Distribución Inicial (N = 10^7)', fontsize=14)
    plt.xlabel('Distribución Inicial del Arreglo', fontsize=12)
    plt.ylabel('Tiempo Promedio (Microsegundos)', fontsize=12)
    plt.xticks(rotation=0)
    plt.yscale('log') 
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Movemos la leyenda afuera para que no tape las barras
    plt.legend(title='Algoritmo', bbox_to_anchor=(1.05, 1), loc='upper left')

    ruta_img2 = os.path.join(ruta_plots, "sorting_comparacion_tipos.png")
    plt.savefig(ruta_img2, bbox_inches='tight') # Evita que se corte la imagen guardada

print(f"¡Gráficos generados con éxito en la carpeta: {ruta_plots}!")