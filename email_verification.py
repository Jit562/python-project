email = input("Enter your email id:  ")

'''
condition:-
1. @ , .in, .com, .yahoo
1. space nahi hona chahiye
2. greter then 5
3. first latter alphabet hona chahiye
4. 
'''
k,j,d = 0,0,0
if len(email) >= 5:
    if email[0].isalpha:
        if ('@' in email) and (email.count('@') == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j = 1
                    elif i.isdigit():
                        continue

                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1        

                if k == 1 or j == 1 or d == 1:
                    print("Invalid email 5")        
            else:
                print("Invalid email 4")
        else:
            print("Invalid email 3")
    else:
        print("Invalid email 2")
    
else:
    print("wrong email 1")



# using regix module

import re

email_search = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

if re.search(email_search, email):
    print("Right email: ")
else:
    print("Wrong email")    
