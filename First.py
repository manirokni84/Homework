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




country = input("where is your favorite county?")

if country.lower()=="iran":
    print("shiraz city")
elif country.lower()=="france":
    print("paris city")
elif country.lower()=="england":
    print("london city")
else:
    print("i dont know.")



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