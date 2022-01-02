import random as random


def passwordGenerator (amountCharacter, s_Characters, numbers):
        password = ''

        for i in range(amountCharacter):
            charType = random.randint(0, 4)
            if charType == 1:
                password = ''.join((password, chr(random.randint(65, 90))))
            elif charType == 2:
                password = ''.join((password, chr(random.randint(97, 122))))
            elif charType == 3 and s_Characters:
                password = ''.join((password, chr(random.randint(35, 47))))
            elif charType == 4 and numbers:
                password = ''.join((password, chr(random.randint(48, 57))))
            else:
                password = ''.join((password, chr(random.randint(65, 90))))

        return password


print(passwordGenerator(25, True, True))
