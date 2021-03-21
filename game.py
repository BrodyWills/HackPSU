import tkinter as tk
import tkinter.ttk as ttk
import random


class Question:
    def __init__(self, question, options, answer, explanation):
        self.question = question
        self.options = options
        self.answer = answer
        self.explanation = explanation


def correct_screen(root, c_question, question, option1, option2, option3):
    correct_frame = ttk.Frame(root)
    correct = ttk.Label(correct_frame, text="CORRECT!")
    correct.place(x=500, y=550, height=300, width=600)
    correct.pack()
    expla = ttk.Label(correct_frame, text=c_question.explanation)
    expla.place(x=500, y=700, height=300, width=600)
    expla.pack()
    next_button = ttk.Button(correct_frame, text="Next Question", command=lambda: next_question(root, question, option1, option2, option3, correct_frame))
    next_button.place(x=500, y=800, height=300, width=600)
    next_button.pack()
    correct_frame.place(x=100, y=200, height=700, width=1400)


def wrong_screen(root, c_question, question, option1, option2, option3):
    wrong_frame = ttk.Frame(root)
    wrong = ttk.Label(wrong_frame, text="WRONG!")
    wrong.place(x=500, y=550, height=300, width=600)
    wrong.pack()
    expla = ttk.Label(wrong_frame, text=c_question.explanation)
    expla.place(x=500, y=700, height=300, width=600)
    expla.pack()
    next_button = ttk.Button(wrong_frame, text="Next Question",
                             command=lambda: next_question(root, question, option1, option2, option3,
                                                           wrong_frame))
    next_button.place(x=500, y=800, height=300, width=600)
    next_button.pack()
    wrong_frame.place(x=100, y=200, height=700, width=1400)


def check_answer(root, letter, c_question, question, option1, option2, option3):
    if letter == c_question.answer:
        correct_screen(root, c_question, question, option1, option2, option3)
    else:
        wrong_screen(root, c_question, question, option1, option2, option3)


def setup(root):
    root.geometry("1600x900")
    root.title("Game")

    question = ttk.Label(root)
    question.place(x=100, y=50, height=100, width=1400)
    question.configure(font="TkDefaultFont")
    question.configure(anchor='center')

    option1 = ttk.Button(root)
    option1.place(x=100, y=200, height=300, width=600)

    option2 = ttk.Button(root)
    option2.place(x=900, y=200, height=300, width=600)

    option3 = ttk.Button(root)
    option3.place(x=500, y=550, height=300, width=600)

    wrong_frame = ttk.Frame(root)
    wrong = ttk.Label(wrong_frame, text="WRONG!")
    wrong.pack()

    root.tkraise()
    return question, option1, option2, option3


def get_questions():

    q1 = Question("What is a basic entrepreneurial mindset?",
                 ["A. A set of skills that enable people to identify and make the most of opportunities while overcoming and learning from setbacks",
                  "B. The ability to think in a manner which prioritizes success while not worrying about the outcome of an opportunity",
                  "C. Prioritization of thoughts specifically relating to the investment of a business in hopes of furthering success"],
                  "A", "The correct answer is A; Entrepreneurship is the ability to strive for success based on various opportunities.")

    q2 = Question("Self reliance and initiative are important characteristics in developing an entrepreneurial mindset. What are some characteristics of these?",
                 ["A. Changing focus in order to maintain the proper thought path",
                  "B. The ability to change commitments based on the projects needs",
                  "C. Maintaining an optimistic attitude despite ambiguity"],
                  "C", "The correct answer is C; Self confidence combined with motivation and initiative create optimism in entrepreneurs.")

    q3 = Question("What is the difference between an internal and external locus of control?",
                 ["A. An internal locus of control believes that the outcome is controlled by luck while an external one is the belief that a person controls the outcome",
                  "B. An internal locus of control believes that the outcome is controlled by the person while external is the thought that the outcome is controlled by luck",
                  "C. An internal locus of control focuses on both luck and the person itself while external focuses on other people"],
                  "B", "The correct answer is B; The difference between an internal and external locus of control is defined exactly in the question.")

    q4 = Question("In order to become future oriented, what is one thing an entrepreneur could do?",
                 ["A. Think ahead of the future and what one would need to continue",
                  "B. Develop an optimistic disposition alongside knowledge in order to push ahead as time progresses",
                  "C. Focus on the business aspect of a group and make predictions for the future"],
                  "B", "The correct answer is B; Thinking ahead for the future allows for an entrepreneur to continue to move forward more efficiently.")

    q5 = Question("Responsibility, inquiry, goal-orientation and forward thinking are all examples of what characteristic of entrepreneurial mindsets?",
                 ["A. Self reliance and initiative",
                  "B. Opportunity recognition",
                  "C. Future oriented"],
                  "C", "The correct answer is C; A future oriented person is required to have at least 2 of the 4 following characteristics.")

    q6 = Question("Why are creativity and innovation key concepts in terms of entrepreneurship?",
                 ["A. They allow for each business to be unique and have its own identity",
                  "B. They create a sense of purpose and reason for the existence of the company",
                  "C. They help create the backbone of the thought for creating an object"],
                  "A", "The correct answer is A; The identity of a business is essential to develop as an entrepreneur.")

    q7 = Question("Critical thinking and problem solving are key skills throughout life, but how can it impact it from an entrepreneurial standpoint?",
                 ["A. Critical thinking is a key skill that works hand in hand with problem solving, but it does not impact entrepreneurial life",
                  "B. Problem solving allows for one to move past a roadblock and improve over time",
                  "C. It allows an entrepreneur to evaluate opportunities and apply other skills, like planning for the future"],
                  "C", "The correct answer is C; The evaluation of different opportunities requires critical thinking and problem solving, those two skills can also be used in working on other problems as well.")

    q8 = Question("Why is communication so important in the entrepreneurial world?",
                 ["A. It permits the entrepreneur to move on important opportunities with other organizations",
                  "B. Without communication entrepreneurs would not be able to focus properly on their business/idea",
                  "C. It hinders the entrepreneurial process and should be avoided entirely"],
                  "A", "The correct answer is A; It allows the entrepreneur to develop relationships with other organizations while seeking the best possible opportunity.")

    q9 = Question("How does communication allow for key partnerships to be developed?",
                 ["A. Partnerships and communication are individual topics that complement one another",
                  "B. Communication creates stable relationships with possible business partners",
                  "C. Communication relies solely on relationships to be effective"],
                  "B", "The correct answer is B; Stable relationships are essential to move forward in the entrepreneurial world.")

    q10 = Question("Flexibility and adaptability are some of the most important factors for entrepreneurs because...",
                 ["A. It allows for in the moment decisions to be made without having a serious effect on the business",
                  "B. Rapid changes will not hinder one's mindset",
                  "C. Both A and B"],
                  "C", "The correct answer is C; In the moment decisions and rapid changes will not affect morale while one is working.")

    q11 = Question("Which of these is not true about entrepreneurial leaders?",
                 ["A. These leaders encourage a collaborative and involved environment to foster good ideas",
                  "B. These leaders’ main goal is to better themselves, with the work they do being a means to that end",
                  "C. These leaders are clear communicators, being honest yet constructive with their teams in order to get the best results from their work"],
                  "B", "The correct answer is B; Leaders are meant to work for the benefit of the collective, pushing for those around them so as to improve the whole.")

    q12 = Question("Entrepreneurial leaders should be...",
                 ["A. Positive",
                  "B. Hyper-Critical",
                  "C. Strict"],
                  "A", "The correct answer is A; Maintaining a positive attitude with your team is paramount to creating a successful work environment.")

    q13 = Question("Entrepreneurial leaders...",
                 ["A. Are hands-off, allowing their team to do most of the work without major input from the leader",
                  "B. Are distant from their employees, giving them space to do their work while the leader focuses on other matters",
                  "C. Are personable with their team, spending time with them and engaging in their work"],
                  "C", "The correct answer is C; Building personal relationships with your team helps to build trust and cohesion.")

    q14 = Question("Building trust with your team is best achieved by being...",
                 ["A. Honest",
                  "B. Secluded",
                  "C. Egotistical"],
                  "A", "The correct answer is A; Honesty and openness is an important part of creating a healthy and sustainable work environment.")

    q15 = Question("All the following are good traits for entrepreneurial leaders except...",
                 ["A. Perseverance",
                  "B. Supportive",
                  "C. Lackadaisical"],
                  "C", "The correct answer is C; Being present and involved with your team is very important for an entrepreneurial leader.")

    q16 = Question("What is a strategic vision?",
                 ["A. A good business idea and passion for your work",
                  "B. A plan on where you want your company to be in the future and strategies on how you will get it there",
                  "C. Both A and B"],
                  "C", "The correct answer is C; While the idea is an important part of any entrepreneurship, a plan is necessary to actually achieve your goals.")

    q17 = Question("Which of the following is a proper response by an entrepreneurial leader to failure?",
                 ["A. Place responsibility on your team and encourage them to do better",
                  "B. Share blame amongst your team and work together to rebound",
                  "C. Accept responsibility and promise to improve in the future"],
                  "B", "The correct answer is B; In a team setting, it is important to recognize that everyone plays a part in both the successes and failures of the team.")

    q18 = Question("As an entrepreneurial leader, you recognize that some of your team members are excelling while others are falling behind. What should you do?",
                 ["A. Place all of your attention on helping those struggling, leaving those succeeding to fend for themselves",
                  "B. Focus on those who are working well and accept that others just won’t meet those same standards",
                  "C. Delegate more responsibilities to those succeeding so that they can help foster improvement from everyone"],
                  "C", "The correct answer is C; Ensuring that those with talent are recognized is just as important as helping those less talented with improving. An effective way to accomplish this is to delegate responsibilities among the team.")

    q19 = Question("Where do entrepreneurial leaders come from?",
                 ["A. All levels of the organization have the ability to foster leadership skills",
                  "B. Individuals outside the organization",
                  "C. Individuals with established positions of leadership and authority"],
                  "A", "The correct answer is A; Leaders can come from anywhere, and it is the job of current leaders to find these talents and develop them through mentorship.")

    q20 = Question("Why does a company need entrepreneurial leaders?",
                 ["A. To maintain the company’s status quo of success and profitability",
                  "B. To keep up with the pace of change in the world, anticipate the future, and adapt to change",
                  "C. To take the ideas of upper management and implement them in everyday work"],
                  "B", "The correct answer is B; The world we live in today is ever-changing, and so it is paramount that those in charge are able to respond to these changes to create the best possible outcome for the company.")

    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]
    return questions


def next_question(root, question, option1, option2, option3, screen):
    screen.destroy()
    if len(questions) <= 1:
        root.destroy()
        exit()
    rand = random.randint(0, len(questions) - 1)
    current_q = questions[rand]
    del questions[rand]
    question['text'] = current_q.question
    option1['text'] = current_q.options[0]
    option2['text'] = current_q.options[1]
    option3['text'] = current_q.options[2]
    option1['command'] = lambda: check_answer(root, 'A', current_q, question, option1, option2, option3)
    option2['command'] = lambda: check_answer(root, 'B', current_q, question, option1, option2, option3)
    option3['command'] = lambda: check_answer(root, 'C', current_q, question, option1, option2, option3)


def main():
    root = tk.Tk()
    screen = tk.Frame()
    questions = get_questions()
    question, option1, option2, option3 = setup(root)
    next_question(root, question, option1, option2, option3, screen)

    root.mainloop()


if __name__ == '__main__':
    questions = get_questions()
    main()
