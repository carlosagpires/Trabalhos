#Programa Calculadora Simples
#Recebe uma string
#Verifica se os caractares são válidos
#Executa a operação com a função eval()

while(1):
    operation = input("\nCALCULADORA (Para sair do programa escreva 'q')\nInsira uma expressão matemática a calcular. Utilize apenas números, parentesis '()' e os seguintes operadores:\n - soma: '+';\n - subtração: '-';\n - multiplicação: '*';\n - divisão: '/';\n - potência: '**'.\nExpressão: ");
    if operation == "q":
        break
    correctChars = "0123456789+-/*()"
    for char in operation:
        if char not in correctChars:
            print("\n\nA operação introduzida é inválida!")
            break
    try:
        print("\nResultado: " + operation + " = " + str(eval(operation)) + "\n")
    except:
        print("\nOpssss!!!! Verifique a sua expressão!")
