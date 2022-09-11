x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0]=15
estudiantes[0]['last_name']='Bryant'
directorio_deportes['fútbol'][0]='Andres'
z[0]['y']=30
print(x)
print(estudiantes)
print(directorio_deportes)
print(z)



estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(estudiantes): 
    for  estudiante in estudiantes:
        for key in estudiante:
            print(f'{key} - {estudiante[key]}')
iterateDictionary(estudiantes)


def iterateDictionary2(key_name, some_list):
    for diccionario in some_list:
        print(diccionario[key_name])
iterateDictionary2('first_name',estudiantes) 
iterateDictionary2('last_name',estudiantes) 

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]),key)
        for y in some_dict[key]:
            print(y)
    
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

    
