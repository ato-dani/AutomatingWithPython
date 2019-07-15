#! usr/bin/python3
# Python script for creating unique capital quiz test for 35(or any number of ) students.
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
   }
def question_writer(capital_keys, quiz_file, answer_file):
    for i in range(len(capital_keys)):
        correct_answer = capitals[capital_keys[i]]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(correct_answer)
        wrong_answers = random.sample(wrong_answers, 3)
        choices = wrong_answers + [correct_answer]
        random.shuffle(choices)
        letters = ["A", "B", "C", "D"]
        quiz_file.write("" + str((i+1)) +". What is the capital city of " + capital_keys[i] + "?\n")
        for j in range(len(choices)):
            #letters = ["A", "B", "C", "D"]
            quiz_file.write(" %s. %s\n" % (letters[j], choices[j]))
            if (choices[j] == correct_answer):
                answer_file.write("" + str((i + 1)) + ") " + letters[j]+ "\n")
            if (j == 3):
                quiz_file.write("\n")

num_quiz = int(input("How many students are taking the quiz?"))
for quiz_num in range(num_quiz):
    quiz_file = open("capitals_quiz%s.txt" % (quiz_num + 1), "w")
    answer_file = open("capitals_quiz_answers%s.txt" % (quiz_num + 1), "w")
    quiz_file.write("Name:\n\nClass:\n\nDate:\n\n")
    quiz_file.write((" " * 20) + "Quiz Captial Test Code %s\n" % (quiz_num + 1))
    capital_keys = list(capitals.keys())
    random.shuffle(capital_keys)
    question_writer(capital_keys, quiz_file, answer_file)
    quiz_file.close()
    answer_file.close()




