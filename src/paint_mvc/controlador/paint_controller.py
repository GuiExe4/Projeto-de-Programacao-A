import tkinter as tk
from modelo.figuras import Linha, Retangulo, Oval, Poligono, MaoLivre

class PaintController:
    def __init__(self, view):
        self.view = view
        
        self.ferramenta = "linha"
        self.cor_borda = "black"
        self.cor_preenchimento = "white"
        
        self.ini_x = None
        self.ini_y = None
        self.forma_mao_livre = None
        
        self.vincular_eventos()

    def vincular_eventos(self):
        self.view.btn_linha.config(command=lambda: self.mudar_ferramenta("linha"))
        self.view.btn_retangulo.config(command=lambda: self.mudar_ferramenta("retangulo"))
        self.view.btn_oval.config(command=lambda: self.mudar_ferramenta("oval"))
        self.view.btn_poligono.config(command=lambda: self.mudar_ferramenta("poligono"))
        self.view.btn_mao_livre.config(command=lambda: self.mudar_ferramenta("mao_livre"))
        
        self.view.btn_preto.config(command=lambda: self.mudar_cor_borda("black"))
        self.view.btn_vermelho.config(command=lambda: self.mudar_cor_borda("red"))
        self.view.btn_azul.config(command=lambda: self.mudar_cor_borda("blue"))
        
        self.view.btn_amarelo.config(command=lambda: self.mudar_preenchimento("yellow"))
        self.view.btn_verde.config(command=lambda: self.mudar_preenchimento("green"))
        self.view.btn_cinza.config(command=lambda: self.mudar_preenchimento("gray"))
        
        self.view.canvas.bind('<ButtonPress-1>', self.marca_inicio)
        self.view.canvas.bind('<B1-Motion>', self.atualiza_fim)

    def mudar_ferramenta(self, ferramenta):
        self.ferramenta = ferramenta

    def mudar_cor_borda(self, cor):
        self.cor_borda = cor

    def mudar_preenchimento(self, cor):
        self.cor_preenchimento = cor

    def marca_inicio(self, event):
        self.ini_x = event.x
        self.ini_y = event.y
        if self.ferramenta == "mao_livre":
            self.forma_mao_livre = MaoLivre(self.cor_borda)
            self.forma_mao_livre.adicionar_ponto(self.ini_x, self.ini_y)

    def atualiza_fim(self, event):
        fim_x = event.x
        fim_y = event.y
        
        self.view.canvas.delete("all")
        
        if self.ferramenta == "linha":
            forma = Linha(self.ini_x, self.ini_y, fim_x, fim_y, self.cor_borda, self.cor_preenchimento)
        elif self.ferramenta == "retangulo":
            forma = Retangulo(self.ini_x, self.ini_y, fim_x, fim_y, self.cor_borda, self.cor_preenchimento)
        elif self.ferramenta == "oval":
            forma = Oval(self.ini_x, self.ini_y, fim_x, fim_y, self.cor_borda, self.cor_preenchimento)
        elif self.ferramenta == "poligono":
            forma = Poligono(self.ini_x, self.ini_y, fim_x, fim_y, self.cor_borda, self.cor_preenchimento)
        elif self.ferramenta == "mao_livre":
            self.forma_mao_livre.adicionar_ponto(fim_x, fim_y)
            forma = self.forma_mao_livre
            
        forma.desenhar(self.view.canvas)