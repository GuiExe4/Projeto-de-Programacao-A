import tkinter as tk

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
        canvas.create_line(
            ini_x, ini_y, fim_x, fim_y
             fill=cor_borda
         )
    elif ferramenta == "retangulo":
        canvas.create_rectangle(
            ini_x, ini_y, fim_x, fim_y
            outline=cor_borda
        )
    elif ferramenta == "oval":
        canvas.create_oval(
            ini_x, ini_y, fim_x, fim_y
            outline=cor_borda
        )

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

root = tk.Tk()
root.title("Paint")

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

canvas = tk.Canvas(root, bg='white', width=600, height=600)
canvas.pack()

ferramenta = "linha"
cor_borda = "black"

ini_x = None
ini_y = None
fim_x = None
fim_y = None

canvas.bind('<ButtonPress-1>', marca_inicio)
canvas.bind('<B1-Motion>', atualiza_fim)

root.mainloop()
