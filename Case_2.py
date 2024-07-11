import random

def function():
 try:
  print("Выбирите уровень сложности: \n 1. Легкий(7 попыток) \n 2. Средний(5 попыток) \n 3. Сложный(3 попытки)")
  difficult = int(input())
  Tries_User = 0
  Answer_User = 0
  match difficult:
   case 1:
    Tries = 7
   case 2:
    Tries = 5
   case 3:
    Tries = 3
  print("Введите загадонное число")
  Answer = random.randint(0, 100)
  while(Answer != Answer_User and Tries_User != Tries):
    Answer_User = int(input())
    Tries_User = Tries_User + 1
    if (Answer_User > Answer):
     print("Ваше число больше загаданного")
    else:
     print("Ваше число меньше загадонного")
  else:
    if (Tries_User == Tries):
     print("Вы проиграли, у вас закончилсь попытки, загаданное число", Answer)
    else:
     print("Поздравляю, вы победили! Загаданное число", Answer)
 except:
  print("Введите корректные данные")
  function()
function()

