# Funcao que define o corpo do dicionario principal que sera extraido do arquivo de Log
def creatOBJ(line):
    racerOBJ = {
        'nome': " ".join(line.rstrip().split()[3]).replace(' ', ''),
        'volta': " ".join(line.rstrip().split()[4]).replace(' ', ''),
        'tempo': " ".join(line.rstrip().split()[5]).replace(' ', ''),
        'posicao': ''
    }
    return racerOBJ

# Funcao que formata e soma o tempo de cada volta dos competidores
def sumTime(origTime, newTime):
    minu = int(origTime.split(':')[0]) + int(newTime.split(':')[0])
    seg = int(origTime.split(':')[1].split('.')[0]) + int(newTime.split(':')[1].split('.')[0])
    mill = int(origTime.split(':')[1].split('.')[1]) + int(newTime.split(':')[1].split('.')[1])
    if mill >= 1000:
        mill -= 1000
        seg += 1
    if seg >= 60:
        seg -= 60
        minu += 1
    millStr = str(mill) if mill > 100 else '0' + str(mill)
    segStr = str(seg) if seg > 10 else '0' + str(seg)
    minuStr = str(minu)
    time = minuStr + ':' + segStr + '.' + millStr
    return time

# Funcao rfesposavel em fazero print final na tela, esta separada do corpo principal, pois em um Back end real, seria descartada
def podium(racers):
    for racer in racers:
        print('Posicao: ' + str(racers[racer]['posicao']) + '; ID: ' + racer + '; Nome: ' + racers[racer]['nome'] + '; Qtd de voltas: ' + racers[racer]['volta'] + '; Tempo de prova: ' + racers[racer]['tempo'])

# Funcao mais volatil de todas onde se concentra a logica e caminhos que o programa pode seguir
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
                if racer[racerId]['volta'] == '1':
                    laps[0] += 1
                    racer[racerId]['posicao'] = laps[0]
                elif racer[racerId]['volta'] == '2':
                    laps[1] += 1
                    racer[racerId]['posicao'] = laps[1]
                elif racer[racerId]['volta'] == '3':
                    laps[2] += 1
                    racer[racerId]['posicao'] = laps[2]
                else:
                    laps[3] += 1
                    racer[racerId]['posicao'] = laps[3]
            else:
                racer[racerId] = creatOBJ(line)
    f.close
    podium(racer)

logReader('corrida')


