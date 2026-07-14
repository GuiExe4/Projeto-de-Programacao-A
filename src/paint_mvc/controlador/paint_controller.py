import tkinter as tk
import json
from tkinter import filedialog
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
        controller.redesenhar_todos()
        forma = Linha(controller.ini_x, controller.ini_y, event.x, event.y, controller.cor_borda, controller.cor_preenchimento)
        forma.desenhar(canvas)
        controller.forma_temporaria = forma

class EstadoRetangulo(EstadoFerramenta):
    def clicar(self, controller, event):
        controller.ini_x, controller.ini_y = event.x, event.y
    def arrastar(self, controller, event):
        canvas = controller.view.canvas
        controller.redesenhar_todos()
        forma = Retangulo(controller.ini_x, controller.ini_y, event.x, event.y, controller.cor_borda, controller.cor_preenchimento)
        forma.desenhar(canvas)
        controller.forma_temporaria = forma

class EstadoOval(EstadoFerramenta):
    def clicar(self, controller, event):
        controller.ini_x, controller.ini_y = event.x, event.y
    def arrastar(self, controller, event):
        canvas = controller.view.canvas
        controller.redesenhar_todos()
        forma = Oval(controller.ini_x, controller.ini_y, event.x, event.y, controller.cor_borda, controller.cor_preenchimento)
        forma.desenhar(canvas)
        controller.forma_temporaria = forma

class EstadoPoligono(EstadoFerramenta):
    def clicar(self, controller, event):
        controller.ini_x, controller.ini_y = event.x, event.y
    def arrastar(self, controller, event):
        canvas = controller.view.canvas
        controller.redesenhar_todos()
        forma = Poligono(controller.ini_x, controller.ini_y, event.x, event.y, controller.cor_borda, controller.cor_preenchimento)
        forma.desenhar(canvas)
        controller.forma_temporaria = forma

class EstadoMaoLivre(EstadoFerramenta):
    def clicar(self, controller, event):
        controller.forma_mao_livre = MaoLivre(controller.cor_borda)
        controller.forma_mao_livre.adicionar_ponto(event.x, event.y)
    def arrastar(self, controller, event):
        canvas = controller.view.canvas
        controller.redesenhar_todos()
        controller.forma_mao_livre.adicionar_ponto(event.x, event.y)
        controller.forma_mao_livre.desenhar(canvas)
        controller.forma_temporaria = controller.forma_mao_livre

class EstadoSelecionar(EstadoFerramenta):
    def clicar(self, controller, event):
        controller.figura_selecionada = None
        for figura in reversed(controller.self_historico_figuras):
            if figura.contem_ponto(event.x, event.y):
                controller.figura_selecionada = figura
                controller.ultimo_x = event.x
                controller.ultimo_y = event.y
                break
        controller.redesenhar_todos()

    def arrastar(self, controller, event):
        if controller.figura_selecionada:
            dx = event.x - controller.ultimo_x
            dy = event.y - controller.ultimo_y
            
            if controller.figura_selecionada.__class__.__name__ == "MaoLivre":
                nova_lista = []
                for px, py in controller.figura_selecionada.pontos:
                    nova_lista.append((px + dx, py + dy))
                controller.figura_selecionada.pontos = nova_lista
            else:
                controller.figura_selecionada.x1 += dx
                controller.figura_selecionada.y1 += dy
                controller.figura_selecionada.x2 += dx
                controller.figura_selecionada.y2 += dy
            
            controller.ultimo_x = event.x
            controller.ultimo_y = event.y
            controller.redesenhar_todos()

class PaintController:
    def __init__(self, view):
        self.view = view
        self.cor_borda = "black"
        self.cor_preenchimento = "white"
        self.ini_x = None
        self.ini_y = None
        self.forma_mao_livre = None
        self.forma_temporaria = None
        self.figura_selecionada = None
        self.ultimo_x = 0
        self.ultimo_y = 0

        self.self_historico_figuras = []
        self.estado_atual = EstadoLinha()
        self.vincular_eventos()

    def vincular_eventos(self):
        self.view.btn_linha.config(command=lambda: self.definir_estado(EstadoLinha()))
        self.view.btn_retangulo.config(command=lambda: self.definir_estado(EstadoRetangulo()))
        self.view.btn_oval.config(command=lambda: self.definir_estado(EstadoOval()))
        self.view.btn_poligono.config(command=lambda: self.definir_estado(EstadoPoligono()))
        self.view.btn_mao_livre.config(command=lambda: self.definir_estado(EstadoMaoLivre()))
        self.view.btn_selecionar.config(command=lambda: self.definir_estado(EstadoSelecionar()))

        self.view.btn_preto.config(command=lambda: self.mudar_cor_borda("black"))
        self.view.btn_vermelho.config(command=lambda: self.mudar_cor_borda("red"))
        self.view.btn_azul.config(command=lambda: self.mudar_cor_borda("blue"))

        self.view.btn_amarelo.config(command=lambda: self.mudar_preenchimento("yellow"))
        self.view.btn_verde.config(command=lambda: self.mudar_preenchimento("green"))
        self.view.btn_cinza.config(command=lambda: self.mudar_preenchimento("gray"))

        self.view.btn_salvar.config(command=self.salvar_desenho)
        self.view.btn_abrir.config(command=self.abrir_desenho)

        self.view.canvas.bind('<ButtonPress-1>', self.marca_inicio)
        self.view.canvas.bind('<B1-Motion>', self.atualiza_fim)
        self.view.canvas.bind('<ButtonRelease-1>', self.solta_clique)

    def definir_estado(self, estado):
        self.estado_atual = estado
        if not isinstance(estado, EstadoSelecionar):
            self.figura_selecionada = None
            self.redesenhar_todos()

    def mudar_cor_borda(self, cor):
        self.cor_borda = cor

    def mudar_preenchimento(self, cor):
        self.cor_preenchimento = cor

    def marca_inicio(self, event):
        self.forma_temporaria = None
        self.estado_atual.clicar(self, event)

    def atualiza_fim(self, event):
        self.estado_atual.arrastar(self, event)

    def solta_clique(self, event):
        if self.forma_temporaria:
            self.self_historico_figuras.append(self.forma_temporaria)
            self.forma_temporaria = None

    def redesenhar_todos(self):
        self.view.canvas.delete("all")
        for forma in self.self_historico_figuras:
            forma.desenhar(self.view.canvas)
        if self.figura_selecionada and isinstance(self.estado_atual, EstadoSelecionar):
            self.view.destacar_figura(self.figura_selecionada)

    def salvar_desenho(self):
        caminho = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if caminho:
            lista_dicts = [forma.to_dict() for forma in self.self_historico_figuras]
            with open(caminho, 'w') as f:
                json.dump(lista_dicts, f)

    def abrir_desenho(self):
        caminho = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if caminho:
            with open(caminho, 'r') as f:
                lista_dicts = json.load(f)

            self.self_historico_figuras.clear()
            self.figura_selecionada = None
            
            mapeamento_classes = {
                "Linha": Linha,
                "Retangulo": Retangulo,
                "Oval": Oval,
                "Poligono": Poligono,
                "MaoLivre": MaoLivre
            }

            for data in lista_dicts:
                tipo = data["tipo"]
                if tipo in mapeamento_classes:
                    classe = mapeamento_classes[tipo]
                    self.self_historico_figuras.append(classe.from_dict(data))

            self.redesenhar_todos()