import tkinter as tk

class JanelaPaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint MVC")

        self.frame_botoes = tk.Frame(self.root)
        self.frame_botoes.pack(fill=tk.X, padx=5, pady=5)

        self.btn_linha = tk.Button(self.frame_botoes, text="Linha")
        self.btn_linha.pack(side=tk.LEFT, padx=2)

        self.btn_retangulo = tk.Button(self.frame_botoes, text="Retângulo")
        self.btn_retangulo.pack(side=tk.LEFT, padx=2)

        self.btn_oval = tk.Button(self.frame_botoes, text="Oval")
        self.btn_oval.pack(side=tk.LEFT, padx=2)

        self.btn_poligono = tk.Button(self.frame_botoes, text="Polígono")
        self.btn_poligono.pack(side=tk.LEFT, padx=2)

        self.btn_mao_livre = tk.Button(self.frame_botoes, text="Mão Livre")
        self.btn_mao_livre.pack(side=tk.LEFT, padx=2)

        self.btn_selecionar = tk.Button(self.frame_botoes, text="Selecionar", bg="lightgray")
        self.btn_selecionar.pack(side=tk.LEFT, padx=10)

        self.btn_preto = tk.Button(self.frame_botoes, text="Preto")
        self.btn_preto.pack(side=tk.LEFT, padx=2)

        self.btn_vermelho = tk.Button(self.frame_botoes, text="Vermelho")
        self.btn_vermelho.pack(side=tk.LEFT, padx=2)

        self.btn_azul = tk.Button(self.frame_botoes, text="Azul")
        self.btn_azul.pack(side=tk.LEFT, padx=2)

        self.btn_amarelo = tk.Button(self.frame_botoes, text="Preench. Amarelo")
        self.btn_amarelo.pack(side=tk.LEFT, padx=2)

        self.btn_verde = tk.Button(self.frame_botoes, text="Preench. Verde")
        self.btn_verde.pack(side=tk.LEFT, padx=2)

        self.btn_cinza = tk.Button(self.frame_botoes, text="Preench. Cinza")
        self.btn_cinza.pack(side=tk.LEFT, padx=2)

        self.btn_salvar = tk.Button(self.frame_botoes, text="Salvar", bg="lightgreen")
        self.btn_salvar.pack(side=tk.RIGHT, padx=5)

        self.btn_abrir = tk.Button(self.frame_botoes, text="Abrir", bg="lightblue")
        self.btn_abrir.pack(side=tk.RIGHT, padx=5)

        self.canvas = tk.Canvas(self.root, bg='white', width=600, height=600)
        self.canvas.pack()

    def destacar_figura(self, figura):
        self.limpar_destaque()
        if not figura:
            return
            
        margem = 3
        
        if figura.__class__.__name__ == "MaoLivre" and figura.pontos:
            xs = [p[0] for p in figura.pontos]
            ys = [p[1] for p in figura.pontos]
            xmin, xmax = min(xs) - margem, max(xs) + margem
            ymin, ymax = min(ys) - margem, max(ys) + margem
        else:
            xmin = min(figura.x1, figura.x2) - margem
            xmax = max(figura.x1, figura.x2) + margem
            ymin = min(figura.y1, figura.y2) - margem
            ymax = max(figura.y1, figura.y2) + margem
        
        self.canvas.create_rectangle(
            xmin, ymin, xmax, ymax,
            outline="red",
            dash=(4, 4),
            tags="selecao"
        )

    def limpar_destaque(self):
        self.canvas.delete("selecao")