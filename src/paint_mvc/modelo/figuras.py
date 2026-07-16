class Figura:
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "x1": self.x1, "y1": self.y1,
            "x2": self.x2, "y2": self.y2,
            "cor_borda": self.cor_borda,
            "cor_preenchimento": self.cor_preenchimento
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            x1=data["x1"],
            y1=data["y1"],
            x2=data["x2"],
            y2=data["y2"],
            cor_borda=data["cor_borda"],
            cor_preenchimento=data["cor_preenchimento"]
        )

    def contem_ponto(self, x, y):
        margem = 5
        xmin = min(self.x1, self.x2) - margem
        xmax = max(self.x1, self.x2) + margem
        ymin = min(self.y1, self.y2) - margem
        ymax = max(self.y1, self.y2) + margem
        return xmin <= x <= xmax and ymin <= y <= ymax


class Linha(Figura):
    def desenhar(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda)

    def contem_ponto(self, x, y):
        margem = 5
        xmin, xmax = min(self.x1, self.x2), max(self.x1, self.x2)
        ymin, ymax = min(self.y1, self.y2), max(self.y1, self.y2)

        if not (xmin - margem <= x <= xmax + margem and ymin - margem <= y <= ymax + margem):
            return False

        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        if dx == 0 and dy == 0:
            return False

        distancia = abs(dy * x - dx * y + self.x2 * self.y1 - self.y2 * self.x1) / ((dy ** 2 + dx ** 2) ** 0.5)
        return distancia <= margem


class Retangulo(Figura):
    def desenhar(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor_borda, fill=self.cor_preenchimento)


class Oval(Figura):
    def desenhar(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline=self.cor_borda, fill=self.cor_preenchimento)


class Poligono(Figura):
    def desenhar(self, canvas):
        topo_x = (self.x1 + self.x2) // 2
        topo_y = self.y1

        base_esq_x = self.x1
        base_esq_y = self.y2

        base_dir_x = self.x2
        base_dir_y = self.y2

        canvas.create_polygon(
            topo_x, topo_y,
            base_esq_x, base_esq_y,
            base_dir_x, base_dir_y,
            outline=self.cor_borda,
            fill=self.cor_preenchimento
        )


class MaoLivre(Figura):
    def __init__(self, cor_borda):
        super().__init__(0, 0, 0, 0, cor_borda, "white")
        self.pontos = []

    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y))

    def desenhar(self, canvas):
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill=self.cor_borda)

    def to_dict(self):
        return {"tipo": "MaoLivre", "cor_borda": self.cor_borda, "pontos": self.pontos}

    @classmethod
    def from_dict(cls, data):
        obj = cls(cor_borda=data["cor_borda"])
        obj.pontos = [tuple(p) for p in data["pontos"]]
        return obj

    def contem_ponto(self, x, y):
        margem = 5
        for px, py in self.pontos:
            if abs(px - x) <= margem and abs(py - y) <= margem:
                return True
        return False


class FiguraComposta:
    def __init__(self, figuras=None):
        self.figuras = figuras if figuras is not None else []
        self._cor_borda = "black"
        self._cor_preenchimento = "white"

    @property
    def cor_borda(self):
        return self._cor_borda

    @cor_borda.setter
    def cor_borda(self, cor):
        self._cor_borda = cor
        for figura in self.figuras:
            figura.cor_borda = cor

    @property
    def cor_preenchimento(self):
        return self._cor_preenchimento

    @cor_preenchimento.setter
    def cor_preenchimento(self, cor):
        self._cor_preenchimento = cor
        for figura in self.figuras:
            if hasattr(figura, "cor_preenchimento"):
                figura.cor_preenchimento = cor

    @property
    def x1(self):
        if not self.figuras:
            return 0
        valores = []
        for f in self.figuras:
            if f.__class__.__name__ == "MaoLivre":
                if f.pontos:
                    valores.append(min(p[0] for p in f.pontos))
            else:
                valores.append(min(f.x1, f.x2))
        return min(valores) if valores else 0

    @x1.setter
    def x1(self, valor):
        pass

    @property
    def y1(self):
        if not self.figuras:
            return 0
        valores = []
        for f in self.figuras:
            if f.__class__.__name__ == "MaoLivre":
                if f.pontos:
                    valores.append(min(p[1] for p in f.pontos))
            else:
                valores.append(min(f.y1, f.y2))
        return min(valores) if valores else 0

    @y1.setter
    def y1(self, valor):
        pass

    @property
    def x2(self):
        if not self.figuras:
            return 0
        valores = []
        for f in self.figuras:
            if f.__class__.__name__ == "MaoLivre":
                if f.pontos:
                    valores.append(max(p[0] for p in f.pontos))
            else:
                valores.append(max(f.x1, f.x2))
        return max(valores) if valores else 0

    @x2.setter
    def x2(self, valor):
        pass

    @property
    def y2(self):
        if not self.figuras:
            return 0
        valores = []
        for f in self.figuras:
            if f.__class__.__name__ == "MaoLivre":
                if f.pontos:
                    valores.append(max(p[1] for p in f.pontos))
            else:
                valores.append(max(f.y1, f.y2))
        return max(valores) if valores else 0

    @y2.setter
    def y2(self, valor):
        pass

    def adicionar(self, figura):
        if figura not in self.figuras:
            self.figuras.append(figura)

    def remover(self, figura):
        if figura in self.figuras:
            self.figuras.remove(figura)

    def desenhar(self, canvas):
        for figura in self.figuras:
            figura.desenhar(canvas)

    def contem_ponto(self, x, y):
        for figura in self.figuras:
            if figura.contem_ponto(x, y):
                return True
        return False

    def to_dict(self):
        return {
            "tipo": "FiguraComposta",
            "figuras": [figura.to_dict() for figura in self.figuras]
        }

    @classmethod
    def from_dict(cls, dados):
        mapeamento_classes = {
            "Linha": Linha,
            "Retangulo": Retangulo,
            "Oval": Oval,
            "Poligono": Poligono,
            "MaoLivre": MaoLivre,
            "FiguraComposta": FiguraComposta
        }
        figuras_carregadas = []
        for item in dados["figuras"]:
            tipo = item["tipo"]
            if tipo in mapeamento_classes:
                classe = mapeamento_classes[tipo]
                figuras_carregadas.append(classe.from_dict(item))
        return cls(figuras_carregadas)