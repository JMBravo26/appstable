import os
import time
os.system('cls')
try:
    
    while True:
        menu_Pr=input('''
        ---------MENU--------
        1.Vender pizzas
        2.Estadisticas
        3.salir              
                      
        Seleccione su opcion: ''')
        clientes=0
        C_Napolitanas=0
        C_Vegetariana=0
        C_Española=0
        if menu_Pr=='1':
            clientes+=1
            os.system('cls')

            print(''''
                Bienvenido a Pizzota
                        las mejores pizzas
                
                Tipo Pizza         Mediana	    Familiar
                -----------       ------  	-------
            1.    Napolitana    	$9.000		$12.000
            2.    Vegetariana      	$8.000		$11.000
            3.    Española	        $10.000	        $13.000

            ''')
            seleccion_P = int(input('Seleccione su Pizza ideal: '))
            print('')
            while not 1 <= seleccion_P < 4:
                print('no papito')
                seleccion_P = int(input('Seleccione su Pizza ideal: '))
                
            if seleccion_P == 1:
                C_Napolitanas+=1
                N_pizza = 'Napolitana'
                precio_F = 12000
                precio_M = 9000

            if seleccion_P == 2:
                C_Vegetariana+=1
                N_pizza = 'Vegetariana'
                precio_F = 11000
                precio_M = 8000
            if seleccion_P == 3:
                C_Española+=1
                N_pizza = 'Española'
                precio_F = 13000
                precio_M = 10000

            print(F'Una Pizza {N_pizza} exlente eleccion')
            print('')
            seleccion_t = int(input(f'''Elija el tamaño de su pizza:
            1.Mediana
            2.Familiar
            '''))
            while not 1 <= seleccion_t < 3:
                print('Datos ingresados no validos')
                seleccion_t = int(input(f'''Elija el tamaño de su pizza:
            1.Mediana
            2.Familiar
            '''))
            if seleccion_t == 1:
                N_tamaño = 'Mediana'

            if seleccion_t == 2:
                N_tamaño = 'Familiar'
            print('')

            print(F'''Perfecto, una {N_tamaño}, a la orden ''')

            print('')

            desea_a = str(input('''
            ¿Desea algun agregado?
            1.Si
            2.No
            
            Eleccion: ''')).upper()
            
            while not '1'<=desea_a<='3':
                print('Datos ingresados incorrectos')
                desea_a = str(input('''
            ¿Desea algun agregado?
            1.Si
            2.No
            
            Eleccion: ''')).upper()
            
                    
            if desea_a == '1':
                print('''
                Adicionales	       Precio
                ---------------    ------
            1.   Palos de ajo	   $2.000	
            2.  Aros de cebolla	   $1.200
                    ''')
                seleccion_a = int(input('Seleccione su agregado perfecto: '))
                while not 1 <= seleccion_a < 3:
                    print('Ingrese datos validos')
                    seleccion_a = int(input('Seleccione su agregado perfecto: '))
                pago=int(input('''
                ¿Como paga?
                1.Efectivo
                2.Tarjeta
                
                seleccione su opcion: '''))
                while not 1<=pago<=3:
                    print('Datos no validos')
                    pago=int(input('''
                ¿Como paga?
                1.Efectivo
                2.Tarjeta
                
                seleccione su opcion: '''))
                    
                if pago=='1':
                    total=total*0.8
                elif pago=='2':
                    pago= total

                if seleccion_a == 1:
                    N_agregado = 'Palos de ajo'
                    precio = 2000
                if seleccion_a == 2:
                    N_agregado = 'Aros de cebolla'
                    precio = 1200

                if seleccion_t == 1:
                    total = precio+precio_M
                if seleccion_t == 2:
                    total = precio+precio_F
                print(F'''
                ===========TICKET===========
                Pizza:    {N_pizza} {N_tamaño}
                Agregado: {N_agregado} ${precio}
                Total:    {total}
                ''')
            elif desea_a == '2':
                total = precio_F or precio_M
                print(F'''
                    ===========TICKET===========
                    Pizza:    {N_pizza} {N_tamaño}
                    Agregado: No deseado
                    Total:    {total}
                    ''')

            os.system('pause')
            os.system('cls')
        if menu_Pr=='2':
            print(F'''
            Clientes     {clientes}
            Napolitanas  {C_Napolitanas}
            Vegetarianas {C_Vegetariana}
            Españolas    {C_Española}
                  
                  
                  ''')
        if menu_Pr=='3':
            seguro=input('¿Esta seguro? S/N').upper()
            if seguro=='N':
                menu_Pr='1'
            if seguro=='S':
                print('Hasta pronto')
            break
                    
except:
    print('Datos invalidos.')
