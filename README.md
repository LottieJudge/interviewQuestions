# Random Question Generator 

This Python script generates two random interview-style questions: one from a set of STAR (Situation, Task, Action, Result) questions and one from a set of more general questions. It collects user input for both questions and saves the answers in separate text files so you can use them to refer back to. 

## Features
- Randomly selects one STAR question and one general question.
- Collects user input for each question.
- Saves the answers in two separate text files:
  - `starQuestionAnswers.txt` for STAR question answers.
  - `otherQuestionsAnswers.txt` for general question answers.

## How It Works
1. The script contains two arrays:
   - `StarQuestions`: A list of STAR interview questions.
   - `otherQuestions`: A list of general questions.
2. The `randomQ()` function selects a random question from each list.
3. The script asks the user to answer both questions.
4. The answers are written to two separate files: `starQuestionAnswers.txt` and `otherQuestionsAnswers.txt`.

## Requirements
- Python 3.x

## Usage
1. Clone the repository or download the script.
2. Run the script in a Python environment:
   ```bash
   python random_question_generator.py
