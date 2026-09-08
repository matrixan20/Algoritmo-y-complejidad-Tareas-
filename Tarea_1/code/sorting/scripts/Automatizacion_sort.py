import os
import subprocess
import time
import sys

N = [10**1, 10**3, 10**5, 10**7] 
T = ["ascendente", "descendente", "aleatorio"]
D = ["D1", "D7"]
M = ["a", "b", "c"]
algoritmos = ["mergesort", "patiencesort", "quicksort", "sort"]

print("Iniciando algoritmos de ordenamiento...\n")

for n in N:
    for t in T:
        for d in D:
            for m in M:
                nombre_archivo = f"{n}_{t}_{d}_{m}"
                
                ruta_ini = os.path.join("data", "array_input", f"{nombre_archivo}.txt")
                ruta_salida = os.path.join("data", "array_output", f"{nombre_archivo}_out.txt")
                
                for algo in algoritmos:
                    if algo == "mergesort":
                        carpeta = "Time merge"
                    elif algo == "patiencesort":
                        carpeta = "Time patience"
                    elif algo == "quicksort":
                        carpeta = "Time quick"
                    elif algo == "sort":
                        carpeta = "Time sort"
                        
                    ruta_directorio = os.path.join("data", "measurements", carpeta)
                    os.makedirs(ruta_directorio, exist_ok=True)
                    
                    ruta_tiempo = os.path.join(ruta_directorio, f"{nombre_archivo}_{algo}_time.csv")
                    
                    # --- INICIO DEL CRONÓMETRO EN VIVO ---
                    comando = ["./sorting", ruta_ini, ruta_salida, ruta_tiempo, algo]
                    
                    # Lanzamos el proceso en el fondo
                    proceso = subprocess.Popen(comando)
                    tiempo_inicio = time.time()
                    
                    # Mientras el proceso siga corriendo (poll es None)
                    while proceso.poll() is None:
                        tiempo_actual = time.time() - tiempo_inicio
                        # \r borra la línea actual y la reescribe para dar el efecto de reloj en vivo
                        sys.stdout.write(f"\r⏳ Trabajando en {nombre_archivo} con {algo} | Tiempo: {tiempo_actual:.1f}s ")
                        sys.stdout.flush()
                        time.sleep(0.1) # Pausa cortita para no saturar la pantalla
                        if tiempo_actual > 3600:  # Si pasa una hora, salimos del bucle
                            proceso.terminate()  # Terminamos el proceso
                            sys.stdout.write(f"\r❌ Tiempo excedido para {nombre_archivo} con {algo}. Se ha detenido el proceso.\n")
                            ruta_tiempo = os.path.join(ruta_directorio, f"{nombre_archivo}_{algo}_time.csv")
                            with open(ruta_tiempo, 'w') as f:
                                f.write("3600 segundos\n")
                            break
                        
                    # Cuando termina, imprimimos un check final y pasamos a la siguiente línea
                    tiempo_total = time.time() - tiempo_inicio
                    sys.stdout.write(f"\r✅ ¡Listo! {nombre_archivo} con {algo} | Tomó: {tiempo_total:.1f}s       \n")
                    # --------------------------------------

print("\nTodos los archivos han sido procesados.")