import random

StarQuestions = ["Tell me about your proudest professional achievement?", "Describe a situation where you overcame an obstacle?", "Describe a time when you had to work closely with different people?", "Describe a time when your team or company was going through a change and how you dealt with that?", "Tell me about a time you had to work closely with someone whos personality was different from yours?", "Tell me about a time you failed? How did you deal with the situation?", "tell me about a time your responsibilites became overwhelming and what did you do?","what role have you played in team situations?", "Describe a time when you achieved a goal you orginally thought out of reach?"]

otherQuestions = ["What motivates you?", "Why do you want to get into Tech?", "What is your passion outside of tech?", "Would you say your values align with that of the company?", "how do you deal with difficult tasks?", "Who's your hero?", "Whats your favourite saying?", "Why our company?", "Where do you see yourself in Ten Years?", "What is your approach to problem solving?", "What is your biggest weakness?"]

def randomQ(arr1, arr2):
  questionStar = random.choice(arr1)
  questionNormal = random.choice(arr2)

  questionOne = input(f"{questionStar}")
  file = open("starQuestionAnswers", "a")
  file.write(questionOne)
  file.close()

  questionTwo = input(f"Thanks so much, and {questionNormal}")
  file = open("otherQuestionsAnswers", "a")
  file.write(questionTwo)
  file.close()

randomQ(StarQuestions, otherQuestions)

