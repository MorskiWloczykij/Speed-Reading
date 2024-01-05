import random
import string
from fpdf import FPDF

digit = string.digits
digit = [int(x) for x in str(digit)]


string = random.choices(digit, k = 1000)    
    
digits = []    
for i in range(5):
    digits.append(digit.pop(random.randrange(0,len(digit),1)))
    


count1 = string.count(digits[0])
count2 = string.count(digits[1])
count3 = string.count(digits[2])
count4 = string.count(digits[3])
count5 = string.count(digits[4])


string = ''.join([str(elem) for elem in string])



pdf = FPDF()  
pdf.add_page()
pdf.set_font("Arial", size = 12)

text = "Letter Wall"
pdf.cell(200, 10, txt = text, 
         ln = 1, align = 'C')

text = "Find and measure time: {}, {}, {}, {}, {}".format(digits[0],digits[1],
                                                          digits[2],digits[3],
                                                          digits[4])
pdf.cell(200, 10, txt = text, 
         ln = 1, align = 'L')

text = string
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')

text = string
pdf.multi_cell(180, 10, txt = '', 
          align = 'L')

text = "{} = {}".format(digits[0], count1)
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')
text = "{} = {}".format(digits[1], count2)
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')
text = "{} = {}".format(digits[2], count3)
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')
text = "{} = {}".format(digits[3], count4)
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')
text = "{} = {}".format(digits[4], count5)
pdf.multi_cell(180, 10, txt = text, 
          align = 'L')




title = input("Filename: ")
pdf.output("{}.pdf".format(title))   

