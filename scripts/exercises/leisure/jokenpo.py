# Pedra, Papel, Tesoura

import random

def compare(choice, cpu):

  if choice.lower() == cpu:
    return "Empate!"
  if cpu == "pedra":
    if choice.lower() == "tesoura":
      return "Derrota!"
    else:
      return "Vitória!"
  if cpu == "papel":
    if choice.lower() == "tesoura":
      return "Vitória!"
    else:
      return "Derrota!"
  if cpu == "tesoura":
    if choice.lower() == "papel":
      return "Vitória!"
    else:
      return "Derrota!"

def JoKenPo():
  choices = ["pedra", "papel", "tesoura"]

  choice = str(input("Insira sua escolha: "))
  cpu = choices[random.randint(0, 2)]


  print(choice, cpu)
  print(compare(choice, cpu))

# Par ou Ímpar
def ParOuImpar():
  choice = int(input("Insira seu número: "))
  cpu = random.randint(0,10)
  if (choice + cpu) % 2 == 0:
    print(choice,"+", cpu, "= Par!")
  else:
    print(choice,"+", cpu, "= Ímpar!")