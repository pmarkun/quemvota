# -*- coding: utf-8 -*-
class MatrizesDeDadosBuilder:

    def __init__(self, votacoes, partidos, parlamentares):
        self.votacoes = votacoes
        self.partidos = partidos
        self.parlamentares = parlamentares
        self.matriz_votacoes = [[0 for col in range(len(self.parlamentares))] for row in range(len(self.votacoes))]

        #self.matriz_presencas = [[0 for col in range(len(self.parlamentares))] for row in range(len(self.votacoes))]
        
        # array de partido.nome's, um por parlamentar
        self.partido_do_parlamentar = []
        
        # chave eh nome do partido, e valor eh VotoPartido
        self._dic_partido_votos = {}
        self._dic_parlamentares_votos = {}  # parlamentar.id => voto.opcao

    def gera_matrizes(self):
        """Cria duas matrizes:
            matriz_votacoes -- de votações (por parlamentares),
            matriz_presencas -- presenças de parlamentares
        Os valores possíveis na matriz de votações são:
        -1 (não), 0 (abtencão/falta) e 1 (sim).
        Os valores possíveis na matriz de presenças são:
        0 (falta) e 1 (presente).
        As linhas indexam parlamentares. As colunas indexam as votações.
        A ordenação das linhas segue a ordem de self.partidos ou
        self.parlamentares, e a ordenação das colunas segue a ordem
        de self.votacoes.
        Retorna matriz_votacoes
        """
        iv = -1  # índice votação
        for votacao in self.votacoes:
            iv += 1
            self._build_dic_parlamentares_votos(votacao)
            self._preenche_matrizes(votacao, iv)
        return self.matriz_votacoes

    def _build_dic_parlamentares_votos(self, votacao):
        # com o "select_related" fazemos uma query eager
        votos = votacao.voto_set.select_related(
            'votacao', 'parlamentar').all()
        for voto in votos:
            self._dic_parlamentares_votos[voto.parlamentar.id] = voto.opcao

    def _preenche_matrizes(self, votacao, iv):
        try:
            ip = -1  # indice parlamentares
            for parlamentar in self.parlamentares:
                ip += 1
                
                if parlamentar.id in self._dic_parlamentares_votos:
                    opcao = self._dic_parlamentares_votos[parlamentar.id]
                    self.matriz_votacoes[ip][iv] = self._opcao_to_double(opcao)
                    if (opcao == "AUSENTE"):
                        self.matriz_presencas[ip][iv] = 0.
                    else:
                        self.matriz_presencas[ip][iv] = 1.
                else:
                    self.matriz_votacoes[ip][iv] = 0.
                    self.matriz_presencas[ip][iv] = 0.
        except:
            pass

    def _opcao_to_double(self, opcao):
        if opcao == 'SIM':
            return 1.
        if opcao == 'NAO':
            return -1.
        return 0.
