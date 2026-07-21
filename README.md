# Paint MVC - Projeto de Programação

Aplicação de desenho vetorial (Paint) desenvolvida em Python e Tkinter utilizando o padrão arquitetural **MVC (Model-View-Controller)** e diversos padrões de projeto para a disciplina de Programação.

---

## Como Executar o Projeto

### Pré-requisitos
* Python 3.8 ou superior instalado na máquina.
* Interface gráfica nativa (Tkinter já vem instalado por padrão no Python).

### Passo a Passo

1. Clonar o repositório:
git clone https://github.com/GuiExe4/Projeto-de-Programacao-A.git
cd Projeto-de-Programacao-A

2. Executar a aplicação:
python src/paint_mvc/main.py

---

## Arquitetura do Sistema (MVC)

O projeto está estruturado na pasta src/paint_mvc/ dividindo as responsabilidades de forma clara:

* Model (modelo/figuras.py, modelo/comandos.py): Contém as classes que representam os dados geométricos (Linha, Retângulo, Oval, Polígono, Mão Livre, Figura Composta) e a representação das ações do usuário em forma de comandos.
* View (visao/janela.py): Responsável exclusivamente pela interface gráfica criada com Tkinter (botões, atalhos de teclado e área de canvas).
* Controller (controlador/paint_controller.py): Atua como intermediário entre a View e o Model. Gerencia os eventos de clique/arraste, altera os estados ativos, executa os comandos de edição e atualiza o redesenho no Canvas.

---

## Padrões de Projeto Aplicados

1. State Pattern (Entrega 4): Gerenciamento polimórfico das ferramentas ativas (Linha, Retângulo, Oval, Polígono, Mão Livre, Selecionar), eliminando estruturas condicionais excessivas nos eventos de mouse.
2. Composite Pattern (Entrega 6): Agrupamento recursivo de figuras simples em uma FiguraComposta, permitindo que o grupo seja movido, colorido, salvo e restaurado como uma única forma polimórfica.
3. Command Pattern (Entrega 7): Empacotamento das operações do usuário (criar, mover, apagar, alterar cor, agrupar e desagrupar) em objetos de comando independentes com suporte às operações de Undo e Redo gerenciadas por pilhas no controlador.

---

## Funcionalidades

* Desenho de Formas: Linha, Retângulo, Oval, Polígono dinâmico e Desenho Livre.
* Seleção e Edição: Seleção simples e múltipla (utilizando a tecla Shift), movimentação pela tela com o mouse, alteração de cor de borda e preenchimento.
* Agrupamento: Agrupar e Desagrupar figuras.
* Gerenciamento de Camadas: Enviar figuras selecionadas para a frente ou para trás.
* Cópia e Colagem: Suporte a Ctrl+C e Ctrl+V para duplicar elementos.
* Persistência de Dados: Salvamento e carregamento completo do desenho em arquivos .json.
* Histórico de Ações: Operações de Desfazer (Ctrl+Z) e Refazer (Ctrl+Y).