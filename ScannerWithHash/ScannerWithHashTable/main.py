from LanguageSpecification import operators, separators, reservedWords
from Scanner import Scanner
from ScannerWithHashTable.FiniteAutomata import FiniteAutomata

if __name__ == '__main__':
    # scanner = Scanner(operators, separators, reservedWords)
    # fileName = input("File name: ")

    # scanner.scan(fileName)

    finiteAutomata = FiniteAutomata()
    finiteAutomata.readAutomata('fa.txt')