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