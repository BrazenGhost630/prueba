def menu():
    try:
        menu=int(input("1. Registrar libro\n2. Listar todos los libros\n3. Registrar venta\n4. Imprimir reporte de ventas\n5. Generar txt\n6. Salir del Programa\n\n"))
        return menu
    except:
        print()
def registrar():
    libros=[]
    generos=["Comedia","Fantasia","filosofia"]
    cant=1
    
    while True:
        try:
            verificar=False
            name=input(f"Titulo del libro {cant}: ")
            if name=="":
                print("Ingrese nuevamente los datos del libro")
                continue
            autor=input(f"Autor del libro {cant}: ")
            if autor=="":
                print("Ingrese nuevamente los datos del libro")
                continue
            genero=input(f"genero del libro {cant}: ")
            if genero=="":
                print("Ingrese nuevamente los datos del libro")
                continue
            for i in generos:
                if i== genero:
                    verificar=True
            if verificar==True:
                verificar=None
            else:
                print("El genero no es valido")
                continue
            
            precio=int(input(f"Precio del libro {cant}: "))


            libros.append(f"Titulo del libro {cant} es {name}")
            libros.append(f"Autor del libro {cant} es {autor}")
            libros.append(f"Genero del libro {cant} es {genero}")
            libros.append(f"Precio del libro {cant} es {precio}")

            
            cant+=1
            bucle=input("Desea registrar mas libro?(y/n)")
            while True:
                if bucle=="n":
                    break
                elif bucle=="y":
                    bucle="y"
                    break
                else:
                    bucle=input("Desea registrar mas libro?(y/n)")
            if bucle=="n":
                print("Se termino el registro")
                return libros
                

            
        except ValueError as error:
            print(f"\nEl dato ingresado no es valido\n")


















#--------------------------------------------------------------------------------------------------------         
def listar(libros):
    for i in libros:
        print(i)
        

    



    














def json(libros):
    imprimir=open("libros.json","w")
    imprimir.write(libros)
    imprimir.close()

verificar=False
while True:
    menu1=menu()
    if menu1==1:
        libros=registrar()
        verificar=True
    elif menu1==2 and verificar==True:
        listar(libros)
    elif menu1==5:
        json(libros)
    

    elif menu1==6:
        break
    else:
        print("\nElija una opcion correcta\n")

