#diccionario
alumnos = {
    "Carlos" : 9,
    "Maria" : 8.5,
    "José" : 7.8,
    "Pedro" : 9.8,
    "Julio" : 7,
    "Carolina" : 8.5,
    "Pablo" : 7.6
}
valor_promedio = alumnos["Carlos"]
print(valor_promedio)

alumnos["Maria"] = 10 #modificar promedio

print(alumnos)

#añadir nuevo elemento
alumnos["Karla"] = 7.8
print(alumnos) 

recorrer = map(lambda n: n +0 for alumnos)