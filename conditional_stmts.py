# 1. Student Result System
# Input marks of 5 subjects.
# If any subject < 40 → Fail
# Else calculate percentage and grade.
s1,s2,s3,s4,s5=map(int, input().split())
if s1 <40 or s2<40 or s3<40 or s4<40 or s5<40:
    print("Fail")
else:
    sum=(s1+s2+s2+s4+s5)
    per=sum/5
    if per>=90:
        print("Grade A")
    elif per>=75:
        print("Grade B")
    if per>=60:
        print("Grade C")
    else:
        print("Grade A")
    
# 2. Leap Year with Century Rule
# Check whether a given year is a leap year considering century years (e.g., 1900, 2000).
year=input("Enter the year to check for the leap year:")
if (year%400==0) or(year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a leap year") 

# 3. Salary Tax Calculator
# Input annual salary:
# ≤ 2.5L → No tax
# 2.5L–5L → 5%
# 5L–10L → 20%
# 10L → 30%
annual_salary=float(input("Enter annual salary in lakhs:"))
if annual_salary<=2.5:
    print("No Tax")
elif annual_salary<=5:
    print("5% tax")
elif annual_salary<=10:
    print("20% tax")
else:
    print("30% tax")

# 4. Triangle Validity and Area
# Check if a triangle is valid using sides, then calculate its area.
import math 
s1=int(input("Enter side1:"))
s2=int(input("Enter side2:"))
s3=int(input("Enter side3:"))
if (s1+s2>s3) and (s2+s3>s1) and (s1+s3>s2):
    print("Valid Triangle")
    s=(s1+s2+s3)/2
    area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    print("Area:",area)
else:
    print("Not a valid traingle")

# 5. Number Comparison
# Input three numbers and print:
# Largest
# Smallest
# Whether all are equal
n1,n2,n3=map(int,input().split())
if n1==n2==n3:
    print("All are equal")
else:
    if n1>=n2 and n1>=n3:
        print("Largest:",n1)
    elif n2>=n1 and n2>=n3:
        print("Largest:",n2)
    else:
        print("Largest:",n3)
    if n1<=n2 and n1<=n3:
        print("smallest:",n1)
    elif n2<=n1 and n2<=n3:
        print("smallest:",n2)
    else:
        print("smallest:",n3)
    
# 6. Character Identifier
# Input a character and identify whether it is:
# Uppercase letter
# Lowercase letter
# Digit
# Special character
ch=input("Enter a character:")
if len(ch)!=1:
    print("Please enter only one character")
if ch.isupper():
    print("Uppercase Character")
elif ch.islower():
    print("Lowercase character")
elif ch.isdigit():
    print("Digit")
else:
    print("special character")

# 7. Password Strength Checker
# Input password and check:
# Minimum 8 characters
# Contains digit and special character
password=input("Enter password:")
if len(password)<8:
    print("password must be atleast 8 characters")
else:
    has_digit=any(ch.isdigit() for ch in password)
    has_special=any(ch.isalnum() for ch in password)
    if has_digit and has_special:
        print("strong password")
    else:
        print("weak password")

# 8. Bus Fare System
# Fare based on distance:
# ≤10 km → ₹10
# 11–30 km → ₹20
# 30 km → ₹30
# Senior citizens get 20% discount.
dis=int(input("enter the distance in km:"))
age=int(input("Enter age:"))
if dis<=10:
    fare=10
elif dis<=30:
    fare=20
else:
    fare=30
if age>=60:
    fare=fare*0.8
print("Total fare:", fare)
        
# 9. Exam Eligibility
# Input attendance percentage and medical certificate (yes/no).
# Check eligibility for exam.
attendance=int(input("Enter attendance in percentage:"))
cer=input("Having medical certificate either (yes/no):").lower()
if attendance>=75 or cer=='yes':
    print("Eligible for the exam")
else:
    print("Not eligible")

# 10. Banking Interest Calculator
# Account type:
# Savings → 4%
# Current → 2%
# Fixed → 6%
# Calculate interest based on balance.
acc_type=input("Enter account type(savings/current/fixed):").lower()
bal=float(input("Enter balance:"))
if acc_type=='savings':
    rate=0.04
elif acc_type=='current':
    rate=0.02
elif acc_type=='fixed':
    rate=0.06
else:
    print("Invalid account type")
    exit()
interest=bal*rate
print("Interest:", interest)

# 11. Number Pattern Check
# Input a number and check if it is:
# Prime
# Composite
# Neither
num=int(input("Enter a number:"))
if num<=1:
    print("Neither prime nor composite")
else:
    for i in range(2,num):
        if num%i==0:
            print("composite")
            break
    else: 
        print("prime")

# 12. Weather Advisory System
# Input temperature:
# <10 → Very Cold
# 10–20 → Cold
# 21–30 → Warm
# 30 → Hot
temp=float(input("Enter the temperature in degree or celsius:"))
if temp<10:
    print("Very Cold")
elif temp<=20:
    print("Cold")
elif temp<=30:
    print("Warm")
else:
    print("Hot")

# 13. Online Order Discount
# Order amount:
# 500 → 10% discount
# 1000 → 20% discount
# Apply coupon if available.
amount=int(input("Enter the order amount:"))
coupon=input("Coupon available?(yes/no):")
if amount>=1000:
    discount=0.2
elif amount>=500:
    discount=0.1
else:
    discount=0 
if coupon=="yes":
    discount+=0.5
final=amount-(amount*discount)
print("Final amount:", final)

# 14. Traffic Signal System
# Input signal color and print action:
# Red → Stop
# Yellow → Ready
# Green → Go
color=input("enter traffic signal color:")
if color=="red":
    print("Stop")
elif color=="yellow":
    print("Ready")
elif color=="green":
    print("Go")
else:
    print("Invalid color")

# 15. Time-Based Greeting
# Input time (0–23):
# Morning
# Afternoon
# Evening
# Night
time=int(input("Enter time(0-23):"))
if time<12:
    print("Morning")
elif time<17:
    print("Afternoon")
elif time<21:
    print("Evening")
else:
    print("Night")

# 16. Insurance Eligibility
# Check eligibility based on:
# Age
# Health condition
# Smoking status
age=int(input("Enter age:"))
health=input("Good health?(yes/no):")
smoke=input("Do you smoke?(yes/no):")
if age>18 and health=='yes' and smoke=='no':
    print("Eligible for insurance")
else:
    print("Not eligible")

# 17. Mobile Recharge Plan
# Recharge amount:
# ₹199 → 1.5GB/day
# ₹299 → 2GB/day
# ₹499 → Unlimited
amount=int(input("Enter the amount for recharge:"))
if amount == 199:
    print("1.5GB/day")
elif amount == 299:
    print("2GB/day")
elif amount == 499:
    print("Unlimited")
else:
    print("Invalid plan")

# 18. Shopping Cart Validation
# Check:
# Item in stock
# Sufficient balance
# Delivery available
stock = input("Item in stock? (yes/no): ")
balance = input("Sufficient balance? (yes/no): ")
delivery = input("Delivery available? (yes/no): ")
if stock == "yes" and balance == "yes" and delivery == "yes":
    print("Order placed")
else:
    print("Order cannot be placed")

# 19. Employee Promotion System
# Based on:
# Performance rating
# Experience years
# Decide promotion eligibility.
rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
if rating >= 4 and experience >= 3:
    print("Eligible for promotion")
else:
    print("Not eligible")

# 20. Grading with Extra Credit
# Add 5 bonus marks if attendance >90%, then assign grade.
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance %: "))
if attendance > 90:
    marks += 5
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
