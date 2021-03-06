
#----------------------------------------------------------------------------------------------------
# Задание 1.2
# Записать условие, которое является истинным, когда каждое из чисел А и В нечетное.
#----------------------------------------------------------------------------------------------------
def task_1_2(a, b):
    if((a % 2 != 0) & (b % 2 != 0)):
        print("task_1_2 true")
    else:
        print("task_1_2 false")

#----------------------------------------------------------------------------------------------------
# Задание 1.12
# Записать условие, которое является истинным, когда каждое из чисел А,В,С кратно трем.
#----------------------------------------------------------------------------------------------------
def task_1_12(a, b, c, div = 3):
    if((a % div == 0) & (b % div == 0) & (c % div == 0)):
        print("task_1_12 true")
    else:
        print("task_1_12 false")

#----------------------------------------------------------------------------------------------------
# Задание 1.22
# Ввести с клавиатуры три числа, положительные возвести в квадрат,
# а отрицательные оставить без изменений.
#----------------------------------------------------------------------------------------------------
def task_1_22(num_val):
    a = []
    for i in input(f"input {num_val} numbers: ").split():
        if(int(i) > 0):
            i = int(i)**2
        a.append(int(i))
    print(f"{a}")

#----------------------------------------------------------------------------------------------------
# Задание 2.2
# Дано двузначное число. Определить:
# а) входят ли в него цифры 3 и 7;
# б) входят ли в него цифры (4 и 8) или цифра 9
#----------------------------------------------------------------------------------------------------
def task_2_2(a):
    a = str(a)
    #a)
    if((a.find('3') >= 0) & (a.find('7') >= 0)):
        print(f"number {a} include 3 and 7")
    else:
        print(f"number {a} do not include 3 and 7")
    #b)
    if((a.find('4') >= 0) & (a.find('8') >= 0) | (a.find('9') >= 0)):
        print(f"number {a} include 4 and 8 or 9")
    else:
        print(f"number {a} do not include 4 and 8 or 9")

#---------------------------------------------------------------------------------------------------
# Задание 3.2
# Мастям игральных карт условно присвоены следующие порядковые номера: масти "пики" — 1,
# масти "трефы" — 2, масти "бубны" — 3, масти "червы" — 4,
# а достоинству карт: "валету" — 11, "даме" — 12, "королю" — 13, "тузу" — 14
# (порядковые номера карт остальных достоинств соответствуют их названиям: "шестерка", "девятка").
# По заданным номеру масти m (1 <= m <= 4) и номеру достоинства карты k (6 <= k <= 14)
# определить полное название (масть и достоинство) соответствующей карты в виде "Дама пик",
# "Шестерка бубен" и т. п.
#----------------------------------------------------------------------------------------------------
def task_3_2( k, m ):
    suit = { 1: 'пики', 2: 'трефы', 3: 'бубны', 4: 'червы' }
    weight = { 6: 'шестерка', 7: 'семерка', 8: 'восьмерка', 9: 'девятка', 10: 'десятка', 11: 'валет', 12: 'дама', 13: 'король', 14: 'туз' }
    s = list(suit.keys())
    w = list(weight.keys())
    if( (s.count(m) == 0) | (w.count(k) == 0) ):
        print(f"ERROR")
        return
    print(f"{weight[k]} {suit[m]}")

#----------------------------------------------------------------------------------------------------
# Задание 4.2
# Даны два целых числа A и B (A < B). Найти все целые числа, расположенные между данными числами
# (не включая сами эти числа), в порядке их убывания, а также количество N этих чисел.
#----------------------------------------------------------------------------------------------------
def task_4_2(a, b):
    if a >= b:
        print("ERROR")
        return
    l = []
    for i in range(a+1, b):
        l.append(i)
    print(f"list: {l}\nsize {len(l)}")

#----------------------------------------------------------------------------------------------------
# Задание 5.1
# Гипотеза Сиракуз гласит, что любое натуральное число сводимо к единице при следующих
# действиях над ним:
# а) если число четное, то разделить его пополам,
# б) если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.
# Над вновь полученным числом вновь повторить действия a) или б) в зависимости от его четности.
# Рано или поздно число станет равным 1.
#----------------------------------------------------------------------------------------------------
def task_5_1(a):
    if a <= 0:
        print("ERROR")
        return
    while(a != 1):
        if( a % 2 == 0 ):
            a /= 2
        else:
            a = (a * 3 + 1) / 2
        print(f"a = {a}")

#----------------------------------------------------------------------------------------------------
# Задание 5.2
# Начав тренировки, спортсмен в первый день пробежал n км.
# Каждый день он увеличивал дневную норму на y% нормы предыдущего дня.
# Какой суммарный путь пробежит спортсмен за x дней?
#----------------------------------------------------------------------------------------------------
def task_5_2(n , y, x):
    if( n < 0 | y < 0 | x < 1 ):
        print("ERROR")
        return
    s = n
    for i in range(x-1):
        n += n * y / 100
        s += n
    print(f"distance = {s}")

#----------------------------------------------------------------------------------------------------
# Задание 5.3
# Определить, сколько в введенном пользователем числе четных цифр, а сколько нечетных.
#----------------------------------------------------------------------------------------------------
def task_5_3(a):
    odd = honest = 0
    for i in list(str(a)):
        if( int(i) % 2 == 0 ):
            honest += 1
        else:
            odd += 1
    print(f"number {a}\nodd number {odd}\nhonest number {honest}")

#----------------------------------------------------------------------------------------------------
# Задание 5.4
# Написать программу в виде оператора цикла с параметром, обеспечивающий вывод на экран "столбиком"
# всех целых чисел от 10 до 30. Оформить этот фрагмент в виде:
#* а. оператора цикла с предусловием
#* б. оператора цикла с постусловием.
#----------------------------------------------------------------------------------------------------
def task_5_4_a(a, b):
    while a <= b :
        print(f"{a}")
        a += 1

def task_5_4_b(a, b):
    while True:
        print(f"{a}")
        a += 1
        if a <= b:
            break

#----------------------------------------------------------------------------------------------------
# Задание 6.1
# В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64.
# Дано натуральное число n. Как наименьшим количеством таких денежных купюр можно выплатить сумму n
# (указать количество каждой из используемых для выплаты купюр)? Предполагается, что имеется
# достаточно большое количество купюр всех достоинств
#----------------------------------------------------------------------------------------------------
def task_6_1(n):
    d = {1: 0, 2: 0, 4: 0, 8: 0, 16: 0, 32: 0, 64: 0}
    ldk = list(d.keys())
    ldk.sort(reverse=True)
    for i in ldk:
        x = n // i;
        d[i] = x;
        n %= i
        print(f"bill [{i}] number {x}")

#----------------------------------------------------------------------------------------------------
# Задание 7.1
# Напечатать таблицу умножения до n
#----------------------------------------------------------------------------------------------------
def task_7_1(n):
    for i in range(1,n+1):
        print("")
        for j in range(1,n+1):
            if n < 100:
                print("{0:5}".format(i*j), end='')
            else:
                print("{0:10}".format(i*j), end='')

#----------------------------------------------------------------------------------------------------
# Задание 7.2
# У гусей и кроликов вместе 64 лапы.
# Сколько могло быть кроликов и гусей (указать все сочетания, которые возможны)?
#----------------------------------------------------------------------------------------------------
def task_7_2(n):
    for i in range(n):
        if((n - i * 4) // 2 >= 0):
            print("вариант {0:2} - кроликов {1:2} гусей {2:2}".format(i, i, (n - i * 4) // 2))
        else:
            break

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
# Задание 4.1
# Даны два целых числа A и B (A < B). Найти все целые числа, расположенные между данными числами
# (включая сами эти числа), в порядке их возрастания,а также количество N этих чисел.
#----------------------------------------------------------------------------------------------------
def task_4_1(a, b):
    if a >= b:
        print("ERROR")
        return
    l = []
    for i in range(a, b+1):
        l.append(i)
    print(f"list: {l}\nsize {len(l)}")

#----------------------------------------------------------------------------------------------------
# Задание 4.3
# Дано вещественное число A и целое число N (> 0).
# Найти A в степени N: AN = A·A··A (числа A перемножаются N раз)
#----------------------------------------------------------------------------------------------------
def task_4_3(a, n):
    s = 1
    for i in range(1,int(n)+1):
        s *= a
        print(f"{a}^{i} = {s}")
#----------------------------------------------------------------------------------------------------
# Задание 4.4
# Задано натуральные числа от 10 до N. Вывести нечетные кратные пяти числа.
#----------------------------------------------------------------------------------------------------
def task_4_4(n):
    if( n < 10 ):
        n = 10
    l = []
    for i in range(10, int(n)+1):
        if( (i % 2 != 0) & (i % 5 == 0) ):
            l.append(i)
    print(f"numbers {l}")

