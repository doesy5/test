from numpy import sign


def add(x, y):
    print(int(x)+int(y))
def subt(x, y):
    print(int(x)-int(y))
def mult(x, y):
    print(int(x)*int(y))
def div(x, y):
    print(int(x)/int(y))
def exp(x, y):
    print(x ** y)
def fact(x):
    loop1 = x - 1
    loop2 = x
    while loop1 > 0:
        loop2 = loop2*loop1
        loop1 -= 1
    print(loop2)
def linA(alg):
    sign = int(alg.find("x"))+1
    if alg[sign] == "+":
        ans = int(alg[alg.find("=")+1:])
        new = str(alg[:alg.find("=")])
        numbs = new.split("x+")
        x = (ans-int(numbs[1]))/int(numbs[0])
        print(x)
    elif alg[sign] == "-":
        ans = int(alg[alg.find("=")+1:])
        new = str(alg[:alg.find("=")])
        numbs = new.split("x-")
        x = (ans+int(numbs[1]))/int(numbs[0])
        print(x)
    elif "/" in alg:
        ans = int(alg[alg.find("=")+1:])
        if "+" in alg:
            new = int(alg[alg.find("/")+1:alg.find("+")])
            x = (ans-int(alg[alg.find("+")+1:alg.find("=")]))*new
            print(x)
        elif "-" in alg:
            new = int(alg[alg.find("/")+1:alg.find("-")])
            x = (ans+int(alg[alg.find("-")+1:alg.find("=")]))*new
            print(x)
        else:
            print("Error")
    else:
        print("Error")
def linG(func, low, high):
    from matplotlib import pyplot as pyl
    x_values = []
    y_values = []
    if "+" in func:
        funcNum = func.split("x+")
        mult = int(funcNum[0])
        add = int(funcNum[1])
        x = [low, high]
        advLow = (low*mult)+add
        advHigh = (high*mult)+add
        y = [advLow, advHigh]
        pyl.plot(x, y)
        pyl.show()  
    elif "-" in func:
        funcNum = func.split("x-")
        mult = int(funcNum[0])
        subt = int(funcNum[1])
        x = [low, high]
        advLow = (low*mult)-subt
        advHigh = (high*mult)-subt
        y = [advLow, advHigh]
        pyl.plot(x, y)
        pyl.show()  