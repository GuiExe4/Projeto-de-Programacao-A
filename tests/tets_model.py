import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/paint_mvc')))

from modelo.figuras import Retangulo, Linha, MaoLivre

def test_criacao_retangulo():
    r = Retangulo(10, 20, 100, 200, "black", "blue")
    assert r.x1 == 10
    assert r.cor_preenchimento == "blue"

def test_serializacao_round_trip():
    r = Retangulo(10, 20, 100, 200, "black", "blue")
    dicionario = r.to_dict()
    nova_figura = Retangulo.from_dict(dicionario)
    assert nova_figura.x1 == 10
    assert nova_figura.cor_preenchimento == "blue"

  
