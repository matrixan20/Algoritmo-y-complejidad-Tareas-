import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Mismos ciclos que en tu automatizador de matrices
Ns = [2**4, 2**6, 2**8, 2**10]
Ts = ["dispersa", "diagonal", "densa"]
Ds = ["D0", "D10"]
Ms = ["a", "b", "c"]
algoritmos = ["strassen", "naive"]

datos = []
print("Recolectando datos de los CSV de matrices...")

for n in Ns:
    for t in Ts:
        for d in Ds:
            for m in Ms:
                nombre_archivo = f"{n}_{t}_{d}_{m}"
                
                for algo in algoritmos:
                    carpeta = f"Time {algo}"
                    ruta_tiempo = os.path.join("data", "measurements", carpeta, f"{nombre_archivo}_{algo}_time.csv")
                    
                    try:
                        with open(ruta_tiempo, 'r') as file:
                            linea = file.readline().strip()
                            if "3600" in linea:
                                tiempo_num = 3600000000.0
                            else:
                                tiempo_num = float(linea.split()[0])
                            
                            datos.append({
                                'N': n,
                                'Tipo': t,
                                'Dominio': d,
                                'Muestra': m,
                                'Algoritmo': algo.capitalize(),
                                'Tiempo_us': tiempo_num
                            })
                    except FileNotFoundError:
                        pass

print("Generando DataFrame y gráficas...")
df = pd.DataFrame(datos)

ruta_plots = os.path.join("data", "plots")
os.makedirs(ruta_plots, exist_ok=True)

df_densa = df[(df['Tipo'] == 'densa') & (df['Dominio'] == 'D10')]
promedios_densa = df_densa.groupby(['N', 'Algoritmo'])['Tiempo_us'].mean().unstack()

plt.figure(figsize=(10, 6))
promedios_densa.plot(kind='line', marker='o', ax=plt.gca(), linewidth=2, markersize=8)

plt.title('Crecimiento del Tiempo vs Tamaño de Matriz (Tipo: Densa)', fontsize=14)
plt.xlabel('Dimensión de la Matriz (N)', fontsize=12)
plt.ylabel('Tiempo Promedio (Microsegundos)', fontsize=12)
plt.xscale('log', base=2) # Escala en base 2 porque tu N son potencias de 2
plt.yscale('log')
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend(title='Algoritmo')

ruta_img1 = os.path.join(ruta_plots, "matriz_tiempo_vs_n.png")
plt.savefig(ruta_img1, bbox_inches='tight')
plt.clf()

df_grande = df[(df['N'] == 1024) & (df['Dominio'] == 'D10')]
promedios_tipo = df_grande.groupby(['Tipo', 'Algoritmo'])['Tiempo_us'].mean().unstack()

plt.figure(figsize=(10, 6))
promedios_tipo.plot(kind='bar', ax=plt.gca(), color=['#ff9999', '#66b3ff'], edgecolor='black')

plt.title('Rendimiento según Distribución (N = 1024)', fontsize=14)
plt.xlabel('Tipo de Matriz', fontsize=12)
plt.ylabel('Tiempo Promedio (Microsegundos)', fontsize=12)
plt.xticks(rotation=0)
plt.yscale('log')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Algoritmo')

ruta_img2 = os.path.join(ruta_plots, "matriz_comparacion_tipos.png")
plt.savefig(ruta_img2, bbox_inches='tight')

print(f"¡Gráficos generados con éxito en la carpeta: {ruta_plots}!")