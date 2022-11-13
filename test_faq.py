import unittest
from robot import *


class TestFaq(unittest.TestCase):
    
    def setUp(self):
        self.robot = start()
        
    
    def test_o_que_e_uma_cooperativa(self):
        questions = ["o que é uma cooperativa?", "o que seria uma cooperativa?", "do que se trata uma cooperativa?", "explique o que é uma cooperativa"]
        
        for question in questions:                    
            print(f"Verificando se o robô entende: {question}")
            
            answer = self.robot.get_response(question)
            self.assertGreaterEqual(answer.confidence, MINIMUM_CONFIDENCE)
            self.assertIn(
                "Uma cooperativa e um agrupamento de pessoas com o mesmo objetivo.",
                answer.text
            )
            
            
    def test_o_que_significa_coomfar(self):
        questions = ["o que significa a sigla coomfar?", "o que é coomfar?", "qual o significado de coomfar?", "o que seria coomfar?"]
        
        for question in questions:                    
            print(f"Verificando se o robô entende: {question}")
            
            answer = self.robot.get_response(question)
            self.assertGreaterEqual(answer.confidence, MINIMUM_CONFIDENCE)
            self.assertIn(
                "Cooperativa Mista dos Produtores e Produtoras da Agricultura Familiar do Municipio de Presidente Janio Quadros e Regiao.",
                answer.text
            )
            
            
    def test_coomfar_localizacao(self):
        questions = ["onde a coomfar está localizada?", "onde fica a coomfar?", "onde eu encontro a coomfar?", "qual o endereço da coomfar?", "onde fica a loja da coomfar?"]
        
        for question in questions:                    
            print(f"Verificando se o robô entende: {question}")
            
            answer = self.robot.get_response(question)
            self.assertGreaterEqual(answer.confidence, MINIMUM_CONFIDENCE)
            self.assertIn(
                "Praça Jose Viana dos Santos - Vila Elisa.",
                answer.text
            )
                    
    
    def test_atuais_coperados(self):
        questions = ["quais são os atuais cooperados da coomfar?", "quem são os cooperados da coomfar?", "quais são os cooperados da coomfar?", "como se chama os cooperados da coomfar?", "qual o nome dos cooperados da coomfar?"]
        
        for question in questions:                    
            print(f"Verificando se o robô entende: {question}")
            
            answer = self.robot.get_response(question)
            self.assertGreaterEqual(answer.confidence, MINIMUM_CONFIDENCE)
            self.assertIn(
                "Ana Paula Pereira, Karen Duarte, Ana dias Vieira, Aparecida Vieira, Maria do Carmo Aguiar, Célia Matos e mais 39 pessoas. Confira a lista completa em nosso site.",
                answer.text
            )
                    
    
    def test_como_virar_coperado(self):
        questions = ["como eu me torno um cooperado?", "como faço pra me juntar a coomfar?", "como participar da cooperativa?", "como participar da coomfar?", "como eu entro na coomfar?"]
        
        for question in questions:                    
            print(f"Verificando se o robô entende: {question}")
            
            answer = self.robot.get_response(question)
            self.assertGreaterEqual(answer.confidence, MINIMUM_CONFIDENCE)
            self.assertIn(
                "E necessario passar por uma capacitacão que e dada pelo cooperados veteranos. Caso tenha interesse, venha pessoalmente ate a loja da COOMFAR.",
                answer.text
            )
                    
    
    def test_quais_produtos_produz(self):
        questions = ["quais produtos a coomfar produz?", "quais tipos de produtos tem na coomfar?", "o que a coomfar produz?", "liste os tipos de produtos da coomfar"]
        
        for question in questions:                    
            print(f"Verificando se o robô entende: {question}")
            
            answer = self.robot.get_response(question)
            self.assertGreaterEqual(answer.confidence, MINIMUM_CONFIDENCE)
            self.assertIn(
                "No momento, produzimos os seguintes tipos de produtos: Hortalicas, Frutas, Graos e Derivados de mandioca",
                answer.text
            )
                    
    
    def test_quais_produtos_vende(self):
        questions = ["quais produtos estão disponíveis para venda no momento?", "tá vendendo o que?", "o que tem pra vender?", "liste os produtos que estão a venda"]
        
        for question in questions:                    
            print(f"Verificando se o robô entende: {question}")
            
            answer = self.robot.get_response(question)
            self.assertGreaterEqual(answer.confidence, MINIMUM_CONFIDENCE)
            self.assertIn(
                "No momento, temos os seguintes produtos disponíveis para venda: Abobora, Feijao catador, Farinha, Rapadura, Puba, Mel, Couve e Tempero caseiro. Caso tenha interesse, visite nossa loja.",
                answer.text
            )
    
            
if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = unittest.TestSuite()
    
    tests.addTest(loader.loadTestsFromTestCase(TestFaq))   
    
    executor = unittest.TextTestRunner()
    executor.run(tests)         