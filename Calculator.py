print("Olá, Eu sou uma calculadora!")

print("O você gostaria de calcular?")

while True:
    try:
        valor1 = float(input("Digite o prmeiro número: "))
        valor2 = float(input("Digite o segundo número: "))
        operador = input("Digite o operador matemático (+, -, *, /): ")
        if operador not in ["+", "-", "*", "/"]:
            raise ValueError("Operador inválido")
        break
    except ValueError:
        print("Por favor, incira um número válido")
        
if operador == "+":
    resultado = valor1 + valor2
elif operador == "-":
    resultado = valor1 - valor2
elif operador == "*":
    resultado = valor1 * valor2
elif operador == "/":
    resultado = valor1 / valor2

print("resultado: ", resultado)