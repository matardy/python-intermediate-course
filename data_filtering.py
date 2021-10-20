from Data import *

def main():

    # Retornar listas
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_worker = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    # Retorna un dictionarie filtrado.
    adults = list(filter(lambda worker: worker['age']>18, DATA))

    # De esta forma solo obtengo los nombres.
    adults = list(map(lambda worker: worker['name'] , adults))
    print(adults)

    # Aqui estoy anadiendo una llave a mi diccionario , es un nuevo diccionario
    old_people = list(map(lambda worker: worker | {"old": worker["age"]>70}, DATA))
    # | = Une a un diccionario con otro nuevo
    # worker es un diccionario. 
    

    # Work by myself 
        # name of all python dev
    all_python_devs_1 = list(filter(lambda worker: worker["language"]=="python" , DATA))
    all_python_devs_1 = list(map(lambda worker: worker["name"] , all_python_devs_1))
    print(all_python_devs_1)
    print(all_python_devs)

        # name of all platzi workers
    all_platzi_workers_1 = list(filter(lambda worker: worker["organization"]=="Platzi" , DATA))
    all_platzi_workers_1 = list(map(lambda worker: worker["name"] , all_platzi_workers_1))
    print(all_platzi_workers_1)
    print(all_platzi_worker)

        # adults people >18 
    adults_1 = [worker["name"] for worker in DATA if worker['age']>18]
    print(adults_1)   
    print(adults) 

        # old people > 70 
    old_people_1 = [worker["name"] for worker in DATA if worker['age']>70]
    print(old_people)
    print(old_people_1)

if __name__ == '__main__':
    main() 