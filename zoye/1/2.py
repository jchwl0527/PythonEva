import matplotlib.pyplot as plt

with open("D:\\score\\pingshi.txt", mode='r', encoding='utf-8') as fin1:
    with open("D:\\score\\shiyan.txt", mode='r', encoding='utf-8') as fin2:
        with open("D:\\score\\scoreresult.txt", mode='w', encoding='utf-8') as fout:
            mydata1 = fin1.readline()
            mydata1 = fin1.readline()
            mydata2 = fin2.readline()
            mydata2 = fin2.readline()
            totalscore = 0
            list01 = []
            list02 = []
            while mydata1 != "":
                str01 = mydata1.split()
                str02 = mydata2.split()
                print(str01[0] + ":")
                print(str02[0] + ":")
                print(str01[1] + ":")
                print(str02[1] + ":")
                totalscore = eval(str01[1]) * 0.1 + eval(str02[1]) * 0.2
                print("总成绩为：" + str(totalscore))
                list01.append(str01[0])
                list02.append(totalscore)
                fout.write(str01[0] + " " + str(totalscore) + "\n")
                mydata1 = fin1.readline()
                mydata2 = fin2.readline()
print(list01)
print(list02)
plt.bar(list01, list02)
plt.show()
fout.close()
fin1.close()
fin2.close()
