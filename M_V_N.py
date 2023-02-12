#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

M = "Matutino"
V = "Vespertino"
N = "Noturno"

tur = str(input("Em qual turno você estuda? Digite M-matutino ou V-Vespertino ou N- Noturno:"))
if tur == M:
    print("Bom dia!")
elif tur == V:
    print("Boa tarde!")
elif tur == N:
    print("Boa noite!")