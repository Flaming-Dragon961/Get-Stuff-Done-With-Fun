import os
import random
import string
from collections import Counter

print("Welcome to the all in one app!")
x = int(input("\n1. To-do list 2. Calculator 3. Filehub 4. EmployeeTracker 5. StockAdvisor. 6. Password Generator 7. Wordle 8. Quit"))

r = []
while x!=8:
    try:
     # to do list
            if x == 1:
                y=int(input("What would you like to do in your to-do list. 1.Add task 2. Remove Task 3. Show tasks 4. Quit"))
                while y<4:
                    if y == 1:
                        j=input("Write the task you want to add:")
                        r.append(j)
                        print("The task has been added")
                    elif y == 2:
                        i=input("Write the task you want to remove:")
                        r.remove(i)
                        print("The task has been removed")
                    elif y == 3:
                        print(r)
                    y = int(input("What would you like to do in your to-do list. 1.Add task 2. Remove Task 3. Show tasks 4. Quit"))
                if y == 4:
                    print("We are done!")
                    x = int(input("\n1. To-do list 2. Calculator 3. Filehub 4. EmployeeTracker 5. StockAdvisor. 6. Password Generator 7. Wordle 8. Quit"))

            #calculator
            if x==2:
                p = int(input("What would you like to do in the calculator: 1. Add, 2. Subtract, 3. Multiplication, 4. Division, 5. Quit"))
                if p<5:
                    t = int(input("What is the first number you want in the operation"))
                    b = int(input("What is the second number you want in the operation"))
                else:
                    print("Goodbye!")
                while p<5:
                    def calculator():
                        if p==1:
                            print(t+b)
                        elif p==2:
                            print(t-b)
                        elif p==3:
                            print(t*b)
                        elif p==4:
                            print(t/b)
                    calculator()
                    p = int(input("What would you like to do in the calculator: 1. Add 2. Subtract 3. Multiplication 4. Division 5. Quit"))
                    if p<5:
                        t = int(input("What is the first number you want in the operation"))
                        b = int(input("What is the second number you want in the operation"))
                else:
                    print("Goodbye!")
                    x = int(input("\n1. To-do list 2. Calculator 3. Filehub 4. EmployeeTracker 5. StockAdvisor. 6. Password Generator 7. Wordle 8. Quit"))
            #filehub

            if x==3:
                g = int(input("What would you like to do in Filehub: 1.Create 2. Create and Update 3. Delete 4. Read 5. Quit"))
                while g<5:
                    l=input("What is the name of the file?:")
                    if g==1:
                        p = open(l, "x")
                        print("The file is created", p)
                        p.close()
                    elif g==2:
                        q = input("What text would you like to write?:")
                        v = open(l, "w")
                        v.write(q)
                        print("The text has been updated")
                        v.close()
                    elif g==3:
                        os.remove(l)
                        print("The file has been deleted")
                    elif g==4:
                        e = int(input("Would you like to read: 1. Specific number of lines 2. Whole file"))
                        if e == 1:
                            z = int(input("How many lines?:"))
                            c = open(l, "r")
                            if z > 1:
                                for i in range(z):
                                    print(c.readline())
                                c.close()
                            else:
                                print(c.readline())
                                c.close()
                        elif e == 2:
                            c = open(l, "r")
                            print(c.read())
                            c.close()
                    g = int(input("What would you like to do in Filehub: 1.Create 2. Create and Update 3. Delete 4. Read 5. Quit"))
                else:
                    print("Goodbye!")
                    x = int(input("\n1. To-do list 2. Calculator 3. Filehub 4. EmployeeTracker 5. StockAdvisor. 6. Password Generator 7. Wordle 8. Quit"))


            # Employee Tracker
            if x==4:
                a = int(input("What is the salary?"))
                b = int(input("What is the age?"))
                c = input("What is the name?")
                d = input("What is the position at the company?")
                e = input("How long have they been there?")

                def employeeinfo():
                    print(f"Name: {c} Age: {b} Position: {d} Duration at company: {e} Current Salary {a}")

                bb = ["Salary", "Age", "Position at company", "Experience at company"]
                w = random.randint(0, 3)
                uu = random.randint(1,100)

                def happyorno():
                    if uu<=50:
                        print(f"{c} is not happy. The reason being his/her:{bb[w]}")
                    else:
                        print(f"{c} is happy. The reason being his/her:{bb[w]}")

                employeeinfo()
                happyorno()
                x = int(input("\n1. To-do list 2. Calculator 3. Filehub 4. EmployeeTracker 5. StockAdvisor. 6. Password Generator 7. Wordle 8. Quit"))

            #stock advisor

            if x==5:
                class Stock():
                    def __init__(self,name,stockvalue,companyrevenue,companyindustry,alltimechange,companylength):
                        self.a=name
                        self.b=stockvalue
                        self.c=companyrevenue
                        self.d=companyindustry
                        self.e=alltimechange
                        self.f=companylength

                    def totalinfo(self):
                        print(f"Company Name: {self.a} Current Stock Value: {self.b} Company Revenue: {self.c} Company Industry: {self.d} All Time Rate of Change for Stock Price(%): {self.e} Company Length: {self.f}")
                        if self.b>500 and self.e>500 and self.f<5:
                            print(f"{self.a} is quite a high priced stock. It's also got an incredible growth rate of {self.e}.\nHowever, it's important to consider that the company was created less than 5 years ago, actually {self.f} years ago, meaning theres not much room for growth so I would not reccommend an investment",end="")
                        else:
                            print(f"{self.a} doesnt have an insanely high stock price. The growth rate is around: {self.e}.\nThat's very good and another good sign is that the company was created {self.f} years ago, meaning theres been steady growth over time. Overall, I would reccommend an investment because the company isn't built off of hype, and still has room to grow",end="")

                q=Stock("Apple", 700, "35 billion", "Technology", 600,3)
                bb=Stock("\nGoogle",300,"40 billion","Technology",300,10)
                q.totalinfo()
                bb.totalinfo()
                x = int(input("\n1. To-do list 2. Calculator 3. Filehub 4. EmployeeTracker 5. StockAdvisor. 6. Password Generator 7. Wordle 8. Quit"))

            #password generator

            if x == 6:
                gg=int(input("How long should the password be in characters?"))
                mm=int(input("Would you like special characters? 1. Yes or 2. No?"))
                yyy = random.randint(0, 25)
                nnn = random.randint(0, 9)
                bbb = random.randint(0, 31)
                if mm==1:
                    pp = random.randint(0, 3)
                    for i in range(gg):
                        if pp == 0:
                            print(string.ascii_uppercase[yyy], end="")
                        elif pp == 1:
                            print(string.ascii_lowercase[yyy], end="")
                        elif pp == 2:
                            print(string.digits[nnn], end="")
                        else:
                            print(string.punctuation[bbb], end="")
                        pp = random.randint(0, 3)
                        yyy = random.randint(0, 25)
                        nnn = random.randint(0, 9)
                        bbb = random.randint(0, 31)
                elif mm==2:
                    pp = random.randint(0, 2)
                    for i in range(gg):
                        if pp==0:
                            print(string.ascii_uppercase[yyy], end="")
                        elif pp==1:
                            print(string.ascii_lowercase[yyy], end="")
                        elif pp==2:
                            print(string.digits[nnn], end="")
                        pp = random.randint(0, 2)
                        yyy = random.randint(0, 25)
                        nnn = random.randint(0, 9)
                        bbb = random.randint(0, 31)
                x = int(input("\n1. To-do list 2. Calculator 3. Filehub 4. EmployeeTracker 5. StockAdvisor. 6. Password Generator 7. Wordle 8. Quit"))

            if x == 7:
                index = 0
                words=[]
                with open("words.txt") as file:
                    for line in file:
                        if len(line.strip()) != 5:
                            continue
                        elif len(line.strip()) == 5 and line.strip().isalpha() and line.strip().islower():
                            words.append(line.strip())
                    rando = random.randint(0, len(words) - 1)
                    word = (words[rando])
                for tries in range(5):
                    guess = input("What is your guess for the 5 letter word?")
                    if guess!=word:
                        for character in word:
                            counter = Counter(word)
                            counter2 = Counter(guess)
                            if guess[index]==character:
                                print("You got a letter!",guess[index])
                                index+=1
                            elif guess[index] in word and guess[index]!= character and counter[guess[index]]>=counter2[guess[index]]:
                                print(f"The letter {guess[index]} is in the word, just not where you put it")
                                index += 1
                            else:
                                print("You did not get a letter")
                                index+=1
                        index=0
                        print(word)
                    else:
                        print(f"You Got It! The guess you made was {guess}, and that was the right word!")
                        break
                x = int(input("\n1. To-do list 2. Calculator 3. Filehub 4. EmployeeTracker 5. StockAdvisor. 6. Password Generator 7. Wordle 8. Quit"))
    except Exception as e:
        print("There is an error",e)
else:
    print("Thanks for coming!")






