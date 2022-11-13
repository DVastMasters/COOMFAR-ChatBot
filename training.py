from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

ROBOT_KNOWLEDGE = [
    "knowledges/greetings.json",
    "knowledges/faq.json"
]

def start():
    robot = ChatBot("COOMFAR Robot")
    coach = ListTrainer(robot)
    
    return coach


def load_knowledges():
    knowledges = []
    
    for file_knowledge in ROBOT_KNOWLEDGE:
        with open(file_knowledge, "r", encoding='UTF-8') as file:
            knowledges_to_learn = json.load(file)
            knowledges.append(knowledges_to_learn["knowledges"])
            
            file.close()
            
    return knowledges


def learn(coach, knowledges):
    for knowledge in knowledges:
        for questions_answers in knowledge:
            questions = questions_answers["questions"]
            answer = questions_answers["answer"]
            
            print("Estou aprendendo algo novo, veja só...")
            print(f"Quando me perguntarem algo como: {questions}")
            print(f"Eu responderei: {answer}")
            for question in questions:
                coach.train([question, answer])
                
                
if __name__ == "__main__":
    coach = start()
    
    knowledges = load_knowledges()
    if knowledges:
        learn(coach, knowledges)