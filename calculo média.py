nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
media_exercicios = float(input("Informe a média dos exercícios: "))
media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

conceito = ""
if media_aproveitamento > 9.0:
    conceito = "A"
elif media_aproveitamento >= 7.5 and media_aproveitamento < 9.0:
    conceito = "B"
elif media_aproveitamento >= 6.0 and media_aproveitamento < 7.5:
    conceito = "C"
elif media_aproveitamento >= 4.0 and media_aproveitamento < 6.0:
    conceito = "D"
else:
    conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
    print("O conceito do aluno é", conceito)
    print("O aluno está aprovado")
else:
    print("O conceito do aluno é", conceito)
    print("O aluno está reprovado")