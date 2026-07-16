import tkinter as tk
import json
from tkinter import filedialog
from modelo.figuras import Linha, Retangulo, Oval, Poligono, MaoLivre, FiguraComposta

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
        shift_pressionado = bool(event.state & 0x0001)
        
        figura_clicada = None
        for figura in reversed(controller.self_historico_figuras):
            if figura.contem_ponto(event.x, event.y):
                figura_clicada = figura
                break
        
        if shift_pressionado:
            if figura_clicada:
                if figura_clicada in controller.figuras_selecionadas:
                    controller.figuras_selecionadas.remove(figura_clicada)
                else:
                    controller.figuras_selecionadas.append(figura_clicada)
        else:
            if figura_clicada:
                if figura_clicada not in controller.figuras_selecionadas:
                    controller.figuras_selecionadas = [figura_clicada]
            else:
                controller.figuras_selecionadas = []
                
        controller.ultimo_x = event.x
        controller.ultimo_y = event.y
        controller.redesenhar_todos()

    def arrastar(self, controller, event):
        if controller.figuras_selecionadas:
            dx = event.x - controller.ultimo_x
            dy = event.y - controller.ultimo_y
            
            for figura in controller.figuras_selecionadas:
                if figura.__class__.__name__ == "MaoLivre":
                    nova_lista = []
                    for px, py in figura.pontos:
                        nova_lista.append((px + dx, py + dy))
                    figura.pontos = nova_lista
                elif figura.__class__.__name__ == "FiguraComposta":
                    for sub_figura in figura.figuras:
                        if sub_figura.__class__.__name__ == "MaoLivre":
                            sub_figura.pontos = [(px + dx, py + dy) for px, py in sub_figura.pontos]
                        else:
                            sub_figura.x1 += dx
                            sub_figura.y1 += dy
                            sub_figura.x2 += dx
                            sub_figura.y2 += dy
                else:
                    figura.x1 += dx
                    figura.y1 += dy
                    figura.x2 += dx
                    figura.y2 += dy
            
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
        self.figuras_selecionadas = []
        self.ultimo_x = 0
        self.ultimo_y = 0
        self.area_transferencia = []

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
        self.view.btn_agrupar.config(command=self.agrupar_figuras)
        self.view.btn_desagrupar.config(command=self.desagrupar_figuras)
        self.view.btn_apagar.config(command=self.apagar_figura_selecionada)
        self.view.btn_frente.config(command=self.trazer_para_frente)
        self.view.btn_tras.config(command=self.enviar_para_tras)

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
        
        self.view.vincular_teclado("<Delete>", self.apagar_figura_por_teclado)
        self.view.vincular_teclado("<Control-c>", self.copiar_figura)
        self.view.vincular_teclado("<Control-C>", self.copiar_figura)
        self.view.vincular_teclado("<Control-v>", self.colar_figura)
        self.view.vincular_teclado("<Control-V>", self.colar_figura)

    def definir_estado(self, estado):
        self.estado_atual = estado
        if not isinstance(estado, EstadoSelecionar):
            self.figuras_selecionadas = []
            self.redesenhar_todos()

    def mudar_cor_borda(self, cor):
        self.cor_borda = cor
        for figura in self.figuras_selecionadas:
            figura.cor_borda = cor
        self.redesenhar_todos()

    def mudar_preenchimento(self, cor):
        self.cor_preenchimento = cor
        for figura in self.figuras_selecionadas:
            figura.cor_preenchimento = cor
        self.redesenhar_todos()

    def apagar_figura_selecionada(self):
        for figura in list(self.figuras_selecionadas):
            if figura in self.self_historico_figuras:
                self.self_historico_figuras.remove(figura)
        self.figuras_selecionadas = []
        self.redesenhar_todos()

    def apagar_figura_por_teclado(self, event):
        self.apagar_figura_selecionada()
    
    def agrupar_figuras(self):
        if len(self.figuras_selecionadas) > 1:
            nova_composta = FiguraComposta()
            for figura in list(self.figuras_selecionadas):
                if figura in self.self_historico_figuras:
                    self.self_historico_figuras.remove(figura)
                nova_composta.adicionar(figura)
            self.self_historico_figuras.append(nova_composta)
            self.figuras_selecionadas = [nova_composta]
            self.redesenhar_todos()

    def desagrupar_figuras(self):
        novas_selecionadas = []
        for figura in list(self.figuras_selecionadas):
            if isinstance(figura, FiguraComposta):
                if figura in self.self_historico_figuras:
                    self.self_historico_figuras.remove(figura)
                for sub_figura in figura.figuras:
                    self.self_historico_figuras.append(sub_figura)
                    novas_selecionadas.append(sub_figura)
        if novas_selecionadas:
            self.figuras_selecionadas = novas_selecionadas
            self.redesenhar_todos()
    
    def copiar_figura(self, event):
        if self.figuras_selecionadas:
            self.area_transferencia = [figura.to_dict() for figura in self.figuras_selecionadas]

    def colar_figura(self, event):
        if self.area_transferencia:
            mapeamento_classes = {
                "Linha": Linha,
                "Retangulo": Retangulo,
                "Oval": Oval,
                "Poligono": Poligono,
                "MaoLivre": MaoLivre
                "FiguraComposta": FiguraComposta
            }
            novas_selecionadas = []
            for item in self.area_transferencia:
                tipo = item["tipo"]
                if tipo in mapeamento_classes:
                    classe = mapeamento_classes[tipo]
                    nova_figura = classe.from_dict(item)
                    
                    deslocamento = 15
                    if tipo == "MaoLivre":
                        nova_figura.pontos = [(px + deslocamento, py + deslocamento) for px, py in nova_figura.pontos]
                    elif tipo == "FiguraComposta":
                        for sub in nova_figura.figuras:
                            if sub.__class__.__name__ == "MaoLivre":
                                sub.pontos = [(px + deslocamento, py + deslocamento) for px, py in sub.pontos]
                            else:
                                sub.x1 += deslocamento
                                sub.y1 += deslocamento
                                sub.x2 += deslocamento
                                sub.y2 += deslocamento
                    else:
                        nova_figura.x1 += deslocamento
                        nova_figura.y1 += deslocamento
                        nova_figura.x2 += deslocamento
                        nova_figura.y2 += deslocamento
                    
                    self.self_historico_figuras.append(nova_figura)
                    novas_selecionadas.append(nova_figura)
            
            self.figuras_selecionadas = novas_selecionadas
            self.redesenhar_todos()

    def trazer_para_frente(self):
        for figura in list(self.figuras_selecionadas):
            if figura in self.self_historico_figuras:
                self.self_historico_figuras.remove(figura)
                self.self_historico_figuras.append(figura)
        self.redesenhar_todos()

    def enviar_para_tras(self):
        for figura in reversed(list(self.figuras_selecionadas)):
            if figura in self.self_historico_figuras:
                self.self_historico_figuras.remove(figura)
                self.self_historico_figuras.insert(0, figura)
        self.redesenhar_todos()

    def marca_inicio(self, event):
        self.view.canvas.focus_set()
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
        if isinstance(self.estado_atual, EstadoSelecionar):
            self.view.destacar_figuras(self.figuras_selecionadas)

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
            self.figuras_selecionadas = []
            
            mapeamento_classes = {
                "Linha": Linha,
                "Retangulo": Retangulo,
                "Oval": Oval,
                "Poligono": Poligono,
                "MaoLivre": MaoLivre
                "FiguraComposta": FiguraComposta
            }

            for data in lista_dicts:
                tipo = data["tipo"]
                if tipo in mapeamento_classes:
                    classe = mapeamento_classes[tipo]
                    self.self_historico_figuras.append(classe.from_dict(data))

            self.redesenhar_todos()
