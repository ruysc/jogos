print("*******************************")
print("Ola mundo cruel da adivinhação!")
print("*******************************")

numero_secreto = 42
chute = int(input("Digite seu número: "))
print("Você digitou: ", chute)
if (chute == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou")
print("Fim do jogo!")