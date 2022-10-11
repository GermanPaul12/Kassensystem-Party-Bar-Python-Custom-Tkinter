import datetime as dt


with open('C:/Users/paulg/Documents/Coding/GUI/Zeiterfassung/kassenstand.txt') as f:
    kassenstand = float(f.read())


def check_happy_hour():
    return dt.datetime.now().hour == 22    


class Kasse:
    def __init__(self):
        self.kassenstand = kassenstand


    def getränke_verkauf(self, erlös, kosten):    
        return erlös - kosten
    
    
    def kalkuriere_kosten(self, menge):
        happy = check_happy_hour()
        if happy:
            bier = 2
            wein = 2
            shot = 1
            longdrink = 3
        else:   
            bier = 2
            wein = 2
            shot = 2
            longdrink = 3
        return menge[0] * bier + menge[1] * wein + menge[2] * shot + menge[3] * longdrink    
                                     