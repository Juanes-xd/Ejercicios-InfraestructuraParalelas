from threading import Thread
import time
import numpy as np

vector = range(1,31) # 30 elementos [1, 2, 3, 4, ..., 30]
#MAX_UNITS = 1 # 1 hilo
#MAX_UNITS = 2 # Hilos
#MAX_UNITS = len(vector)//4 # Hilos
#MAX_UNITS = len(vector)//2 # Hilos
MAX_UNITS = len(vector) # Hilos
valores_x_worker =  len(vector) // MAX_UNITS

def tareas_x_worker(low_limit = 0, high_limit = len(vector)):
  for i in range(np.int32(low_limit), np.int32(high_limit)):
    print(f"sleep de {i} es {vector[i]}")
    time.sleep(1)  # Pausa de 1 segundo

workers = []

#     1         2           3           4
# [0,...,8] [9,...,17] [18,...,26] [27,...35]

count = 0
for worker in range(0,MAX_UNITS):
  worker = Thread(target = tareas_x_worker,
                  args = (count, count + valores_x_worker))
  workers.append(worker)
  count += valores_x_worker

start = time.time()
for worker in workers:
  worker.start()

for worker in workers:
  worker.join()

end = time.time()

print(f"Tiempo transcurrido hilos {end - start}")