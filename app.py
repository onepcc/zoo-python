# from animal import Animal
import os

# os.system("ascii_py -t buinzoo.jpg")
# call("pip -V")

from gato import Gato
from perro import Perro
from pinguino import Pinguino
from zoo import Zoo

from colorama import init
init()
from colorama import Fore, Back, Style

# print(Style.BRIGHT+ Fore.RED + 'some red text')
# print(Back.RED + Style.BRIGHT+ Fore.GREEN + 'and with a green background' + Back.RESET)
# print(Style.RESET_ALL)
# print('back to normal now')

# # print(type(snowball.__name__))
# # print(Perro.__name__)
# # print(snowball.__class__.__name__)


# snowball.ruido().ruido().ruido().comer().info()
# bigotes.accidente().vidas().accidente().vidas().comer().info()
# cabo=Pinguino("Cabo",6,"nadar")



print(Style.BRIGHT+ Fore.YELLOW + Back.RED + "*"*90)
print (f"""{"-"*30} Bienvenidos Sims Animals {"-"*30}""")
print("*"*90)

zoovar=input("""Ingrese nombre del Zoo: """)
myzoo= Zoo(zoovar)

while True:
    print(Style.BRIGHT+ Fore.YELLOW + Back.RESET + "")
    zoologicos = []
    perros=[]
    gatos=[]
    pinguinos=[]
    
    

    try:
        opc=int(input(f"""{"-"*30} Ingrese un animal {"-"*30} 
    [1] Perro, 
    [2] Gato, 
    [3] Pinguino ,
    [4] Muestra los animales, 
    [5] Acciones, 
    [6] Salir: """))

        print("*"*90)
        os.system('cls')
        
        #ANÑADIR PERRO
        if opc ==1:
            print(Style.BRIGHT+ Fore.YELLOW + Back.RESET + "")
            print("*"*90)
            
            nperro=input("Ingrese Nombre del perro: ")
            print("*"*90)
            
            eperro=int(input("Ingrese Edad del perro: "))
            print("*"*90)
            
            aperro=input("Ingrese Ladrido del perro: ")
            print("*"*90)
            perro = Perro(nperro,aperro,eperro)
            myzoo.añade_animal(perro)
            os.system('cls')            
        
        #ANÑADIR GATO
        elif opc ==2:
            print(Style.BRIGHT+ Fore.MAGENTA + Back.RESET + "")
            print("*"*90)
            ngato=input("Ingrese Nombre del gato: ")
            print("*"*90)
            
            egato=int(input("Ingrese Edad del gato: "))
            print("*"*90)
            gato = Gato(ngato,egato)
            myzoo.añade_animal(gato)
            os.system('cls')           
        
        #AÑADIR PINGUINO
        elif opc ==3:
                print(Style.BRIGHT+ Fore.BLUE + Back.RESET + "")
                print("*"*90)
                npinguino=input("Ingrese Nombre del Pinguino: ")
                print("*"*90)
                
                epinguino=int(input("Ingrese Edad del Pinguino: "))
                print("*"*90)
                pinguino = Pinguino(npinguino,epinguino)
                myzoo.añade_animal(pinguino)
                os.system('cls')
        
        #MUESTRA TODOS LOS ANIMALES
        elif opc ==4:
            print(Style.BRIGHT+ Fore.RED + Back.YELLOW + "")
            myzoo.print_all_info()
            
        
        #ACCIONES PARA LOS ANIMALES
        elif opc ==5:
                print(Style.BRIGHT+ Fore.RED + "")
                opc2 = int(input(f"""{"-"*30}Seleccione un animal para ver sus acciones:{"-"*30}
        [1] Perro, 
        [2] Gato, 
        [3] Pinguino ,
        [4] Todos comen, 
        [5] Salir: """))
                
                while True:

                    if opc2 == 1:
                        print(Style.BRIGHT+ Fore.YELLOW + Back.RESET + "")
                        try:
                            print(perro)
                        except Exception as e:
                            print("Error: ", e)
                            break
                            
                        opcperro = int(input("""Seleccione:  
        [1] Para Comer, 
        [2] Ruido 
        [3] Salir: """))
                        if opcperro ==1:
                            perro.comer()
                        elif opcperro ==2:
                            perro.ruido()
                        elif opcperro ==3:
                            os.system('cls')
                            break
                        else:
                            continue

                    elif opc2 ==2:
                        print(Style.BRIGHT+ Fore.MAGENTA + Back.RESET + "")
                        try:
                            print(gato)
                        except Exception as e:
                            print("Error: ", e)
                            break
                        
                        opcgato = int(input("""Seleccione: 
        [1] Para Comer, 
        [2] Tener un Accidente 
        [3] Salir: """))
                        if opcgato ==1:
                            gato.comer()
                        elif opcgato ==2:
                            gato.accidente()
                            
                        elif opcgato ==3:
                            os.system('cls')
                            break
                        else:
                            continue
                    
                    elif opc2 ==3:
                        print(Style.BRIGHT+ Fore.BLUE + Back.RESET + "")
                        try:
                            print(pinguino)
                        except Exception as e:
                            print("Error: ", e)
                            break
                        
                        opcpinguino = int(input("""Seleccione: 
        [1] Para Comer, 
        [2] Nadar 
        [3] Salir: """))
                        if opcpinguino ==1:
                            pinguino.comer()
                        elif opcpinguino ==2:
                            pinguino.slide()
                        elif opcpinguino ==3:
                            os.system('cls')
                            break
                        else:
                            print("Opcion invalida")
                            continue
                    
                    # TODOS COMEN
                    elif opc2 ==4:
                        print(Style.BRIGHT+ Fore.GREEN + "")
                        myzoo.todos_comen()
                        
                        break
                    
                    # SALIR
                    elif opc2 == 5:
                        print(Style.BRIGHT+ Fore.RESET + Back.RESET + "")
                        break
                    
                    else:
                        continue
        
        elif opc ==6:
                print(Style.BRIGHT+ Fore.RESET + Back.RESET + "")
                salir = input ("Seguro quieres salir (S/N): ")
                if salir.strip() == "s" or salir == "S":
                    break
                
                elif salir.strip() == "n" or salir =="N":
                    continue


        else:
            print(Style.BRIGHT+ Fore.RESET + Back.RED + "")
            print("*"*80)
            print(f"""{"-"*30} ENTRADA INVALIDA {"-"*30}""")
            print(Style.BRIGHT+ Fore.RESET + Back.RED + "*"*80)
            continue

    except Exception as invalid:
        print("*"*80)
        print("Error", invalid).print(Style.BRIGHT+ Fore.RESET + Back.RED + "")
        print(f"""{"-"*30} ENTRADA INVALIDA {"-"*30}""")
        print(Style.BRIGHT+ Fore.RESET + Back.RED + "*"*80)
        continue
    
    
