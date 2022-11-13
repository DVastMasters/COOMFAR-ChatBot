from robot import *
from flask import Flask

robot = start()
robot_service = Flask(__name__)

@robot_service.route("/answer/<question>")
def get_answer(question):
    answer = get_answer_from_question(robot, question)
    
    return answer


if __name__ == "__main__":
    robot_service.run()