# Funciones que no tienen un nombre, funciones anonimas
# lambda argumentos: expresion 
# solo pueden tener una sola linea de codigo

#Palindromo         Argumento que recibe
palindrome = lambda argument: argument == argument[::-1]
# Para llamar a la funcion, hacemos llamado a la variable

print(palindrome('ana'))