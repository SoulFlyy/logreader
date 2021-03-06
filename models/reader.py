class Reader:
    def __init__(self):
        self.racer = {}
        self.laps = [0, 0, 0, 0]
        self.first = True

    # Metodo responsavel por limpar os espacos do arquivo e pegas apenas a coluna desejada
    # Parametros são, o arquivo sendo lido e o indice da coluna
    def clearSpace(self, line, ind):
        return " ".join(line.rstrip().split()[ind]).replace(' ', '')

    # Metodo responsavel por transformar a linha em um dicionario
    # Recebe como parametro a linha sendo lida 
    def creatOBJ(self, line):
        racerOBJ = {
            'nome': self.clearSpace(line, 3),
            'volta': self.clearSpace(line, 4),
            'tempo': self.clearSpace(line, 5),
            'posicao': ''
        }
        return racerOBJ

    # Metodo principal o qual trata de todos os rumos que a leitura pode levar, nele esta sentralizado a leitura do arquivo e as regras para estrurutar o JSON
    def logReader(self):
        f = open('corrida.log', 'r')
        first = True
        for line in f:
            racerId = self.clearSpace(line, 1)
            if first:
                first = False
            else:
                if racerId in self.racer:        
                    self.racer[racerId]['volta'] = self.clearSpace(line, 4)
                    self.racer[racerId]['tempo'] = self.sumTime(self.racer[racerId]['tempo'], self.clearSpace(line, 5))
                    if self.racer[racerId]['volta'] == '2':
                        self.laps[1] += 1
                        self.racer[racerId]['posicao'] = self.laps[1]
                    elif self.racer[racerId]['volta'] == '3':
                        self.laps[2] += 1
                        self.racer[racerId]['posicao'] = self.laps[2]
                    else:
                        self.laps[3] += 1
                        self.racer[racerId]['posicao'] = self.laps[3]
                        break
                else:
                    self.racer[racerId] = self.creatOBJ(line)
                    self.laps[0] += 1
                    self.racer[racerId]['posicao'] = self.laps[0]
        f.close
        return self.racer

    # Metodo responsavel por somar e edivar o tempo corretamente
    # Recebe como parametro o tempo atual e o tempo a ser somado
    def sumTime(self, origTime, newTime):
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