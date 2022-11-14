reservedWords = ['var', 'if', 'else', 'in', 'every', 'const', 'break', 'null', 'write', 'read', 'while']
operators = ['+', '-', '*', '/', ':', '<', '<=', '==', '>=', '>','%', '&', '!', '!=',
             '||']
separators = ['[', ']', '{', '}', ';', ':', ' ','(',')','\n']
allThree = separators + operators + reservedWords

def find_pos(elem):
    index = 0
    for element in allThree:
        if elem == element:
            return index
        index += 1