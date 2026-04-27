# 1. Student Result System
# Input marks of 5 subjects.
# If any subject < 40 → Fail
# Else calculate percentage and grade.
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))
if m1 < 40 or m2 < 40 or m3 < 40 or m4 < 40 or m5 < 40:
    print("Fail")
else:
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5
    print("Percentage:", percentage)
    if percentage >= 90:
        print("Grade A")
    elif percentage >= 75:
        print("Grade B")
    elif percentage >= 50:
        print("Grade C")
    else:
        print("Grade D")
    
# 2. Leap Year with Century Rule
# Check whether a given year is a leap year considering century years (e.g., 1900, 2000).
year=int(input("Enter the year to check for the leap year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap year")
else:
    print("Not leap year") 

# 3. Salary Tax Calculator
# Input annual salary:
# ≤ 2.5L → No tax
# 2.5L–5L → 5%
# 5L–10L → 20%
# 10L → 30%
income = int(input("Enter income: "))
if income <= 250000:
    print("No Tax")
elif income <= 500000:
    print("Tax: 5%")
elif income <= 1000000:
    print("Tax: 20%")
else:
    print("Tax: 30%")

# 4. Triangle Validity and Area
# Check if a triangle is valid using sides, then calculate its area.
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("Triangle is valid")
    print("Area of triangle:", area)
else:
    print("Invalid Triangle")

# 5. Number Comparison
# Input three numbers and print:
# Largest
# Smallest
# Whether all are equal
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
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
        print("Smallest:",n1)
    elif n2<=n1 and n2<=n3:
        print("Smallest:",n2)
    else:
        print("Smallest:",n3)
    
# 6. Character Identifier
# Input a character and identify whether it is:
# Uppercase letter
# Lowercase letter
# Digit
# Special character
ch=input("Enter a character:")
if len(ch)!=1:
    print("Please enter only one character")
else:
    if ch.isupper():
        print("Uppercase letter")
    elif ch.islower():
        print("Lowercase letter")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special character")

# 7. Password Strength Checker
# Input password and check:
# Minimum 8 characters
# Contains digit and special character
password=input("Enter password:")
if len(password)<8:
    print("password must be atleast 8 characters")
else:
    has_digit=any(ch.isdigit() for ch in password)
    has_special=any(not ch.isalnum() for ch in password)
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
if dis <= 10:
    fare = 10
elif dis <= 30:
    fare = 20
else:
    fare = 30
if age >= 60:
    fare *= 0.8
print("Total fare:", round(fare, 2))
        
# 9. Exam Eligibility
# Input attendance percentage and medical certificate (yes/no).
# Check eligibility for exam.
attendance=int(input("Enter attendance in percentage:"))
cer=input("Having medical certificate either (yes/no):").lower()
if attendance>=75:
    print("Eligible")
elif cer=='yes':
    print("Eligible")
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
    discount+=0.05
final=amount-(amount*discount)
print("Final amount:", final)

# 14. Traffic Signal System
# Input signal color and print action:
# Red → Stop
# Yellow → Ready
# Green → Go
color=input("enter traffic signal color:").lower()
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
