# program capable of displaying questions to the user like KBC (kaun banega crorepati)
# using list to store the questions and their right answers
# displaying final amount that user wins after playing the game

questions = [
    ["What's your name", "Hamza", "Ali", "Ansab", "Hasan", 1],
    ["What's your age", "Ham", "A", "An", "Has", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1],
    ["What's your place", "R", "Z", "Y", "X", 1]

]
# level=[1000,2000,3000,5000, 10000, 20000,40000,80000,160000, 320000, 640000,125000,2500000,5000000, 1000000]
level = ['1 Thousand', '2 Thousand', '3 Thousand', '5 Thousand', '10 Thousand', '20 Thousand',
         '40 Thousand', '80 Thousand', '1.6 Lac', '3.2 Lac', '6.4 Lac', '12.5 Lac', '25 Lac', '50 Lac', '1 Crore']
money = 0
print('''\n                                               Game rules\n
-> There are 15 levels in this game , means you have to answer 15 questions correct to win Rs.1 Crore
-> You can quit the game at any point and you will get the amount you had win from the last question
->    *But*
-> Game over! (if you failed to answer correctly)(and the amount you will win will be determined upon the level you are currently)
-> level 1 ** If you have answered the first 5 questions correctly so you will win Rs. 10 Thousand either you failed to answer the next question or quit           
-> level 2 ** If you have answered the first 10 questions correctly so you will win Rs. 3.2 lacs either you failed to answer the next question or quit
-> level 3 ** If you have answered the all the 15 questions correctly so you will win Rs. 1 crore ''')
for i in range(0, len(questions)):
    question = questions[i]
    print(f'\n\n             level: {i+1}\n')
    print(f'Question for Rs. {level[i]}')
    print(question[0])
    print(f"A. {question[1]}         B. {question[2]}")
    print(f"C. {question[3]}         D. {question[4]}")
    reply = int(input("Enter your answer {1-4} or {0} to quit \n"))
    if reply==0:
        money=level[i-1]
        break
    if reply == question[-1]:
        print(f'Correct answer! You have won Rs. {level[i]} \n')
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
            print("Congratulations! You have won the game")
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is Rs. {money}")
