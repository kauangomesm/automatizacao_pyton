import pyautogui
import time


listam1 = [
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

listam2 = [
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


listap1 = [
"O sol brilha no céu",
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
"A paciência é uma virtude",
"Os sonhos alimentam a alma",
"A coragem enfrenta medos profundos",
"O conhecimento expande horizontes infinitos",
"A beleza reside na simplicidade",
"As memórias aquecem o coração",
"A solidão ensina lições valiosas",
"O riso contagia os espíritos",
"A gratidão transforma perspectivas",
"Os desafios fortalecem o caráter",
]

listap2 = [
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
"A autoconfiança impulsiona conquistas",
"A gratidão enriquece o espírito",
"A autenticidade é a chave",
"A humildade é a base da grandeza",
"A introspecção traz autoconhecimento",
"A tolerância amplia horizontes",
"A transformação começa de dentro para fora",
"A esperança é uma luz guia",
"O amor é a essência da vida",
"A gentileza suaviza as arestas",
"O sol brilha no céu",
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
"A amizade é um tesouro"
]

time.sleep(2)

for x in listam2:
    # adicionar guia
    pyautogui.click(x=2241, y=831)
    time.sleep(3)

    # clicar na barra de pesquisa
    pyautogui.click(x=1422, y=412)
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

#limpar historico
pyautogui.click(x=743, y=995)
time.sleep(1)
pyautogui.click(x=1174, y=103)
time.sleep(4)
pyautogui.click(x=1291, y=629)
time.sleep(4)
pyautogui.click(x=1654, y=223)
time.sleep(3)
pyautogui.click(x=1570, y=223)
time.sleep(2)
pyautogui.click(x=1568, y=165)
time.sleep(1)
pyautogui.click(x=1654, y=223)
time.sleep(2)
pyautogui.click(x=1570, y=223)
time.sleep(2)


#fechar o bluestacks
pyautogui.click(x=2510, y=10)
time.sleep(1)
pyautogui.click(x=1375, y=558)
time.sleep(1)

pyautogui.click(x=1101, y=1061)
time.sleep(1)

for x in listap2:
    # clicar na barra de pesquisa
    pyautogui.click(x=350, y=50)
    time.sleep(1)

    # digitar na barra de pesquisa
    pyautogui.write(x)

    # pesquisar
    pyautogui.press('enter')

    time.sleep(5)

    # abrir uma nova guia
    pyautogui.hotkey('ctrl', 't')
    
    # fechar a guia anterior
    pyautogui.click(x=269, y=17)
    time.sleep(1)