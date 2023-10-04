import psutil
import time

def mostrar():
    procesos = psutil.process_iter()

    print("Lista de los procesos en ejecucion:")
    for proceso in procesos:
        print(f"Id de del proceso: {proceso.pid}, nombre del proceso: {proceso}\n")

def finalizar(pid):
    try:
        proceso = psutil.Process(pid)
        proceso.terminate()
        print("El proceso se finalizo corretamente")
    except psutil.NoSuchProcess:
        print("El proceso no existe")

def ram():
    mram = psutil.virtual_memory()
    tram = mram.total/(1024**3)
    uram = mram.used/(1024**3)
    print(f"El total de memoria ram es de {tram}GB y se estan utilizando: {uram}GB")

def procesador():
    procesador = psutil.cpu_percent(interval=1)
    print(f"Porcentaje de uso del procesador {procesador}%")

def discoDuro():
    infodisco = psutil.disk_usage('/')
    totaldisco = infodisco.total/(1024**3)
    usodisco = infodisco.used/(1024**3)
    libredisco = infodisco.free/(1024**3)

    return f"El tamaño total del disco duro es de {totaldisco}GB y se estan utilizando{usodisco}GB. \n Memoria disponible: {libredisco}" 
    
if __name__ == "_main_":
    mostrar()

    try:
        pid_fin = int(input("ingresa el id del proceso que quieras finalizar"))
        finalizar(pid_fin)
    except ValueError:
        print("id de proceso invalido")

    while True:
      print(discoDuro())
      procesador()
      ram()
      time.sleep(60)