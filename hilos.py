import threading
import time
import datetime
import logging


i=0

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')


def hilo1(idaaa):
	logging.info("Consultado para el id" + str(idaaa))
	global i
	while i<5:
		print("Este es el primer hilo",i)
		i= i+1
		time.sleep(2)
	
	

def hilo2(ida):
	logging.info("Consultado para el id" + str(ida))
	j=0

	while j<5:
		print("Este es el segundo hilo",j)
		j= j+1
		time.sleep(2)
	#print ("este es el segundo hilo")


tiempo_ini = datetime.datetime.now()

t1 = threading.Thread(name="hilo_1", target =hilo1, args=(1, ) )
t2 = threading.Thread(name="hilo_2", target =hilo2, args=(1, ) )

t1.start()
t2.start()
t2.join()
t1.join()

print ("Termino los hilos y llego al hilo principal")


tiempo_fin = datetime.datetime.now()

print("Tiempo transcurrido", str(tiempo_fin - tiempo_ini))