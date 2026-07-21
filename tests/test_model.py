import unittest
from src.paint_mvc.modelo.figuras import Retangulo, Oval, FiguraComposta
from src.paint_mvc.modelo.comandos import ComandoAdicionar, ComandoMover

class ControllerMock:
    def __init__(self):
        self.self_historico_figuras = []
        self.figuras_selecionadas = []

class TestPaintModelo(unittest.TestCase):

    def test_geometria_e_selecao(self):
        ret = Retangulo(10, 10, 50, 50, "black", "red")
        self.assertTrue(ret.contem_ponto(20, 20))
        self.assertFalse(ret.contem_ponto(100, 100))

    def test_serializacao_json(self):
        ret = Retangulo(10, 10, 50, 50, "black", "red")
        dicionario = ret.to_dict()
        ret_recriado = Retangulo.from_dict(dicionario)
        self.assertEqual(ret.x1, ret_recriado.x1)
        self.assertEqual(ret.cor_preenchimento, ret_recriado.cor_preenchimento)

    def test_composite_entrega_6(self):
        r1 = Retangulo(0, 0, 10, 10, "black", "white")
        r2 = Oval(20, 20, 30, 30, "black", "white")
        grupo = FiguraComposta([r1, r2])
        
        self.assertEqual(len(grupo.figuras), 2)
        self.assertIn(r1, grupo.figuras)
        self.assertIn(r2, grupo.figuras)

    def test_command_adicionar_desfazer(self):
        controller = ControllerMock()
        ret = Retangulo(0, 0, 10, 10, "black", "white")
        
        cmd = ComandoAdicionar(controller, ret)
        cmd.executar()
        self.assertIn(ret, controller.self_historico_figuras)

        cmd.desfazer()
        self.assertNotIn(ret, controller.self_historico_figuras)

    def test_command_mover(self):
        controller = ControllerMock()
        ret = Retangulo(10, 10, 50, 50, "black", "white")
        
        cmd = ComandoMover(controller, [ret], 10, 10)
        cmd.executar()
        self.assertEqual(ret.x1, 20)
        
        cmd.desfazer()
        self.assertEqual(ret.x1, 10)

if __name__ == "__main__":
    unittest.main()