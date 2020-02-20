#How to pass a lot of params withoutDeclares


#know animals means any animal the person knows ,
#description means a animal named and its descrption


'''
With * is only params withoutname
With ** is with params named
'''

def animals(favorite, *knowAnimals,**description):
    print("Your favorie animal is: ", favorite, " With param mandatory")
    print('\n')
    print('Not named params')
    #This dont give a spify value...
    for an in knowAnimals:
        print("Paramerter ", an , "Its name that: ",knowAnimals)
    print('-' * 40)#print a lot of aschterict
    for d  in description:
        print("Name: ", d, ':', description[d])
    print("FINISHED PROGRAMM")


myDescription : dir = {
    "I like" : "The perico",
    "More " : "To mas info"
}

animals("Cat","Elefhanp","Jirhapie","Nokore",ilove = "pericazo",)

#Nice example...


def concatenar(*args, sep="/"):
     return sep.join(args)

concatenar("tierra", "marte", "venus")

concatenar("tierra", "marte", "venus", sep=".")

'''
>>> def hacer_incrementador(n):
...     return lambda x: x + n
...
>>> f = hacer_incrementador(42)
>>> f(0)
42
>>> f(1)
43

'''


def getDoc():
    '''
    a line should be 79 caracters or large....
    With .doc 
    '''
    pass

print(getDoc.__doc__)

#Anotacion de funciones...
#Asi se regresa una funcion de algun tipo...
def annotation(meal : str, drink : str = 'Water') -> str: 
    print('My meal is: ', meal,' and my drinks is: ', drink)
    return 'My argumens ' + meal + ' and ' + drink

print(annotation('Jamon'))












    
    