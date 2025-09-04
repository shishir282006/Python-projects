print("***************")
print("Welcome to Quiz Game")

question_bank=[
    {"text": "What is the output of the expression 3+2*2?" , "Answer" : "B"},
    {"text": "Which of the following is a valid variable name in Python?","Answer": "C"},
    {"text": "Which keyword is used to define a function in Python?" , "Answer" : "C"},
    {"text": "Which operator is used for exponentiation in Python?" , "Answer": "B"},
    {"text": "Which of the following is a mutable data type in Python?" , "Answer": "D"},
]
option=[
    ["A. 12" , "B. 7" , "C. 8" , "D. 10"],
    ["A. 2value" , "B. value2" ,"C. value_2" , "D. value-2"],
    ["A. func" , "B. function" , "C. def" , "D. define"],
    ["A. ^^" , "B. **" , "C. ^ ", "D. exponent"],
    ["A. tuple" , "B. str" , "C. int " , "D. list"]
]
score = 0
def check_answer(answer , check_answer_answer):
    if answer == check_answer:
        return True
    else:
        return False


for question in range(len(question_bank)):
    
    print("***********************")
    print(question_bank[question]["text"])
    for i in option[question]:
        print(i)
    answer = input("Enter your answer(A/B/C/D):").upper()
    if check_answer = (answer , question_bank[question]["Answer"]):
        print("correct answer")
        score +=1
    else:
        print("wrong answer")
        print(f"the correct nswer is {question_bank[question]["Answer"]}")
        score += 0

print(f"your final score is {score}")