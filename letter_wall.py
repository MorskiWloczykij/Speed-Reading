import random
import string
from fpdf import FPDF

lettersLowercase = list(string.ascii_lowercase)
lettersUppercase = list(string.ascii_uppercase)

selection = input("Lowercase or uppercase? type  l or u ")

letter = lettersLowercase
if selection == 'l':
    letter = lettersLowercase
if selection == 'u':
    letter = lettersUppercase

string = random.choices(letter, k = 1000)    
    
letters = []    
for i in range(5):
    letters.append(letter.pop(random.randrange(0,len(letter),1)))
    


count1 = string.count(letters[0])
count2 = string.count(letters[1])
count3 = string.count(letters[2])
count4 = string.count(letters[3])
count5 = string.count(letters[4])


string = ''.join([str(elem) for elem in string])



pdf = FPDF()  
pdf.add_page()
pdf.set_font("Arial", size = 12)

text = "Letter Wall"
pdf.cell(200, 10, txt = text, 
         ln = 1, align = 'C')

text = "Find and measure time: {}, {}, {}, {}, {}".format(letters[0],letters[1],
                                                          letters[2],letters[3],
                                                          letters[4])
pdf.cell(200, 10, txt = text, 
         ln = 1, align = 'L')

text = string
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')

text = string
pdf.multi_cell(180, 10, txt = '', 
          align = 'L')

text = "{} = {}".format(letters[0], count1)
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')
text = "{} = {}".format(letters[1], count2)
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')
text = "{} = {}".format(letters[2], count3)
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')
text = "{} = {}".format(letters[3], count4)
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')
text = "{} = {}".format(letters[4], count5)
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')




title = input("Filename: ")
pdf.output("{}.pdf".format(title))   

