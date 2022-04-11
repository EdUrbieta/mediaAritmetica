nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
media = (nota1 + nota2 + nota3) / 3
provaFinal = 10 - media
recuperacao = 10 - media + 2
print("A sua média aritmética é: ", round(media, 1))
if media >= 7:
    print("O aluno foi aprovado por média!")
elif media >= 5:
    print("O aluno está em prova final! Deverá tirar na prova final", round(provaFinal, 1), "para ser aprovado!")
else:
    print("O aluno está em recuperacao! Deverá tirar na recuperação", round(recuperacao, 1), "para ser aprovado!")
