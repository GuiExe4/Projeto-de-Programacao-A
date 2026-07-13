import tkinter as tk
from modelo.figuras import Linha, Retangulo, Oval, Poligono, MaoLivre

class EstadoFerramenta:
    def clicar(self, controller, event):
        pass
    def arrastar(self, controller, event):
        pass

class EstadoLinha(EstadoFerramenta):
    def clicar(self, controller, event):
        controller.ini_x, controller.ini_y = event.x, event.y
    def arrastar(self, controller, event):
        canvas = controller.view.canvas
        canvas.delete("all")
        forma = Linha(controller.ini_x, controller.ini_y, event.x, event.y, controller.cor_borda, controller.cor_preenchimento)
        forma.desenhar(canvas)

class EstadoRetangulo(EstadoFerramenta):
    def clicar(self, controller, event):
        controller.ini_x, controller.ini_y = event.x, event.y
    def arrastar(self, controller, event):
        canvas = controller.view.canvas
        canvas.delete("all")
        forma = Retangulo(controller.ini_x, controller.ini_y, event.x, event.y, controller.cor_borda, controller.cor_preenchimento)
        forma.desenhar(canvas)

class EstadoOval(EstadoFerramenta):
    def clicar(self, controller, event):
        controller.ini_x, controller.ini_y = event.x, event.y
    def arrastar(self, controller, event):
        canvas = controller.view.canvas
        canvas.delete("all")
        forma = Oval(controller.ini_x, controller.ini_y, event.x, event.y, controller.cor_borda, controller.cor_preenchimento)
        forma.desenhar(canvas)

class EstadoPoligono(EstadoFerramenta):
    def clicar(self, controller, event):
        controller.ini_x, controller.ini_y = event.x, event.y
    def arrastar(self, controller, event):
        canvas = controller.view.canvas
        canvas.delete("all")
        forma = Poligono(controller.ini_x, controller.ini_y, event.x, event.y, controller.cor_borda, controller.cor_preenchimento)
        forma.desenhar(canvas)

class EstadoMaoLivre(EstadoFerramenta):
    def clicar(self, controller, event):
        controller.forma_mao_livre = MaoLivre(controller.cor_borda)
        controller.forma_mao_livre.adicionar_ponto(event.x, event.y)
    def arrastar(self, controller, event):
        canvas = controller.view.canvas
        canvas.delete("all")
        controller.forma_mao_livre.adicionar_ponto(event.x, event.y)
        controller.forma_mao_livre.desenhar(canvas)

class PaintController:
    def __init__(self, view):
        self.view = view
        self.cor_borda = "black"
        self.cor_preenchimento = "white"
        self.ini_x = None
        self.ini_y = None
        self.forma_mao_livre = None
        
        self.estado_atual = EstadoLinha()
        self.vincular_eventos()

    def vincular_eventos(self):
        self.view.btn_linha.config(command=lambda: self.definir_estado(EstadoLinha()))
        self.view.btn_retangulo.config(command=lambda: self.definir_estado(EstadoRetangulo()))
        self.view.btn_oval.config(command=lambda: self.definir_estado(EstadoOval()))
        self.view.btn_poligono.config(command=lambda: self.definir_estado(EstadoPoligono()))
        self.view.btn_mao_livre.config(command=lambda: self.definir_estado(EstadoMaoLivre()))
        
        self.view.btn_preto.config(command=lambda: self.mudar_cor_borda("black"))
        self.view.btn_vermelho.config(command=lambda: self.mudar_cor_borda("red"))
        self.view.btn_azul.config(command=lambda: self.mudar_cor_borda("blue"))
        
        self.view.btn_amarelo.config(command=lambda: self.mudar_preenchimento("yellow"))
        self.view.btn_verde.config(command=lambda: self.mudar_preenchimento("green"))
        self.view.btn_cinza.config(command=lambda: self.mudar_preenchimento("gray"))
        
        self.view.canvas.bind('<ButtonPress-1>', self.marca_inicio)
        self.view.canvas.bind('<B1-Motion>', self.atualiza_fim)

    def definir_estado(self, estado):
        self.estado_atual = estado

    def mudar_cor_borda(self, cor):
        self.cor_borda = cor

    def mudar_preenchimento(self, cor):
        self.cor_preenchimento = cor

    def marca_inicio(self, event):
        self.estado_atual.clicar(self, event)

    def atualiza_fim(self, event):
        self.estado_atual.arrastar(self, event)