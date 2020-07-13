import numpy as np

ano = np.loadtxt("carros-anos.txt",dtype=int)
km = np.loadtxt("carros-km.txt",dtype=int)

print(ano.size)

#coloca dados dos 2 arquivos em duas colunas
array = np.column_stack((ano, km))

#printa formato do array
print(array.shape)

#copia array original
new_array = array.copy()

#cria uma nova coluna com zeros
new_column = np.zeros((258, 1), dtype=int)

#adiciona coluna com zeros ao array existente
array2 = np.append(new_array, new_column, axis=1)

#calcula novo campo no array2 (km rodado por ano até 2019)
array2[:, 2] = array2[:, 1]/(2019-array2[:, 0])

#printa o resultado definindo valor 0 como mínímo, ou seja, substitui os negativos
#print(array2.clip(0))


#filtra só carros com ano 2002 e 2019
a = np.asarray(array2)
filter = np.asarray([2002, 2019])
mask = np.in1d(a[:, 0], filter)
print(a[mask])


