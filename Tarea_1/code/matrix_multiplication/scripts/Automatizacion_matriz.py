import os
import subprocess
import time
import sys

Ns = [2**4, 2**6, 2**8, 2**10]
Ts = ["dispersa", "diagonal", "densa"]
Ds = ["D0", "D10"]
Ms = ["a", "b", "c"]

for n in Ns:
    for t in Ts:
        for d in Ds:
            for m in Ms:
                nombre_archivo = f"{n}_{t}_{d}_{m}"
                
                ruta_ini1 = os.path.join("data", "matrix_input", f"{nombre_archivo}_1.txt")
                ruta_ini2 = os.path.join("data", "matrix_input", f"{nombre_archivo}_2.txt")
                ruta_salida = os.path.join("data", "matrix_output", f"{nombre_archivo}_out.txt")
                tamaño = n
                for algo in ["strassen", "naive"]:
                    if algo == "strassen":
                        carpeta = "Time strassen"
                    elif algo == "naive":
                        carpeta = "Time naive"
                        
                    ruta_directorio = os.path.join("data", "measurements", carpeta)
                    os.makedirs(ruta_directorio, exist_ok=True)
                    
                    ruta_tiempo = os.path.join(ruta_directorio, f"{nombre_archivo}_{algo}_time.csv")

                    # Parte pedida a la IA para poder mostrar el tiempo en vivo mientras se ejecuta el proceso
                    # --- INICIO DEL CRONÓMETRO EN VIVO ---
                    comando = ["./matrix_multiplication", ruta_ini1, ruta_ini2, ruta_salida, ruta_tiempo, algo, str(n)]
                    
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
                        if tiempo_actual > 3600:
                            proceso.terminate()
                            sys.stdout.write(f"\r❌ Tiempo excedido para {nombre_archivo} con {algo}. Se ha detenido el proceso.\n")
                            ruta_tiempo = os.path.join(ruta_directorio, f"{nombre_archivo}_{algo}_time.csv")
                            with open(ruta_tiempo, 'w') as f:
                                f.write("3600 segundos\n")
                            break
                    # Cuando termina, imprimimos un check final y pasamos a la siguiente línea
                    if proceso.poll() is not None:
                        sys.stdout.write(f"\r✅ Completado {nombre_archivo} con {algo} | Tiempo final: {tiempo_actual:.1f}s\n")

print("\nTodos los archivos han sido procesados.")