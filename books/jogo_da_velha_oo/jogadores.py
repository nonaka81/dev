import copy
from random import randint

class Jogadores(object):

    def __init__(self, controle, posicoes):
        self.controle = controle
        self.posicoes = posicoes
        self.fim_de_partida = False
        self._vencedor = None
    
    def _set_vencedor(self, vencedor):
        self._vencedor = vencedor
    
    def _get_vencedor(self):
        return copy.copy(self._vencedor)
    
    vencedor = property(_get_vencedor, _set_vencedor)

    def jogador(self):
        if self.posicoes[self.controle.pos_y][self.controle.pos_x] == ' ':
            self.posicoes[self.controle.pos_y][self.controle.pos_x] == 'X'
            return True
        return False
    
    def robo(self):
        vazias = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.posicoes[j][i] == ' ':
                    vazias.append([j, i])
        
        n_escolhas = len(vazias)
        
        if n_escolhas != 0:
            j, i = vazias[randint(0, n_escolhas - 1)]
            self.posicoes[j][i] = 'O'

    def __total_alinhado(self, linha):
        num_x = linha.count('X')
        num_o = linha.count('O')

        if num_x == 3:
            return 'X'
        
        if num_o == 3:
            return 'O'
        
        return None
    
    def ganhador(self):
        diagonal1 = [self.posicoes[0][0],
                     self.posicoes[1][1],
                     self.posicoes[2][2]]
        
        diagonal2 = [self.posicoes[0][2],
                     self.posicoes[1][1],
                     self.posicoes[2][0]]
        
        gan = self.__total_alinhado(diagonal1)
        if gan is not None:
            self._vencedor = gan
            return True

        gan = self.__total_alinhado(diagonal2)
        if gan is not None:
            self._vencedor = gan
            return True
        
        transposta = [[], [], []]
        for i in range(3):
            for j in range(3):
                transposta[i].append(self.posicoes[j][i])
        
        velha = 9
        for i in range(3):
            gan = self.__total_alinhado(self.posicoes[i])
            if gan is not None:
                self._vencedor = gan
                return True
        
        gan = self.__total_alinhado(transposta[i])

        if gan is not None:
            self._vencedor = gan
            return True
        
        velha -= self.posicoes[i].count('X')
        velha -= self.posicoes[i].count('O')

        if velha == 0:
            self._vencedor = 'Velha'
            return True
        
        return False
    
    def jogar(self):
        jogou = self.jogador()
        self.fim_de_partida = self.ganhador()

        if jogou is True and self.fim_de_partida is False:
            self.robo()
            self.fim_de_partida = self.ganhador()
