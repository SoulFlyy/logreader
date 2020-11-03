# Funcao que define o corpo do dicionario principal que sera extraido do arquivo de Log
# O parametro recebido eh a String da linha presente
def creatOBJ(line):
    racerOBJ = {
        'nome': " ".join(line.rstrip().split()[3]).replace(' ', ''),
        'volta': " ".join(line.rstrip().split()[4]).replace(' ', ''),
        'tempo': " ".join(line.rstrip().split()[5]).replace(' ', ''),
        'posicao': ''
    }
    return racerOBJ

# Funcao que formata e soma o tempo de cada volta dos competidores
# Os parametros recebidos sao tempo que ja esta no diconario e novo tempo 
def sumTime(origTime, newTime):
    minu = int(origTime.split(':')[0]) + int(newTime.split(':')[0])
    sec = int(origTime.split(':')[1].split('.')[0]) + int(newTime.split(':')[1].split('.')[0])
    mill = int(origTime.split(':')[1].split('.')[1]) + int(newTime.split(':')[1].split('.')[1])
    if mill >= 1000:
        mill -= 1000
        sec += 1
    if sec >= 60:
        sec -= 60
        minu += 1
    millStr = str(mill) if mill > 100 else '0' + str(mill)
    secStr = str(sec) if sec > 10 else '0' + str(sec)
    minuStr = str(minu)
    time = minuStr + ':' + secStr + '.' + millStr
    return time

# Funcao resposavel em fazero print final na tela, esta separada do corpo principal, pois em um Back end real, seria descartada
# O parametro recebido eh o dicionario com todas as informacoes a serem passadas para a tena de uma forma mais amigavel
def podium(racers):
    for racer in racers:
        print('Posicao: ' + str(racers[racer]['posicao']) + '; ID: ' + racer + '; Nome: ' + racers[racer]['nome'] + '; Qtd de voltas: ' + racers[racer]['volta'] + '; Tempo de prova: ' + racers[racer]['tempo'])

# Funcao mais volatil de todas onde se concentra a logica e caminhos que o programa pode seguir
# O parametro recebiodo eh o nome do arquivol log a ser pesquisado
def logReader(file):
    racer = {}
    laps = [0, 0, 0, 0]
    f = open(file + '.log', 'r')
    first = True
    for line in f:
        racerId = " ".join(line.rstrip().split()[1]).replace(' ', '')
        if first:
            first = False
        else:
            if racerId in racer:        
                racer[racerId]['volta'] = " ".join(line.rstrip().split()[4]).replace(' ', '')
                racer[racerId]['tempo'] = sumTime(racer[racerId]['tempo'], " ".join(line.rstrip().split()[5]).replace(' ', ''))
                if racer[racerId]['volta'] == '2':
                    laps[1] += 1
                    racer[racerId]['posicao'] = laps[1]
                elif racer[racerId]['volta'] == '3':
                    laps[2] += 1
                    racer[racerId]['posicao'] = laps[2]
                else:
                    laps[3] += 1
                    racer[racerId]['posicao'] = laps[3]
                    break
            else:
                racer[racerId] = creatOBJ(line)
                laps[0] += 1
                racer[racerId]['posicao'] = laps[0]
    f.close
    podium(racer)

logReader('corrida')


