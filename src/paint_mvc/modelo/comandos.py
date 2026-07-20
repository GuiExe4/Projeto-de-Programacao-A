from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self):
        pass

    @abstractmethod
    def desfazer(self):
        pass

class ComandoAdicionar(Comando):
    def __init__(self, controller, figura):
        self.controller = controller
        self.figura = figura

    def executar(self):
        if self.figura not in self.controller.self_historico_figuras:
            self.controller.self_historico_figuras.append(self.figura)

    def desfazer(self):
        if self.figura in self.controller.self_historico_figuras:
            self.controller.self_historico_figuras.remove(self.figura)
            if self.figura in self.controller.figuras_selecionadas:
                self.controller.figuras_selecionadas.remove(self.figura)

class ComandoMover(Comando):
    def __init__(self, controller, figuras, dx, dy):
        self.controller = controller
        self.figuras = list(figuras)
        self.dx = dx
        self.dy = dy

    def _mover(self, dx, dy):
        for figura in self.figuras:
            if figura.__class__.__name__ == "MaoLivre":
                figura.pontos = [(px + dx, py + dy) for px, py in figura.pontos]
            elif figura.__class__.__name__ == "FiguraComposta":
                for sub in figura.figuras:
                    if sub.__class__.__name__ == "MaoLivre":
                        sub.pontos = [(px + dx, py + dy) for px, py in sub.pontos]
                    else:
                        sub.x1 += dx
                        sub.y1 += dy
                        sub.x2 += dx
                        sub.y2 += dy
            else:
                figura.x1 += dx
                figura.y1 += dy
                figura.x2 += dx
                figura.y2 += dy

    def executar(self):
        self._mover(self.dx, self.dy)

    def desfazer(self):
        self._mover(-self.dx, -self.dy)

class ComandoApagar(Comando):
    def __init__(self, controller, figuras):
        self.controller = controller
        self.figuras = list(figuras)
        self.posicoes = []

    def executar(self):
        self.posicoes.clear()
        for figura in self.figuras:
            if figura in self.controller.self_historico_figuras:
                idx = self.controller.self_historico_figuras.index(figura)
                self.posicoes.append((idx, figura))
                self.controller.self_historico_figuras.remove(figura)
        self.controller.figuras_selecionadas = []

    def desfazer(self):
        for idx, figura in sorted(self.posicoes, key=lambda x: x[0]):
            self.controller.self_historico_figuras.insert(idx, figura)
        self.controller.figuras_selecionadas = list(self.figuras)

class ComandoMudarCor(Comando):
    def __init__(self, controller, figuras, nova_cor, tipo_cor="borda"):
        self.controller = controller
        self.figuras = list(figuras)
        self.nova_cor = nova_cor
        self.tipo_cor = tipo_cor
        self.cores_antigas = []

        for f in self.figuras:
            cor_atual = f.cor_borda if tipo_cor == "borda" else getattr(f, "cor_preenchimento", "white")
            self.cores_antigas.append(cor_atual)

    def executar(self):
        for f in self.figuras:
            if self.tipo_cor == "borda":
                f.cor_borda = self.nova_cor
            else:
                f.cor_preenchimento = self.nova_cor

    def desfazer(self):
        for f, cor in zip(self.figuras, self.cores_antigas):
            if self.tipo_cor == "borda":
                f.cor_borda = cor
            else:
                f.cor_preenchimento = cor

class ComandoAgrupar(Comando):
    def __init__(self, controller, figuras_para_agrupar):
        self.controller = controller
        self.figuras = list(figuras_para_agrupar)
        self.grupo = None
        self.posicoes = []

    def executar(self):
        from modelo.figuras import FiguraComposta
        if not self.grupo:
            self.grupo = FiguraComposta()
            for f in self.figuras:
                self.grupo.adicionar(f)

        self.posicoes.clear()
        for f in self.figuras:
            if f in self.controller.self_historico_figuras:
                idx = self.controller.self_historico_figuras.index(f)
                self.posicoes.append((idx, f))
                self.controller.self_historico_figuras.remove(f)

        self.controller.self_historico_figuras.append(self.grupo)
        self.controller.figuras_selecionadas = [self.grupo]

    def desfazer(self):
        if self.grupo in self.controller.self_historico_figuras:
            self.controller.self_historico_figuras.remove(self.grupo)

        for idx, f in sorted(self.posicoes, key=lambda x: x[0]):
            self.controller.self_historico_figuras.insert(idx, f)

        self.controller.figuras_selecionadas = list(self.figuras)

class ComandoDesagrupar(Comando):
    def __init__(self, controller, grupos_para_desagrupar):
        self.controller = controller
        self.grupos = list(grupos_para_desagrupar)
        self.sub_figuras = []
        self.posicoes_grupos = []

    def executar(self):
        self.sub_figuras.clear()
        self.posicoes_grupos.clear()
        for grupo in self.grupos:
            if grupo in self.controller.self_historico_figuras:
                idx = self.controller.self_historico_figuras.index(grupo)
                self.posicoes_grupos.append((idx, grupo))
                self.controller.self_historico_figuras.remove(grupo)
                for sub in grupo.figuras:
                    self.controller.self_historico_figuras.append(sub)
                    self.sub_figuras.append(sub)
        self.controller.figuras_selecionadas = list(self.sub_figuras)

    def desfazer(self):
        for sub in self.sub_figuras:
            if sub in self.controller.self_historico_figuras:
                self.controller.self_historico_figuras.remove(sub)

        for idx, grupo in sorted(self.posicoes_grupos, key=lambda x: x[0]):
            self.controller.self_historico_figuras.insert(idx, grupo)

        self.controller.figuras_selecionadas = list(self.grupos)