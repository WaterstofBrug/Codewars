def solution(string, markers):
    erasing = False
    string = list(string)
    for i, char in enumerate(string):
        if char in markers:
            erasing = True
        elif char == "\n":
            erasing = False

        if erasing:
            string[i] = ''

    removeLastSpace = lambda x: x[:-1] if x[-1] == ' ' else x

    return removeLastSpace(''.join(string).replace(' \n', '\n')) if len(string) > 0 else ''.join(string).replace(' \n', '\n')


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
