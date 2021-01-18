import datetime, time
personnummer=(input('vad är ditt personnummer?'))#för att få reda på nummret man behöver för denna övning
nästsistanummer=personnummer[-2]#för att leta reda på numret som är viktigt
if nästsistanummer == 0 or 2 or 4 or 6 or 8:#gör att för att se om personnummeret fissar om det är en kvinnas personnummer
    print("congratulation you're a girl!")#skrivet ut texten
elif nästsistanummer ==1 or 3 or 5 or 7 or 9:#gör samma sak som förra men för män istället
    print("congratulation you're a boy!")#skrivet ut texten
ålder=personnummer[0:6]
#ska göra så man kan se hur gammal man är sida 96-97  från sitt personnummer