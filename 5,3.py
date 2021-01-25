import datetime, time#tar från libraryt dom här modulerna så man kan programera med saker som handlar om tid
dt=datetime.datetime.now()#detta är för att ge den tid som är just nu
personnummer=input('skriv ditt personnummer')#(input('vad är ditt personnummer?'))#för att få reda på nummret man behöver för denna övning

nästsistanummer=personnummer[-2]#för att leta reda på numret som är viktigt
if nästsistanummer == 0 or 2 or 4 or 6 or 8:#gör att för att se om personnummeret fissar om det är en kvinnas personnummer
    print("congratulation you're a girl!")#skrivet ut texten
elif nästsistanummer ==1 or 3 or 5 or 7 or 9:#gör samma sak som förra men för män istället
    print("congratulation you're a boy!")#skrivet ut texten

ålder=dt.strptime(personnummer[0:6],'%y%m%d')#används för att överföra textens 6 första tal till det år månad och dag det motsvarar
dagar=abs((ålder - dt).days)#minskar åldern från ens personnummer med nutiden för att få fram ens ålder i dagar
år=int(dagar/365)#används för att dela dagarna till så manga år man kan dela det till
månad=int(dagar%365/31)#samma som år fast med månader
dag=int(dagar%365%31)#samma som år fast med dom dagar som blir kvar
print('du är',år,'år',månad,'månader och',dag,'dagar')#för att visa hur många år månader och agar du är ifrån ens personnummer

