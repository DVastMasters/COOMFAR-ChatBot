from chatterbot import ChatBot
from difflib import SequenceMatcher

MINIMUM_CONFIDENCE = 0.50


def compare_messages(user_message, possible_message):
    confidence = 0.0
    
    user_msg = user_message.text    
    possible_msg = possible_message.text
    if user_msg and possible_message:
        confidence = SequenceMatcher(None,
                                     user_msg,
                                     possible_msg)
        confidence = round(confidence.ratio(), 2)
    
    return confidence


def start():
    robot = ChatBot("COOMFAR Robot",
                    read_only=True,
                    statement_comparion_function=compare_messages,
                    logic_adapters=[
                        {
                            "import_path": "chatterbot.logic.BestMatch"
                        }
                    ])
    
    return robot


def get_answer_from_question(robot, question):
    answer = robot.get_response(question.lower())
    if answer.confidence >= MINIMUM_CONFIDENCE:
        return answer.text
    else:
        return "Não entendi o que você disse. Tente escrever de outra forma ou perguntar outra coisa."