import random
""""
loops = 0
while loops != 100:
    loops += 1
    print(loops)

a = 20/(4*2)
print(a)

b = 11.5 % 3
print(b)

c = 2
d = "2"
print(c, d)

flo = 3, 432432424324234252353243243243253253254534543543534534543
e = type(c)
f = type(d)
g = type(flo)
print("\n", e, "\n", f, "\n", g, "\n")

print(27//26) # / outputs float // outputs int

mod = 32876445688
print(mod % 100)


if a <= b: # < eller > måste vara före =
    print("testy")

nummera = 7
nummerb = 10.56
summa = 0

loop = 0
while loop == 0:
    try:
        nummerb = int(nummerb)         # converts data to specified type, int in this case
        summa = nummera + nummerb
        print(summa)
        loop += 1
    except:
        print("Only numbers")

nummer1 = 20
nummer2 = 0
summa2 = 0
if nummer1 != 0 and nummer2 != 0 and (nummer1/nummer2==5): #guard statement
    print(nummer1/nummer2)
    print("hej")

"""

testv = "banan"
overtime = 0
totalpayovertime = 0
totalpay= 0
overtimepay = 1.5
notcorrect = 0
while notcorrect == 0:
    #input from user should be here when i find out how to take input
    pay = (input("Timlön tack\n"))
    hours = (input("Timmar per vecka\n" ))
    try:
        pay =int(pay)
        hours =int(hours)
        if hours >= 0 and hours >40 and pay >= 0:
            overtime = hours % 10
            totalpayovertime = (pay*(hours-overtime))+(pay*overtime*overtimepay)
            print("veckolön på",totalpayovertime*4,"kr.")
            notcorrect = notcorrect + 1
        elif hours >= 0 and hours <=40 and pay >=0:
            totalpay = (pay*hours)
            print("Månadslön på",totalpay*4,"kr.")
            notcorrect = notcorrect + 1
        else:
            print("positiva tal, tack")
    except:
        print("only numbers, compadre.")


'''
conv = int(32.73)
print(conv)

num = (3,5,7)
for i in range(4):
    print("runda nr",i)
    slumpnummer = random.choice(num)
    print(slumpnummer)



def rantry():
    print("nummer 1")
    print("nummer 2")
    print("nummer 3")

def rantry_repeat():
    rantry()
    rantry()

rantry_repeat()

def print_twice(pot):
    print(pot)
    print(pot)

print_twice(pay)

def plus(plus1, plus2): #takes 2 arguements
    thiswillbereturned = plus1 + plus2  #when called this will add the arguments and return them
    return thiswillbereturned  #specifies which variable to return

funk = plus(-2,7)
print (funk)
'''