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