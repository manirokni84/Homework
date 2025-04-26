a = 28
b = 2

c = a+b
print(c)

d = a-b
print(d)

f = a*b
print (f)

h = a/b
print(h)

n = a//b
print(n)

m = a**b
print(m)


print(..................................................................................................)


grades = []

# گرفتن نمره 6 درس
for i in range(6):
    grade = float(input(f"نمره درس {i + 1} را وارد کنید: "))
    grades.append(grade)

# محاسبه معدل
average = sum(grades) / len(grades)
print(f"معدل شما: {average}")

# بررسی شرایط جایزه
if 18 <= average <= 20:
    print("شما برنده پلی استیشن شدید!")
elif 16 <= average < 18:
    print("شما برنده دوچرخه شدید!")
else:
    print("شرمنده، جایزه‌ای نداریم!")


print(...........................................................................................)

country = input("where is your favorite county?")

if country.lower()=="iran":
    print("shiraz city")
elif country.lower()=="france":
    print("paris city")
elif country.lower()=="england":
    print("london city")
else:
    print("i dont know.")


print(................................................................................................)


numbers = []

for i in range(6):
    num = float(input(f"عدد {i+1} را وارد کنید: "))
    numbers.append(num)

total_sum = sum(numbers)
total_sub = numbers[0] - sum(numbers[1:])
total_mul = 1
for num in numbers:
    total_mul *= num
total_div = numbers[0]
for num in numbers[1:]:
    if num != 0:
        total_div /= num
    else:
        total_div = "خطا: تقسیم بر صفر"
        break

print("جمع:", total_sum)
print("تفریق:", total_sub)
print("ضرب:", total_mul)
print("تقسیم:", total_div)

if isinstance(total_sum, (int, float)) and total_sum > 100:
    print("Yes")
else:
    print("No")


print(................................................................................................)

    print("type a text")
x = input()
reversed_x = x[::-1]
print(reversed_x)


print(..............................................................................................)

print("type one number ")
x=int(input())
x1 = x//2
T = x-(x1*2)

x2 = x//3
T2 = x-(x2*3)

if  (T==2 or T==1) and (T2==2 or T2==1):
    print("The number is a prime number")
elif  x==2 or x==3  :
    print("The number is a prime number")
elif T==0 or T2 == 0 :
    print("sorry""  ,  ""The number is  NOT a prime number")
else :
    print("sorry""  ,  ""The number is  NOT a prime number")


print(..............................................................................................)

print("type one number ")
x=int(input())

print("Your number is :" , x)

print(".")
print(".")
print(".")
print(".")
print(".")
print(".")

xlist=[1*x,2*x,3*x,4*x,5*x,6*x,7*x,8*x,9*x,10*x,11*x,12*x]
for x in xlist:
    print(x)

print(..................................................................................................)