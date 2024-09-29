import random 
import string
print("Welcome To Password Generator")
letters=string.ascii_letters
digits=string.digits
special_characters=string.punctuation
all_characters=letters+digits+special_characters
print("Press 1 for letters password")
print("Press 2 for Digits password")
print("Press 3 for special_characters password")
print("Press 4 for all_characters password")
print("Press 5 for exit")
password=""
password2=""
password3=""
password4=""
while(True):
 choice=int(input("Enter your choices:"))
 if choice==1:
    length=int(input("Enter your length of your password:"))
    for i in range(length):
     password+="".join(random.choices(letters))
    print("Your Required Password is:",password)
 elif choice==2:
   length=int(input("Enter the length of your password :"))
   for i in range(length):
     password2+="".join(random.choices(digits))
     print("Required Password is:",password2)
 elif choice==3:
   length
