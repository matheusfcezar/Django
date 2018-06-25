from random import randint

COORDENADAS_INVALIDAS = "Coodenadas Invalidas"
JOGADA_SEGURA = "Jogada Segura"
GAME_OVER = "Game Over"
VITORIA = "Parabéns você venceu"


class CampoMinadoView:

    def novo_jogo(self, linha, coluna):
       
        self.__linha = linha
        self.__coluna = coluna
        self.__matriz = self.__init_matriz(linha, coluna)
        self.__coordenadas = self.__distribuir_bombas()
        self.jogadas_restantes = self.__calcular_jogadas()
        
    def jogada(self, linha, coluna):


        if not self.__validar_coordenadas(linha,coluna):
            return COORDENADAS_INVALIDAS
        if self.__procurar_bomba(linha, coluna):
            return GAME_OVER

        self.__marcar_posicao(linha, coluna, self.__contar_bombas_adjacentes(linha, coluna))
        
        self.jogadas_restantes -=1

        if self.jogadas_restantes == 0:
            return VITORIA
        else:
            return JOGADA_SEGURA

    def retornar_matriz(self):
        return self.__matriz

    def imprimir_matriz(self):
        for posicao in self.__matriz:
            print(str(posicao))

    def jogadas_restantes(self):
        return self.jogadas_restantes

    def __init_matriz(self, linha, coluna):
   
        return [["X" for x in range(coluna)] for j in range(linha)]

    def __distribuir_bombas(self):
        quantidade_bombas = self.__total_bombas()
        coordenadas_bombas = []
        while quantidade_bombas > 0:
            coordenada = (randint(0, self.__linha - 1), randint(0, self.__coluna - 1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                print("("+str(coordenada[0]+1)+","+ str(coordenada[1]+1)+")")
                quantidade_bombas -= 1
        return coordenadas_bombas

    def __total_bombas(self):
        return int((self.__linha * self.__coluna) / 3)
    def __validar_coordenadas(self, linha, coluna):
        if linha in range(0, self.__linha) and coluna in range(0, self.__coluna):
            return True
        return False
    
    def __procurar_bomba(self, linha, coluna):
        return (linha, coluna) in self.__coordenadas

    def __contar_bombas_adjacentes(self, linha, coluna):
        linha_adjacente = linha - 1
        total_bombas = 0
        while linha_adjacente <= linha + 1:
            coluna_adjacente = coluna - 1
            while coluna_adjacente <= coluna + 1:
                if self.__procurar_bomba(linha_adjacente, coluna_adjacente):
                    total_bombas += 1
                coluna_adjacente += 1
            linha_adjacente += 1
        return total_bombas

    def __marcar_posicao(self, linha, coluna, quantidade_bombas):
        self.__matriz[linha][coluna] = str(quantidade_bombas)

    def __calcular_jogadas(self):
        return (self.__linha * self.__coluna) - self.__total_bombas()
