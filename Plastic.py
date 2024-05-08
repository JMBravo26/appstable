import os
import time
os.system('cls')
try:
    
    while True:

        opcion_pro = (input('''
        Bienvenido a Plastic 
            
        ¿Que producto va a llevar?     


        1.- Tazón
        2.- Llavero
        3.- Polera estampada
        4.- Salir
        
        Seleccione el producto de su preferencia: '''))
        while not '1'<=opcion_pro<='4':
            os.system('cls')
            print('Dato ingresado no valido.')
            time.sleep(1.5)
            os.system('cls')
            opcion_pro = (input('''\t\t
        Bienvenido a Plastic 
            
        ¿Que producto va a llevar?     


        1.- Tazón
        2.- Llavero
        3.- Polera estampada
        4.- Salir
        
        Seleccione el producto de su preferencia: '''))
    
        socio=(input('\n\t¿Es socio de Plastic? S/N ')).upper()
        if socio=='S':
            if opcion_pro == '1':
                os.system('cls')
                N_producto = 'Tazónes'

                print('''
                      Tazónes
                    
                 Precio no socio   
                                    
                        $500       
                    ''')
            elif opcion_pro == '2':
                os.system('cls')
                N_producto = 'Llaveros'

                print(''' Llaveros
                    
                 Precio no socio  
                                
                        $300            
                    ''')
            elif opcion_pro == '3':
                os.system('cls')
                N_producto = 'Poleras Estampadas'

                print(''' Polera Estampada
                    
                 Precio no socio    
                            
                        $3000          
                    ''')
        if socio=='N':
            if opcion_pro == '1':
                os.system('cls')
                N_producto = 'Tazónes'

                print(''' Tazónes
                    
                   Precio socio    
                                    
                        $800             
                    ''')
            elif opcion_pro == '2':
                os.system('cls')
                N_producto = 'Llaveros'

                print(''' Llaveros
                    
                   Precio socio 
                                
                        $500           
                    ''')
            elif opcion_pro == '3':
                os.system('cls')
                N_producto = 'Poleras Estampadas'

                print(''' Polera Estampada
                    
                   Precio socio    
                                    
                        $5000             
                    ''')
        elif opcion_pro == '4':
            os.system('cls')
            print('Hasta pronto')
            break

        cantidad_pro = int(input('¿Cuantas unidades necesita? '))
        while not 0<cantidad_pro:
            print('Favor de indicar cantidad mayor a uno.')
            os.system('pause')
            cantidad_pro = int(input('¿Cuantas unidades necesita? '))

        if socio=='S':
            p_tazon=500
            p_llavero=300
            p_estam=3000
        
        if socio=='N':

            p_tazon=800
            p_llavero=500
            p_estam=5000    



        total = cantidad_pro

        print('')
        print(F'Exelente {cantidad_pro} de {N_producto} estaran geniales ')
        print('')
        efectivo = str(input('¿Paga en efectivo? S/N ')).upper()
  
        if  efectivo =='S' and socio=='S':
            total = cantidad_pro

            print(F'''
            =======TICKET=======
            Producto: {N_producto}
            Opcion:   
            Precio U: 
            Total:    {total}

                ''')

        if cantidad_pro >= 100 and efectivo == 'S':
            total = total*0.9
            descuento = total*0.1

            print(F'''
            =======TICKET=======
            Producto:  {N_producto}
            Opcion:    
            Precio U:   
            Descuento:  {descuento}
            Total:     {total}

                ''')
        os.system('pause')
except:
    print('dato invalido')