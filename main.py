import tkinter as tk

class Figura:
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def desenhar(self, canvas):
        pass

class Linha(Figura):
    def desenhar(self, canvas):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2,
            fill=self.cor_borda
        )

class Retangulo(Figura):
    def desenhar(self, canvas):
        canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2,
            outline=self.cor_borda,
            fill=self.cor_preenchimento
        )

class Oval(Figura):
    def desenhar(self, canvas):
        canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2,
            outline=self.cor_borda,
            fill=self.cor_preenchimento
        )

def marca_inicio(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

def atualiza_fim(event):
    global fim_x, fim_y
    fim_x = event.x
    fim_y = event.y
    
    canvas.delete("all")
    
    if ferramenta == "linha":
        forma = Linha(ini_x, ini_y, fim_x, fim_y, cor_borda, cor_preenchimento)
    elif ferramenta == "retangulo":
        forma = Retangulo(ini_x, ini_y, fim_x, fim_y, cor_borda, cor_preenchimento)
    elif ferramenta == "oval":
        forma = Oval(ini_x, ini_y, fim_x, fim_y, cor_borda, cor_preenchimento)
        
    forma.desenhar(canvas)

def usar_linha():
    global ferramenta
    ferramenta = "linha"

def usar_retangulo():
    global ferramenta
    ferramenta = "retangulo"

def usar_oval():
    global ferramenta
    ferramenta = "oval"

def usar_preto():
    global cor_borda
    cor_borda = "black"

def usar_vermelho():
    global cor_borda
    cor_borda = "red"

def usar_azul():
    global cor_borda
    cor_borda = "blue"

def usar_amarelo():
    global cor_preenchimento
    cor_preenchimento = "yellow"

def usar_verde():
    global cor_preenchimento
    cor_preenchimento = "green"

def usar_cinza():
    global cor_preenchimento
    cor_preenchimento = "gray"

root = tk.Tk()
root.title("Paint OO")

frame_botoes = tk.Frame(root)
frame_botoes.pack(fill=tk.X, padx=5, pady=5)

btn_linha = tk.Button(frame_botoes, text="Linha", command=usar_linha)
btn_linha.pack(side=tk.LEFT, padx=2)

btn_retangulo = tk.Button(frame_botoes, text="Retângulo", command=usar_retangulo)
btn_retangulo.pack(side=tk.LEFT, padx=2)

btn_oval = tk.Button(frame_botoes, text="Oval", command=usar_oval)
btn_oval.pack(side=tk.LEFT, padx=2)

btn_preto = tk.Button(frame_botoes, text="Preto", command=usar_preto)
btn_preto.pack(side=tk.LEFT, padx=2)

btn_vermelho = tk.Button(frame_botoes, text="Vermelho", command=usar_vermelho)
btn_vermelho.pack(side=tk.LEFT, padx=2)

btn_azul = tk.Button(frame_botoes, text="Azul", command=usar_azul)
btn_azul.pack(side=tk.LEFT, padx=2)

btn_amarelo = tk.Button(frame_botoes, text="Preench. Amarelo", command=usar_amarelo)
btn_amarelo.pack(side=tk.LEFT, padx=2)

btn_verde = tk.Button(frame_botoes, text="Preench. Verde", command=usar_verde)
btn_verde.pack(side=tk.LEFT, padx=2)

btn_cinza = tk.Button(frame_botoes, text="Preench. Cinza", command=usar_cinza)
btn_cinza.pack(side=tk.LEFT, padx=2)

canvas = tk.Canvas(root, bg='white', width=600, height=600)
canvas.pack()

ferramenta = "linha"
cor_borda = "black"
cor_preenchimento = "white"

ini_x = None
ini_y = None
fim_x = None
fim_y = None

canvas.bind('<ButtonPress-1>', marca_inicio)
canvas.bind('<B1-Motion>', atualiza_fim)

root.mainloop()