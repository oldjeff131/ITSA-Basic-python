month,day=map(int,input().split())
if month==1:
    if day<21:
        print('Capricorn')
    else:
        print('Aquarius')
elif month==2:
    if day<19:
        print('Aquarius')
    else:
        print('Pisces')
elif month==3:
    if day<21:
        print('Pisces')
    else:
        print('Aries')
elif month==4:
    if day<21:
        print('Aries')
    else:
        print('Taurus')
elif month==5:
    if day<22:
        print('Taurus')
    else:
        print('Gemini')
elif month==6:
    if day<22:
        print('Gemini')
    else:
        print('Cancer')
elif month==7:
    if day<23:
        print('Cancer')
    else:
        print('Leo')
elif month==8:
    if day<24:
        print('Leo')
    else:
        print('Virgo')
elif month==9:
    if day<24:
        print('Virgo')
    else:
        print('Libra')
elif month==10:
    if day<24:
        print('Libra')
    else:
        print('Scorpio')
elif month==11:
    if day<23:
        print('Scorpio')
    else:
        print('Sagittarius')
elif month==12:
    if day<23:
        print('Sagittarius')
    else:
        print('Capricorn')

print('\n')