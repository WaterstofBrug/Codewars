def solution(args):
    formattedList = []
    for position, number in enumerate(args):
        if position >= 1:
            if args[position - 1] == number - 1:
                if type(formattedList[-1]) is list:
                    formattedList[-1][1] = str(number)
                else:
                    formattedList[-1] = [formattedList[-1], str(number)]
            else:
                formattedList.append(str(number))
        else:
            formattedList.append(str(number))

    for pos, obj in enumerate(formattedList):
        if type(obj) is list:
            if abs(int(obj[1]) - int(obj[0])) > 1:
                formattedList[pos] = '-'.join(obj)
            else:
                formattedList[pos] = ','.join(obj)

    return ','.join(formattedList)


print(solution([-4,-3,-2,-1,2,10,15,16,18,19,20]))
