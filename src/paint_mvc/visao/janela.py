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
        
        self.canvas = tk.Canvas(self.root, bg='white', width=600, height=600)
        self.canvas.pack()