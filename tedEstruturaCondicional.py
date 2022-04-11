#Em uma escola, a média final é dada pela média aritmética de três notas. E a mesma tem o seguinte esquema de avaliação: 
# |  Média  |  Situação do Aluno  |
# |  0 - 4.9  |  Aluno em recuperação  |
# | 5 - 6.9  | Aluno em prova final |
# | 7 - 10  | Aluno aprovado por média |
#Desenvolva um algoritmo que a partir da entrada das três notas mostre a situação do aluno.
#No caso do aluno em recuperação e prova final, mostre também quanto o aluno irá precisar para passar.
#No caso da recuperação a nota necessária para passar é dada por 10 – Média + 2 e na prova final é dado por 10 – Média.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
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
