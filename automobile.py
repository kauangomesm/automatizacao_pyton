import pyautogui
import time

lista1 = [
"O sol brilha no mel",
"A chuva molha o chão",
"As folhas dançam ao vento",
"O mar murmura segredos antigos",
"A vida é uma jornada",
"O amor transcende fronteiras invisíveis",
"As estrelas cintilam na noite",
"Os pássaros cantam ao amanhecer",
"O tempo voa sem aviso",
"A esperança nunca morre completamente",
"A arte inspira a alma",
"A mente busca conhecimento incessantemente",
"A música acalma os corações inquietos",
"Os sorrisos iluminam os rostos",
"As lágrimas lavam a dor",
"A amizade é um tesouro",
"A verdade liberta as mentes",
"O silêncio fala volumes inteiros",
"O destino tecido pelas escolhas",
"O perdão cura feridas antigas",
"A fé move montanhas imensas",
]


lista2 = [
"A harmonia une os opostos",
"O otimismo alimenta a alma",
"A curiosidade desperta o conhecimento",
"A liberdade é um direito fundamental",
"O respeito fortalece os laços",
"A bondade ilumina o mundo",
"O trabalho árduo gera recompensas",
"A criatividade dá asas à imaginação",
"A generosidade aquece os corações",
"A simplicidade é a sofisticação suprema",
"O equilíbrio traz paz interior",
"A serenidade enfrenta tempestades",
"A honestidade é um valor inegociável",
"A compaixão acalma as dores alheias",
"O conhecimento é uma jornada constante",
"A reflexão traz clareza mental",
"A perseverança supera obstáculos",
"A comunicação fortalece os vínculos",
"A empatia conecta almas distantes",
"A cooperação constrói pontes",
"A resiliência é uma armadura",
]

time.sleep(2)

for x in lista2:
    # adicionar guia

    pyautogui.click(x=2241, y=831)

    time.sleep(3)

    # digitar na barra de pesquisa
    pyautogui.write(x)
    time.sleep(3)

    # pesquisar
    pyautogui.press('enter')

    time.sleep(5)

    # clicar em guias

    pyautogui.click(x=1776, y=978)

    time.sleep(3)

    # fechar a guia anterior

    pyautogui.click(x=1079, y=333)


    time.sleep(3)