
#A function defined
def add(numberOne,numberTwo):
    return numberOne + numberTwo


print(add(5,10))

#lambda functions...

print('\n')

#name =  lambda function  two numbers   => numberOne - numbertwo...
substraction = lambda numberOne,numberTwo : numberOne - numberTwo

print(substraction(5,10))

#Functions like in dart

#Mandatory parameter or optional...

def ask_confirmation (mandatoryMsg,retries = 4,reminder = 'Dont forget anything'):
   
    ok = input(mandatoryMsg + '\n')

    if ok in ('s','si','ok'):
        return True
    if ok in ('n','no','No'):
        return False
    retries = retries - 1

    print('Retries remainig {retries}')

    if retries == 0:
        raise ValueError('Invalidate answer')
    print('Reminder ' + reminder)
    

#ask_confirmation('Wasup type \'s\'')

def pedir_confirmacion(prompt, reintentos=4, recordatorio='Por favor, intente nuevamente!'):
    while True:
        ok = input(prompt + '\n')
        if ok in ('s', 'S', 'si', 'Si', 'Si'):
            return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise ValueError('respuesta de usuario invalida')
        print(recordatorio)

#first the manatory function then the optional o defalutt value
def printName(mandoryName,value = 'Rolando'):
    print(value + mandoryName)
    msgUser = str(input())
    print(msgUser)


def f(a,L = []): 
    L.append(a)
    return L

# print(f(1))#Added a number 1 into an array with zero values
# print(f(2))#Added a number 2 with the value 1
# print(f(3))

# print this
# [1]
# [1, 2]
# [1, 2, 3]

# print('Tested')


def e(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

'''
print(e(1)) #Added a number 1 into an array with zero values
print(e(2)) #Added a number 2 with the value 1
print(e(3))

this dont save the before values...

[1]
[2]
[3]
'''

#How dont called the functions...

#loro()                      # falta argumento obligatorio
#loro(tension=5.0, 'muerto') # argumento posicional luego de uno nombrado
#loro(110, tension=220)      # valor duplicado para el mismo argumento
#loro(actor='Juan Garau')    # nombre del argumento desconocido















    


 