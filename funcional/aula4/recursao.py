# n! : 1 se n == 0 se nao n * (n-1)!
# n == 0 (caso base)
# n * (n-1)! (caso recursivo)

fat = lambda n : 1 if n == 0 else n * fat(n-1)

print fat(5)
