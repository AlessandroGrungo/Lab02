from dictionary import Dictionary


class Translator:

    def printMenu(self):
        print("______________________________\n" +
              "   Translator Alien-Italian\n"+
              "______________________________\n" +
              "1. Aggiungi nuova parola\n" +
              "2. Cerca una traduzione\n" +
              "3. Cerca con wildcard\n" +
              "4. Stampa tutto il Dizionario\n" +
              "5. Exit\n"+
              "______________________________\n")

    def __init__(self, dizionario=Dictionary()):
        self.dizionario = dizionario
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        self.dizionario.loadDictionary(dict)

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.dizionario.addWord(entry)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        self.dizionario.translate(query)

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        self.dizionario.translateWordWildCard(query)

    def stampaTutto(self):
        self.dizionario.stampaTutto()