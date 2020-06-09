print('-' * 20)
titulo = 'Capítulo {}'
print(titulo.format('4').upper())
print('')
#cancion = 'Te,encontrare,una,mañana,dentro,de,mi,habitación,y,preparas,la,cama,para,dos'
#print (cancion)
#print('Con reemplazo:', cancion.replace(',',' '))
#nombre = input('Ingrese su nombre completo: ')
#direccion = input('Ingrese su dirección: ')
#dato = nombre + '; ' + direccion
#print('Nombre y dirección: ', dato)
#print(len(dato))
#print(dato.upper())
#print(dato.find('Albus'))
print('-' * 20)
print(titulo.format('5').upper())
print('')
#kilometro = int(input('Ingrese una distancia a convertir de kilómetros a millas: '))
#milla = kilometro / 0.6214
#print(kilometro , 'km equivalen a' , milla , 'mi')
print('-' * 20)
print(titulo.format('6').upper())
print('')
#numero = int(input('Ingrese un numero: '))
#if numero > 0:
#    print('El número es positivo')
#elif numero < 0:
#    print('El número es negativo')
#else:
#    print('El número es 0')
#if numero == 0:
#    print('El número es 0')
#else:
#    parimpar = ('El número es par' if numero % 2 == 0 else 'El númmero es impar')
#    print (parimpar)
#kilometro = input('Ingrese una distancia a convertir de kilómetros a millas: ')
#if kilometro.isnumeric():
#    if float(kilometro) < 0 :
#        kilometro = input('Por favor ingrese una distancia valida: ')
#else:
#    kilometro = input('Por favor ingrese una distancia valida: ')
#    if float(kilometro) < 0 :
#        kilometro = input('Por favor ingrese una distancia valida: ')
#milla = float(kilometro) / 0.6214
#print(kilometro , 'km equivalen a' , milla , 'mi')
print('-' * 20)
print(titulo.format('7').upper())
print('')
#factorial = 1
#numero1 = None
#numero1 = input('Ingrese el número que desee obtener su factorial: ')
#if numero1.isnumeric():
#    if int(numero1) == 0:
#        print('El factorial de ', numero1, ' es: ', factorial)
#    elif int(numero1) > 0:
#        for i in range (1, int(numero1) + 1):
#            factorial = factorial * i
#        print('El factorial de ', numero1, ' es: ', factorial)
#else:
#    print('Ingrese un valor valido')

#print('')
#print('Bienvenido a: "Los Números Primos"')
#print('')
#seguir = 's'
#while  seguir == 'Si' or seguir == 'si' or seguir == 'S' or seguir == 's':
#    valor = None
#    valor = input('Los números primos hasta el: ')
#    print('')
#    if valor.isnumeric() and int(valor) > 0: 
#        ctrl_primo = True
#        print ('1  ', end='')
#        for i in range (2, int(valor)+1):
#            for j in range (2, i+1):
#                if j != i and ctrl_primo == True:
#                    if i % j != 0:
#                        ctrl_primo = True
#                    else:
#                        ctrl_primo = False
#                else:
#                    if j == i and ctrl_primo == True:
#                        print (i, ' ', end='')
#                    else:
#                        ctrl_primo = True
#                        break
#    else:
#        print('Por favor ingrese un valor valido')
#    print()
#    print('')
#    seguir = input('¿Desea probar con un nuevo valor? (Si / No): ')
#    print('')
print('-' * 20)
print(titulo.format('8').upper())
print('')
# Otro archivo NumberGuessingGame
print('-' * 20)
print(titulo.format('9').upper())
print('')
#seguir = 's'
#while seguir == 'Si' or seguir == 'si' or seguir == 'S' or seguir == 's':
#    valor = None
#    valor = input('Ingrese un número a saber si es primo: ')
#    print('')
#    if valor.isnumeric() and int(valor) > 0:
#        n = int(valor)-1
#        def es_primo (n):
#            if n == 1:
#                return True
#            elif int(valor) % n != 0:
#                res = True * es_primo(n-1)
#                return res
#            else:
#                res = False * es_primo(n-1)
#                return res
#        print('¿ Es primo el número', valor,'?:', bool(es_primo(n)))
#        print('')
#    else:
#        print('Por favor ingrese un valor valido')
#        print('')
#    seguir = input('¿ Desea probar con un nuevo valor ? (Si / No): ')
#    print('')

#print('SOLO RECURSIVE N° PRIMO')
#valor = input('Ingrese un número a saber si es primo: ')
#n = int(valor)-1
#def es_primo (n):
#    if n == 0 or n == 1:
#        return True
#    elif int(valor) % n != 0:
#        res = True * es_primo(n-1)
#        return res
#    else:
#        res = False * es_primo(n-1)
#        return res
#print('¿Es primo el número', valor, '?:', bool(es_primo(n)))

#print('EJEMPLO RECURSIVE')
#print('')
#def factorial(n):
#    if n == 1:
#        return 1
#    else:
#        res = n * factorial(n-1)
#        return res
#print('')
#numero = input('Ingrese un número entero: ')
#print('')
#print(factorial(int(numero)))
print('-' * 20)
print(titulo.format('11').upper())
print('')

#def pedir_valor(mensaje, valor_string):
#    """
#    Esta función evalua si el valor ingresado es un número mayor a 0 y menor a 11.
#    En caso de que no lo sea devuelve un mensaje de error."""#
#
#    while not (valor_string.isnumeric() and int(valor_string) > 0 and int(valor_string) < 10):
#        print('')
#        print('El valor ingresado no es valido')
#        valor_string = input(mensaje)
#    return  int(valor_string)
#
#def mensaje_fin_juego(valor_propuesto, numero_adivinar, n_intento):
#    """
#    Esta función devuelve el mensaje final del juego, ya sea si ganó o perdió."""
#    if int(valor_propuesto) == numero_adivinar:
#        print('')
#        print('Felicitaciones ha adivinado el número correctamente, cuyo valor era:', numero_adivinar)
#        print('Logró adivinarlo en', n_intento, 'intento/s')
#    else:
#        print('')
#        print('Lo siento, no ha adivinado el número correctamente. Su valor era:', numero_adivinar)
#        print('')
#        print('GAME OVER')
#
#def main_juego(seguir):
#    """
#    Se ejecuta el juego en su totalidad."""
#    import random
#    while seguir == 'S' or seguir == 's' or seguir == 'Si' or seguir == 'si':
#        numero_a_adivinar = random.randint(1,10)
#        intento = 1
#        valor = input('Por favor adivine el número entre 1 y 10: ')
#        valor = pedir_valor('Por favor ingrese un número válido entre 1 y 10: ', valor)
#        while int(valor) != numero_a_adivinar:
#            print('')
#            print('Lo siento, número equivocado')
#            if intento == 4:
#                break
#            elif int(valor) < numero_a_adivinar:
#                print('')
#                print('El número que propuso es menor al que desea adivinar')
#            else:
#                print('')
#                print('El número que propuso es mayor al que desea adivinar')
#            intento += 1
#            print('')
#            print('Tiene', 5 - intento, 'intentos restatnes')
#            print('')
#            valor = input('Proponga un nuevo número: ')
#            valor = pedir_valor('Por favor ingrese un número  valido entre 1 y 10: ', valor)
#        mensaje_fin_juego(valor, numero_a_adivinar, intento)
#        print('')
#        seguir = input('¿Desea jugar nuevamente? (Si / No): ')
#    print('')
#
#print('')
#print ('Bienvenido al "Number Guessing Game"')
#print('')
#sigue = 's'
#main_juego(sigue)
#print('GAME OVER')
print('-' * 20)
print(titulo.format('13').upper())
print('')
# Otro archivo Calculator
print('-' * 20)
print(titulo.format('15').upper())
print('')

#def es_primo(n):
#    """
#   FUNCIÓN RECURRENTE - 
#    La función requiere usar la variable 'num'
#    en el código global.
#    """
#    global num
#    n = int(n)
#    if n == 1 or n == 2:
#        return True
#    elif int(num) % (n-1) != 0:
#        res = True * es_primo(n-1)
#        return bool(res)
#    else:
#        res = False * es_primo(n-1)
#        return bool(res)
#
#def square_root(n):
#    return int(n) ** 0.5
#
#def high_order_function(i, func):
#    return func(i)
#
#num = input('Ingresar: ')
#print('')
#print(high_order_function(num, es_primo))
#print('')
#print(high_order_function(num, square_root))
print('-' * 20)
print(titulo.format('16').upper())
print('')

#def convert(a, b):
#    return a * b#
#
#def curry(func, num):
#    return lambda rate: func(num, rate)
#
#pesoARG_a_dolar = curry(convert, 1/75)
#dolar_a_pesoARG = curry(convert, 65)
#
#pesoARG_a_euro = curry(convert, 1/76.25)
#euro_a_pesoARG = curry(convert, 72.25)
#
#print(pesoARG_a_euro(80000))
#print(dolar_a_pesoARG(3000))
print('-' * 20)
print(titulo.format('18').upper())
print('')

#class Account:
#    def __init__(self, acc_number, acc_name, acc_balance, acc_type):
#        self.acc_number = acc_number
#        self.acc_name = acc_name
#        self.acc_balance = acc_balance
#        self.acc_type = acc_type

#    def __str__(self):
#        return 'Account[' + str(self.acc_number) + '] - ' + self.acc_name + ', ' + self.acc_type + ' account = ' + str(self.acc_balance)

#    def deposit(self, depo_amount):
#        self.acc_balance += depo_amount

#    def withdraw(self, with_amount):
#        if with_amount > self.acc_balance:
#            return print('The amount you want to withdraw is larger than your actual balance:', self.acc_balance)
#        else:
#            self.acc_balance -= with_amount

#    def get_balance(self):
#        return self.acc_balance

#acc1 = Account('123', 'Pedro', 50.00, 'investment')
#acc2 = Account('124', 'Victoria', 75.00, 'current')

#print(acc1)
#print(acc2)
#acc1.deposit(10.00)
#acc2.withdraw(50.00)
#print(acc2)
#acc2.withdraw(50.00)
#print('Balance:', acc1.get_balance())
print('-' * 20)
print(titulo.format('19').upper())
print('')

#Creo la calse Account, le agrego los atributos acc_number (justo este va a depender de las cuentas que se vayan 
# haciendo con instance_count), acc_name, acc_balance y acc_type
class Account:
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    def __init__(self, acc_number, acc_name, acc_balance, acc_type):
        Account.increment_instance_count()
        print('New Account created')
        self.acc_number = Account.instance_count
        self.acc_name = acc_name
        self.acc_balance = acc_balance
        self.acc_type = acc_type

    def __str__(self): #Acá impime los datos de la cuenta en un string
        return 'Account[' + str(self.acc_number) + '] - ' + self.acc_name + ', ' + self.acc_type + ' account = ' + str(self.acc_balance)

    def deposit(self, depo_amount): #Método para depositar en una cuenta
        self.acc_balance += depo_amount
        return print('A deposit has been made, of:', depo_amount)

    def withdraw(self, with_amount): #Método para extraer de una cuenta
        if with_amount > self.acc_balance:
            return print('The amount you want to withdraw is larger than your actual balance:', self.acc_balance)
        else:
            self.acc_balance -= with_amount
            return print('A withdraw has been made, of:', with_amount)

    def get_balance(self): #Obtine la info de la cuenta
        return self.acc_balance
#
#acc1 = Account('', 'Pedro', 50.00, 'investment')
#acc2 = Account('', 'Victoria', 75.00, 'current')
#
#print(acc1)
#print(acc2)
#acc2.withdraw(50.00)
#print(acc2)
#print('Number of Accounts instances created:', Account.instance_count)
print('-' * 20)
print(titulo.format('20').upper())
print('')

#HABILITAR EJERCICIO DEL CAP. 19 PARA USAR
#Este ejercicio depende de los datos del capítulo anterior, se crean las subcalses: Current, Deposit e Investment

class CurrentAccount(Account):
    def __init__(self, acc_number, acc_name, acc_balance, acc_type, overdraft_limit): #Acá es donde si yo saco el acc_type, después
        super().__init__(acc_number, acc_name, acc_balance, acc_type) #                me tira un error, porque le estoy  pidiendo 
        self.overdraft_limit = overdraft_limit #                                       que herede todo lo del padre
    
    def __str__(self):
        return super().__str__() + '. Overdraft limit: ' + str(self.overdraft_limit)
    
    def withdraw(self, with_amount):
        if with_amount > self.acc_balance + self.overdraft_limit:
            return print('The amount you want to withdraw surpasses your overdraft limit. Your current balance is:', self.acc_balance)
        else:
            self.acc_balance -= with_amount
            return print('A withdraw has been made, of: ', with_amount, '. Your current balance is: ', self.acc_balance, sep='')

class DepositAccount(Account):
    def __init__(self, acc_number, acc_name, acc_balance, acc_type, interest_rate):
        super().__init__(acc_number, acc_name, acc_balance, acc_type)
        self.interest_rate = interest_rate
    
    def __str__(self):
        return super().__str__() + '. Interest rate: ' + str(self.interest_rate)

class InvesmentAccount(Account):
    def __init__(self, acc_number, acc_name, acc_balance, acc_type, investment_type):
        super().__init__(acc_number, acc_name, acc_balance, acc_type)
        self.investment_type = investment_type

    def __str__(self):
        return super().__str__() + '. Investment type: ' + str(self.investment_type)

#acc1 = CurrentAccount('', 'Pedro', 100.00, )