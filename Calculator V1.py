print("Olá, Eu sou uma calculadora!")

print("O você gostaria de calcular?")

def get_float_input(prompt):
        while True:
                try:
                    valor = float(input(prompt))
                    return valor
                except ValueError:
                    print("Valor inválido. Por Favor, digite um número Válido")
                
valor1 = get_float_input("Digite o primeiro número: ")
valor2 = get_float_input("Digite o segundo número: ")

while True:
      operador = input("Digite o operador matemático (+, -, *, /): ")
      if operador not in ["+", "-", "*", "/"]:
            print("Operador inválido. Por favor, digite um operador válido.")
      else:
            break
      
if operador == "+":
    resultado = valor1 + valor2
elif operador == "-":
    resultado = valor1 - valor2
elif operador == "*":
    resultado = valor1 * valor2
elif operador == "/":
    resultado = valor1 / valor2

# imprime o resultado
print("Resultado:", resultado)