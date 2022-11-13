import unittest
from robot import *


class TestGreetings(unittest.TestCase):
    
    def setUp(self):
        self.robot = start()
        
    
    def test_oi(self):
        greetings = ["oi", "eae", "ola", "olá", "alo", "tudo bem?", "tudo bom?", "td bem?", "td bom?"]
        
        for greeting in greetings:                    
            print(f"Verificando se o robô entende: {greeting}")
            
            answer = self.robot.get_response(greeting)
            self.assertGreaterEqual(answer.confidence, MINIMUM_CONFIDENCE)
            self.assertIn(
                "Ola, eu sou o robo de atendimento da COOMFAR! Estou a sua disposicao...",
                answer.text
            )
            
            
    def test_bom_dia(self):
        greetings = ["Bom dia", "Boa tarde", "Boa noite"]
        
        for greeting in greetings:                    
            print(f"Verificando se o robô entende: {greeting}")
            
            answer = self.robot.get_response(greeting.lower())
            self.assertGreaterEqual(answer.confidence, MINIMUM_CONFIDENCE)
            self.assertIn(
                greeting + "! Eu sou o robo de atendimento da COOMFAR! Estou a sua disposicao...",
                answer.text
            )
            
            
    def test_greetings_variability(self):
        greetings = ["Bom dia", "Boa tarde", "Boa noite"]
        
        for greeting in greetings:                    
            print(f"Verificando se o robô entende: {greeting}")
            
            answer = self.robot.get_response("oi, " + greeting.lower())
            self.assertGreaterEqual(answer.confidence, MINIMUM_CONFIDENCE)
            self.assertIn(
                greeting + "! Eu sou o robo de atendimento da COOMFAR! Estou a sua disposicao...",
                answer.text
            )
    
            
if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = unittest.TestSuite()
    
    tests.addTest(loader.loadTestsFromTestCase(TestGreetings))   
    
    executor = unittest.TextTestRunner()
    executor.run(tests)         