
import translator as tr

t = tr.Translator()

t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        t.handleAdd(txtIn)
        continue
    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        t.handleTranslate(txtIn)
        continue
    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare? [wildcard]")
        txtIn = input()
        t.handleWildCard(txtIn)
        continue
    if int(txtIn) == 4:
        t.stampaTutto()
        continue
    if int(txtIn) == 5:
        exit("Chiusura del traduttore..\nGrazie e a presto!")