import random
def alphavit(a,b,d,f,s):
    psw = ''
    for i in range(b):
        index = random.randint(0, len(A) - 1)
        psw += A[index]
    for i in range(a):
            index = random.randint(0,9)
            psw += str(index)
    for i in range(d):
            index = random.randint(0, len(v) - 1)
            psw += v[index]
    psw=list(psw)
    random.shuffle(psw)
    psw="".join(psw)
    for i in range(f):
        h = random.choice(s)
        psw=str(psw)+str(h)
    return psw
print('Привет я Генератор сложных паролей')
while True:
    print('Сколько вы хотите использовать цифр в пароле?')
    a=int(input())
    print('Сколько вы хотите использовать букв в пароле?')
    b=int(input())
    print('Сколько вы хотите использовать спец символов в пароле?')
    d=int(input())
    print('Сколько вы хотите использовать слов в пароле?')
    f=int(input())
    A = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    v = '!@#$%^&*()'
    s = ['CAT','DOG','GUN','END','WAS','SIT']
    print(alphavit(a,b,d,f,s))
    print('Если вы хотите продолжить использование программы введите любую цифру если хотите закончить введите 1')
    g=int(input())
    if g==1:
        break