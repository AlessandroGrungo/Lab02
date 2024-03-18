import re
class Dictionary:
    def __init__(self, dizionario={}):
        self.dizionario = dizionario

    def addWord(self, entry):
        o = entry.lower().strip().split()
        key = o[0]
        trad = o[1:]

        if len(trad)>0:
            if key in self.dizionario:
                # Utilizzo un set per eliminare duplicati
                trad_set = set(self.dizionario[key])
                trad_set.update(trad)
                self.dizionario[key] = list(trad_set)
                print(f"Traduzioni aggiunte per la parola '{key}': {trad}")
                print(self.dizionario[key])
            else:
                self.dizionario[key] = list(set(trad))
                print(f"Parola '{key}' aggiunta al dizionario con traduzioni: {trad}")
        else:
            print("Non hai specificato traduzioni per la parola")

    def translate(self, query):
        o = query.lower()
        if self.dizionario.get(o) is not None:
            print(f"TRADUZIONE...")
            print(f"{o}: {self.dizionario[o]}")
        else:
            print("Parola sconosciuta, ma se conosci la traduzione aggiungila al dizionario premendo il tasto 1 al prossimo step!")

    def translateWordWildCard(self, query):
        wildCard = query.replace("?", ".")  # Replace "?" with "." to use regex
        risultato = []
        stringa = ""
        for w in self.dizionario.keys():
            if re.search(wildCard, w):
                risultato.extend(self.dizionario.get(w))
        for r in risultato:
            stringa += r+" "
        print(stringa)


    def loadDictionary(self,filename):
        with open(filename, "r") as file:
            for line in file:
                o = line.lower().strip().split()
                self.dizionario[o[0]] = o[1:]

    def stampaTutto(self):
        print("DIZIONARIO ALIENO-ITALIANO (contiene tutte le traduzioni raccolte fino ad oggi)")
        for key, trad in self.dizionario.items():
            print(f"{key}: {trad}")
