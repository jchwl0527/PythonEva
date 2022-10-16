# 1
str1 = "Nanjing University"
str2 = str1[:7] + " Normal " + str1[-10:]
print(str2)
# 2
s = "python\n编程\t很\t容易\t学"
print(len(s))
# 3
# strip()
# 4
s = 'hello'
t = 'world'
s += t
print(s, s[-1], s[2:8], s[::3], s[-2::-1])
# 5
print('4' + '5')
# 6
s = "PYTHON"
print("{0:3}".format(s))
# 7
a = "Python等级考试"
b = "="
c = ">"
print("{0:{1}{3}{2}}".format(a, b, 25, c))
# 8
s1 = "企鹅"
s2 = "超级游泳健将"
print("{0:^4}:{1:!<9}".format(s1, s2))
# 9
print("{:>15s}:{:<8.2f}".format("length", 23.87501))
# 10 C
# 11
vlist = list(range(5))
print(vlist)
# 12
ls = [3.5, "Python", [10, "LIST"], 3.6]
print(ls[2][-1][1])
# 13
L1 = ['abc', ['123', '456']]
L2 = ['1', '2', '3']
print(L1 > L2)

# 14
import random

li = []
for i in range(0, 100):
    x = random.randint(70, 100)
    li.append(x)
    print(li[i], end=" ")
    if (i + 1) % 10 == 0:
        print()
print(max(li))
print(min(li))
# 15
li = [8, 10, 2, 16, 14, 4, 6, 18, 12]
print(li)
print(li.index(4))
# 16
import random

li = []
for i in range(0, 100):
    x = random.randint(70, 100)
    li.append(x)
    print(li[i], end=" ")
    if (i + 1) % 10 == 0:
        print()
print(li.count(75))
print(li.index(75))

# 17
li = [8, 10, 2, 16, 14, 4, 6, 18, 12]
print(li)
li.sort()
print(li)
for x in li:
    if x > 15:
        p = li.index(x)
        break
li.insert(p, 15)
print(li)
li.remove(10)
print(li)
# 18
import random

li = []
for i in range(0, 10):
    li.append(random.randint(0, 100))
print(li)
li.sort()
print(li)
li.reverse()
print(li)

# 19
import random

li = []
for i in range(0, 10):
    li.append(random.randint(0, 100))
print(li)
s = 0
for x in li:
    s = s + x
ave = s / 10
print(ave)
n = 0
for x in li:
    if x > ave:
        n = n + 1
print(n)

# 20
cj = []
for i in range(3):
    a = eval(input('请输入一个成绩'))
    cj.append(a)
print(cj)
s = 0
for x in cj:
    s = s + x
ave = s / len(cj)
cha = abs(cj[0] - ave)
mincha = cha
minzhi = cj[0]
for x in cj:
    cha = abs(x - ave)
    if cha < mincha:
        minzhi = x
        mincha = cha
print(minzhi)
