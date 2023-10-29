import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


recenzja = """Ciekawy film.
Był dobry i podobał mi się bo był niezły i ok,
ale nie podobały mi się niektóre ujęcia, a jeden moment był wręcz nudny i nie lubiłem gry jednego aktora, nie lubiłem też muzyki. """

print("Recenzja: ", recenzja)
interpunkcja = "._!,:;-"

# usuwam interpunkcję
for znak in interpunkcja:
    recenzja = recenzja.replace(znak, "")  
                
rec = [recenzja]
def convert(list):
    return (list[0].split()) 

opinia = convert(rec)

# otwieram listę słów pozytynych
with open('pozytywy.txt', 'r', encoding='utf-8') as f:
    pozlines = f.readlines()

poztxt=convert(pozlines)


# otwieram listę słów negatywnych
with open('negatywy.txt', 'r', encoding='utf-8') as f:
    neglines = f.readlines()

negtxt=convert(neglines)

# liczę słowa pozytywne
licznikpoztxt = 0
for i in poztxt:
    for j in opinia:
            if i == j:
                licznikpoztxt = licznikpoztxt+1
                
#print("Całkowita liczba pozytywów z txt: ", licznikpoztxt)        
            
    
    
# liczę słowa negatywne
liczniknegtxt = 0
for i in negtxt:
    for j in opinia:
            if i == j:
                liczniknegtxt = liczniknegtxt+1 
                
#print("Całkowita liczba negatywów z txt: ", liczniknegtxt)



# nie + pozytywne określenie to negatyw
nie_poz = ["nie podobały", "nie lubiłem", "nie lubię"]

# słowa z listy nie_poz występujące w recenzji
nie_poz = [x for x in nie_poz if x in recenzja]


licze = 0
for i in nie_poz:
    licze = nie_poz.count(i)
    licze = licze+1
    

całe_poz = licznikpoztxt - licze

liczba = len(nie_poz)

całe_neg = liczba+liczniknegtxt

print("Całkowita liczba pozytywów", całe_poz)
print("Całkowita liczba negatywów", całe_neg)
wynik = całe_poz-całe_neg
print("Wynik: ", wynik)
if wynik == 0:
    op = "neutralna"
elif wynik > 0:
    op = "pozytywna"
elif wynik < 0:
    op = "negatywna"
print("Opinia raczej ", op)
