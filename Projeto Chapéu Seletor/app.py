Grifinoria = 0
Lufalufa = 0
Corvinal = 0
Sonserina = 0

pergunta1 = int(input('Você gosta mais do Amanhecer (1) ou do Anoitecer(2)?'))
if pergunta1 == 1:
  Grifinoria += 1
  Corvinal += 1
elif pergunta1 == 2:
  Lufalufa += 1
  Sonserina += 1
else:
  print('Resposta errada!')

pergunta2 = int(input('Quando eu morrer, quero que as pessoas se lembrem de mim como: O Bom (1), O Grande (2), O Sabio (3) ou O Corajoso (4)?'))
if pergunta2 == 1:
  Lufalufa += 2
elif pergunta2 == 2:
  Sonserina += 2
elif pergunta2 == 3:
  Corvinal += 2
elif pergunta2 == 4:
  Grifinoria += 2
else:
  print('Resposta errada!')        

pergunta3 = int(input('Que tipo de instrumento mais agrada seus ouvidos? 1)Violino, 2)Trompete, 3)Piano ou 4)Tambor'))
if pergunta3 == 1:
  Sonserina += 4
elif pergunta3 == 2:
  Lufalufa += 4
elif pergunta3 == 3:
  Corvinal += 4
elif pergunta3 == 4:
  Grifinoria += 4
else:
  print('Resposta errada!')

vencedor = max(Grifinoria, Sonserina, Corvinal, Lufalufa)

if vencedor == Grifinoria:
  print('Parabéns você é da Grifinoria!!!')
elif vencedor == Sonserina:
  print('Parabéns você é da Sonserina!!!')
elif vencedor == Corvinal:
  print('Parabéns você é da Corvinal!!!')
else:
  print('Parabéns você é da Lufa Lufa!!!')      