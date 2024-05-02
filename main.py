import random
def alphavit(z,A,v,s):
    psw = ''
    if a==20 and b==5:
        z=z+1
    for i in range(z):
        index = random.randint(0, len(A) - 1)
        psw += A[index]
    if b==1 or b==3 or b==4:
        if a==15 and b==1:
            z=z+1
        for i in range(z):
            index = random.randint(0,9)
            psw += str(index)
    if b==3 or b==4 or b==5:
        if a==20 and b==3 or a==20 and b==4:
            z=z+2
        elif a==10 and b==3 or a==10 and b==4 or a==10 and b==5:
            z=z+1
        elif a==20 and b==5:
            z=z-1
        for i in range(z):
            index = random.randint(0, len(v) - 1)
            psw += v[index]
    psw=list(psw)
    random.shuffle(psw)
    psw="".join(psw)
    if b==4 or b==5:
        s = random.choice(s)
        psw=str(psw)+str(s)
    return psw

('Привет я Генератор сложных паролей,я помогу тебе с выбором пароля')
print('Выбери длину пароля:10 либо 15 либо 20 символов')
a=int(input())
print('Выбери тип пароля')
print('1 - буквы разного регистра и цифры')
print('2 - только буквы разного регистра')
print('3 - буквы, цифры и спецсимволы')
print('4 - буквы, цифры, спецсимволы и популярные слова')
print('5 - буквы, спецсимволы и популярные слова')
b=int(input())
A = 'QWERTYUIOPASDFGHJKLZXCVBNM'
v = '!@#$%^&*()'
s = ['CAT','DOG','GUN','END','WAS','SIT']
if a==10:
    if b==2:
        print(alphavit(10,A,v,s))
    if b==1:
        print(alphavit(5,A,v,s))
    if b==3:
        print(alphavit(3,A,v,s))
    if b==4:
        print(alphavit(2,A,v,s))
    if b==5:
        print(alphavit(3,A,v,s))
if a==15:
    if b==2:
        print(alphavit(15,A,v,s))
    if b==1:
        print(alphavit(7,A,v,s))
    if b==3:
        print(alphavit(5,A,v,s))
    if b==4:
        print(alphavit(4,A,v,s))
    if b==5:
        print(alphavit(6,A,v,s))
if a==20:
    if b==2:
        print(alphavit(20,A,v,s))
    if b==1:
        print(alphavit(10,A,v,s))
    if b==3:
        print(alphavit(6,A,v,s))
    if b==4:
        print(alphavit(5,A,v,s))
    if b==5:
        print(alphavit(8,A,v,s))