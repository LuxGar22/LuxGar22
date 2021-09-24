def distancia ():
    kilometro = int(input("Cuantos kilometros camino?"))
    if kilometro <= 0 or kilometro <= 10:
        print ("lo puedes hacer mejor")
    elif kilometro >= 40: 
        print ("Animo!!!")
    else:
        print ("sigue caminando")
distancia ()