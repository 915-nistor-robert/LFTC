from LanguageSpecification import operators, separators, reservedWords
from Scanner import Scanner

if __name__ == '__main__':
    scanner = Scanner(operators, separators, reservedWords)
    fileName = input("File name: ")

    scanner.scan(fileName)