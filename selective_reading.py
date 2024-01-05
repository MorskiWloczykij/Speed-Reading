import random
from fpdf import FPDF

def switchInputLength(num):
    if num == 1:
        return random.randrange(0,9,1)
    elif num == 2:
        return random.randrange(10,99,1)
    elif num == 3:
        return random.randrange(100,999,1)
    elif num == 4:
        return random.randrange(1000,9999,1)
    elif num == 5:
        return random.randrange(10000,99999,1)
    else:
        print("max length is 5") 
        return 0
    
def switchExcerciseLength(enum,nnum):
    if enum < 5*nnum:
        print("Excersise too short: should be at least 5 times longer than number")
    else:
        return enum
   
def generateNumberArray(eL,nL,nOO):
    nA = []
    for number in range(0,eL-nL*nOO):
        nA.append(switchInputLength(1))
    return nA, len(nA)
    
def generateIndexNumber(nOO, nA):
    iN = []
    for number in range(0,nOO):
        iN.append(random.randrange(0,nA,1))
    return iN
   
ranger = int(input("Number of excercises: "))

numbersLength = int(input("Length of number: "))
excerciseLength = int(input("Length of excercise: "))
numberOfOccurences = int(input("Number of occurences: "))
numbers = [switchInputLength(numbersLength) for number in range(ranger)]
length = switchExcerciseLength(excerciseLength,numbersLength)

numberArray = [generateNumberArray(excerciseLength,numbersLength,numberOfOccurences) for array in range(ranger)] 
indexNumber = [generateIndexNumber(numberOfOccurences, numberArray[0][1]) for index in range(ranger)]

for i in range(ranger):
    for j in indexNumber[i]:
        numberArray[i][0].insert(j,numbers[i])

excersiseNumber = []
for i in range(ranger):
    excersiseNumber.append(''.join([str(elem) for elem in numberArray[i][0]]))    

pdf = FPDF()  
pdf.add_page()
pdf.set_font("Arial", size = 12)

text = "Selective Reading"
pdf.cell(200, 10, txt = text, 
         ln = 1, align = 'C')

text = "Parameters:"
pdf.cell(200, 10, txt = text, 
         ln = 1, align = 'L')

text = "Number length = {}".format(numbersLength)
pdf.cell(200, 10, txt = text, 
         ln = 1, align = 'L')

text = "Number of occurences = {}".format(numberOfOccurences)
pdf.cell(200, 10, txt = text, 
         ln = 1, align = 'L')

pdf.cell(200, 10, txt = ' ', 
         ln = 1, align = 'L')

for i in range(ranger):
    text = "{}: {}".format(numbers[i], excersiseNumber[i])
    pdf.cell(200, 10, txt = text, 
             ln = 1, align = 'L')
    pdf.cell(200, 10, txt = ' ', 
             ln = 1, align = 'L')
    
title = input("Filename: ")
pdf.output("{}.pdf".format(title))   


