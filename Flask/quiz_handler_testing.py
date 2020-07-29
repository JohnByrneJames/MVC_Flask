import json
import random

class QuizCreator:
    questions_all = None
    questions_QA = {}
    questions_to_display = []
    question_counter = 0
    random_nums = []
    counter = 0
    score = 0

    def read_json_into_dict(self):
        with open("static/JSON/quiz_questions.json") as jsonfile:
            self.questions_all = json.load(jsonfile)

    @staticmethod
    def merge(dict1, dict2):
        return dict2.update(dict1)

    def generate_unique_random_values(self):
        self.counter = 0

        for n in range(100):
            r = random.randint(1, 15)
            if r not in self.random_nums:
                self.random_nums.append(r)

            if len(self.random_nums) == 10:
                for m in range(len(self.random_nums)):
                    if len(self.questions_QA) == 10:
                        break
                    self.merge({'Question' + str(self.random_nums[m]): self.questions_all['Questions']['Question' +
                               str(self.random_nums[m])]}, self.questions_QA)
            else:
                continue

    def get_random_nums(self):
        return self.random_nums

    def get_questions(self):
        return self.questions_QA

    def ask_user_question(self):
        self.question_counter = 0
        self.score = 0

        print("Welcome! please answer these questions, you will receive a score at the end.")
        print("\nYou will receive a question followed by 4 possible options, select your choice using [A],[B],"
              "[C] or [D].")
        print("Then the test will continue to the next question. There are 10 questions.\n")
        while self.question_counter < 10:
            question_link = self.questions_QA['Question' + str(self.random_nums[self.question_counter])]
            print("Question " + str(self.question_counter + 1))
            print("\n" + question_link['Question'])

            print("\nOptions\n")
            try:
                print("A : " + str(question_link['A'][0]))
                print("B : " + str(question_link['B'][0]))
                print("C : " + str(question_link['C'][0]))
                print("D : " + str(question_link['D'][0]))

                users_response = input("\nWhat is your decision : ")

                if not any(x in users_response.upper() for x in ['A', 'B', 'C', 'D']):
                    raise ValueError("\nYou have entered something other than the available options.. "
                                     "Please try again.\n")
            except ValueError as e:
                print(e)
                continue
            except KeyError:
                print("\nYou haven't entered a valid answer for... Please try again.\n")
                continue
            else:
                if question_link[users_response.upper()][1]:
                    self.score += 1
                self.question_counter += 1
                print("_" * 50)
                continue

        print("\nThanks for taking the quiz!")
        if self.score == 0:
            print("\nDo some more revision please, then you can definitely get that 100%")
        elif 1 <= self.score <= 5:
            print("\n Not bad, maybe revise some parts")
        elif 6 <= self.score <= 9:
            print("\nWow.. very impressive")
        else:
            print("\nNot one wrong.. you are good!")

        print("\nYou scored " + str(self.score) + " out of " + str(len(self.questions_QA)))

        exit("\n...exiting...")


# quiz = QuizCreator()
# quiz.read_json_into_dict()
# quiz.generate_unique_random_values()
# question = quiz.get_questions()
#
# print(question.get('Question1')['A'][1])
