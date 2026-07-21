# Registro de Divisão de Tarefas - Paint MVC

Este documento detalha a identificação da equipe e a divisão de responsabilidades ao longo de todas as entregas do projeto, com base no histórico de contribuições do repositório.

---

## 👥 Identificação dos Integrantes

* **Guilherme Soares Oliveira**
  * GitHub: [@GuiExe4](https://github.com/GuiExe4)
  * Matrícula: 202500056451

* **Luiz Arthur de Almeida Macedo Silva**
  * GitHub: [@arthur2805749](https://github.com/arthur2805749)
  * Matrícula: 202200092745

* **João Victor Pereira Nascimento**
  * GitHub: [@JOA070](https://github.com/JOA070)
  * Matrícula: 202500056504

---

## 📋 Quadro de Contribuições por Entrega

### Entrega 1: Padrão Imperativo Inicial
* **Guilherme Soares Oliveira:** Subida inicial do código base, reestruturação para suportar retângulos e ovais (`main.py`) e ajustes de sintaxe para cores de borda e preenchimento.
* **Luiz Arthur de Almeida Macedo Silva:** Implementação do suporte a bordas coloridas nos desenhos individuais.

---

### Entrega 2: Refatoração para Orientação a Objetos (OO)
* **Guilherme Soares Oliveira:** Substituição do código imperativo por modelagem orientada a objetos, finalização da modularização e correção de bugs na execução do polígono e mão livre.
* **Luiz Arthur de Almeida Macedo Silva:** Criação inicial do arquivo `figuras.py` e implementação das classes de desenho para `Poligono` e `MaoLivre`.

---

### Entrega 3: Estruturação Arquitetural em MVC
* **Guilherme Soares Oliveira:** Refatoração e reestruturação do projeto para a arquitetura MVC (Model-View-Controller), organizando a árvore de diretórios no pacote `src/` (`modelo/`, `visao/` e `controlador/`).

---

### Entrega 4: Padrão State, Persistência JSON e Testes
* **Guilherme Soares Oliveira:** Implementação do padrão State para gerenciamento polimórfico de ferramentas no controlador, correções de salvar/abrir, criação do `.gitignore` e limpeza de cache do repositório.
* **Luiz Arthur de Almeida Macedo Silva:** Implementação dos métodos de serialização e desserialização (`to_dict`/`from_dict`) no modelo de figuras e criação dos botões de salvar/abrir na View.
* **João Victor Pereira Nascimento:** Criação e estruturação inicial da suíte de testes unitários para geometria e serialização das figuras na pasta `tests/`.

---

### Entrega 5: Seleção, Movimentação e Atalhos
* **Guilherme Soares Oliveira:** Implementação da seleção e movimentação de figuras pelo mouse, exclusão, alteração de cores e seleção múltipla com ações em lote.
* **Luiz Arthur de Almeida Macedo Silva:** Aprimoramento da manipulação de formas por atalhos de teclado e associação de navegação na View.

---

### Entrega 6: Padrão Composite (Agrupamento)
* **Guilherme Soares Oliveira:** Implementação da classe `FiguraComposta` seguindo o padrão estrutural Composite.
* **Luiz Arthur de Almeida Macedo Silva:** Adição dos botões de agrupar/desagrupar na interface e vinculação das ações no controlador.

---

### Entrega 7: Padrão Command (Undo / Redo)
* **Guilherme Soares Oliveira:** Criação do módulo `comandos.py` com as classes concretas do padrão Command para gerenciamento de Undo e Redo.
* **Luiz Arthur de Almeida Macedo Silva:** Integração das pilhas de Undo/Redo no controlador, adição dos botões de ação na View e vinculação dos atalhos de teclado (`Ctrl+Z` / `Ctrl+Y`).