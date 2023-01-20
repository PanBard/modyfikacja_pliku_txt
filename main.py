import codecs


nazwa_pliku_pierwotnego = "drillznumerkami.txt"

nazwa_nowego_pliku = "nowyplikdrill.txt"



plik_nowy = codecs.open(nazwa_nowego_pliku,'a',"utf-8")


with codecs.open(nazwa_pliku_pierwotnego,'r',"utf-8") as file:
    lines = list(file)
    licznik = 1
    modyfikowane_zdanie = ""
    numer_z_pliku =""

    for sentence in lines:
        
        modyfikowane_zdanie = ""
        if sentence.find('[#') == 0:
            for x in range(len(sentence)) :
                if (sentence[x] == '[') and (sentence[x+1]=='#'):
                    for z in range(len(sentence)):
                        if sentence[x+z].isnumeric():
                            numer_z_pliku += sentence[x+z]
                        if sentence[x+z] == ']':
                            break


            for x in sentence:
                modyfikowane_zdanie += x
                if x == ']':
                    modyfikowane_zdanie += " "+numer_z_pliku
                    numer_z_pliku = ''
            plik_nowy.write(modyfikowane_zdanie)
        else: plik_nowy.write(sentence)

      


plik_nowy.close()
