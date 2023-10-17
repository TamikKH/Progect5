print("Введите N <= 10")
N=int(input())
if N>10:
    print("Недопустимое число")
if N==1:
    print("Я купил один карандаш")
if N>1 and N<5:
    print("Я купил", N, "карандаша")
if N>4 and N<11:
    print("Я купил", N ,"карандашей")