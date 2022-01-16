from copy import copy

def main():
    files = [open("alle nederlandse woorden\OpenTaal-210G-basis-gekeurd.txt", 'r'),
             open("alle nederlandse woorden\OpenTaal-210G-basis-ongekeurd.txt", 'r'),
             open("alle nederlandse woorden\OpenTaal-210G-flexievormen.txt", 'r'),
             open("alle nederlandse woorden\OpenTaal-210G-verwarrend.txt", 'r')]

    elementsOneLetter = ['h', 'b', 'c', 'n', 'o', 'f', 'p', 's', 'v', 'y', 'i', 'w', 'u', 'k']
    elementsTwoLetters = ['he', 'li', 'be', 'na', 'mg', 'ca', 'sc', 'rd', 'sr', 'cs', 'ba', 'la', 'fr', 'ra', 'ac',
                          'ti', 'zr', 'hf', 'rf', 'nb', 'ta', 'db', 'cr', 'mo', 'sg', 'mn', 'tc', 're', 'bh', 'fe',
                          'ru', 'os', 'hs', 'co', 'rh', 'ir', 'mt', 'ni', 'pd', 'pt', 'ds', 'cu', 'ag', 'au', 'rg',
                          'zn', 'cd', 'hg', 'cn', 'al', 'ga', 'in', 'ti', 'nh', 'si', 'ge', 'sn', 'pb', 'fl', 'as',
                          'sb', 'bi', 'mc', 'se', 'te', 'po', 'lv', 'cl', 'br', 'at', 'ts', 'ne', 'ar', 'kr', 'xe',
                          'rn', 'og', 'ce', 'pr', 'nd', 'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb',
                          'lu', 'th', 'pa', 'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no', 'lr']

    longestWords = []
    longestWordLength = 0

    for file in files:
        for word in file.readlines():
            usedElements = []
            word_C = copy(word)
            for element in elementsTwoLetters:
                if element in word_C:
                    #print(element, 'in', word_C)
                    word_C = word_C.replace(element, '--')
                    #print(element, 'removed now', word_C)
                    usedElements.append(element)

            for element in elementsOneLetter:
                if element in word_C:
                    word_C = word_C.replace(element, '-')
                    usedElements.append(element)

            #print(word, '-->', word_C)

            word_C = word_C.replace(' ', '')
            word_C = word_C.replace("'", '')
            word_C = word_C.replace("-", '')

            if len(word_C) == 1:
                # print(word, '-------------------------------------------------')
                if len(word) > longestWordLength:
                    longestWords = []
                    longestWordLength = len(word)
                    longestWords.append((word, usedElements))
                elif len(word) == longestWordLength:
                    longestWords.append(word)
                else:
                    pass
            else:
                #print(word, f'left is:{word_C}): len is {len(word_C)}')
                pass

    print(f'longest words are {longestWords} with a length of {longestWordLength} characters')



    for file in files:
        file.close()

if __name__ == '__main__':
    main()
