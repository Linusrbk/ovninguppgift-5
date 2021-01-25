
text=("Saa haer aer min oe gjord.")#text med amerikanskt keyboard 

text=text.lower().replace("aa","å")#tar bort där det är aa i texten och her ut å istället
text=text.replace("ae","ä")#samma sak som förra men med ae och ä istället
text=text.replace("oe","ö")#samma sak som dom två innan men med oe och ö istället
print(text)#visar den nya och förbättrade texten 
