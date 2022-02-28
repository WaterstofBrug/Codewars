def get_pins(observed):
    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['', '0', '']]

    numbers = []

    for i, number in enumerate(observed):
        numbers.append([number])
        numbers[i].append(((int(number)-1) // 3, (int(number)-1) % 3))

    possibilities = []

    for number in numbers:
        itt = []
        itt.append(number[0])
        try: itt.append(keypad[number[1][0]][number[1][1] + 1])
        except: pass
        try: itt.append(keypad[number[1][0]][number[1][1] - 1])
        except: pass
        try: itt.append(keypad[number[1][0] + 1][number[1][1]])
        except: pass
        try: itt.append(keypad[number[1][0] - 1][number[1][1]])
        except: pass

        for i in itt:
            if i == '':
                itt.remove(i)

        possibilities.append(itt)

    possibleCombinations = []

    def varyingNestedForLoops(rangeLoop, varNested):
        def loop(rangeLoop):
            prints = []
            for x in range(rangeLoop):
                prints.append(x)
            return prints

        b = []
        for i in range(varNested):
            b.append(loop(rangeLoop))

        return b


    print(varyingNestedForLoops(4, 2))
    return -1


print(get_pins('11'))
