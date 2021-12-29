def format_duration(seconds):
    if seconds == 0:
        return 'now'

    readableFormat = ''

    numberOfYears = seconds // 60 // 60 // 24 // 365
    seconds -= numberOfYears * 365 * 24 * 60 * 60

    if numberOfYears > 1:
        readableFormat = f' and {numberOfYears} years'
    elif numberOfYears == 1:
        readableFormat = ' and 1 year'

    numberOfDays = seconds // 60 // 60 // 24
    seconds -= numberOfDays * 24 * 60 * 60

    if numberOfDays > 1:
        readableFormat = readableFormat = readableFormat.replace(' and', ',')
        readableFormat = f'{readableFormat} and {numberOfDays} days'
    elif numberOfDays == 1:
        readableFormat = readableFormat.replace(' and', ',')
        readableFormat = f'{readableFormat} and 1 day'

    numberOfHours = seconds // 60 // 60
    seconds -= numberOfHours * 60 * 60

    if numberOfHours > 1:
        readableFormat = readableFormat.replace(' and', ',')
        readableFormat = f'{readableFormat} and {numberOfHours} hours'
    elif numberOfHours == 1:
        readableFormat = readableFormat.replace(' and', ',')
        readableFormat = f'{readableFormat} and 1 hour'

    numberOfMinutes = seconds // 60
    seconds -= numberOfMinutes * 60

    if numberOfMinutes > 1:
        readableFormat = readableFormat.replace(' and', ',')
        readableFormat = f'{readableFormat} and {numberOfMinutes} minutes'
    elif numberOfMinutes == 1:
        readableFormat = readableFormat.replace(' and', ',')
        readableFormat = f'{readableFormat} and 1 minute'

    if seconds > 1:
        readableFormat = readableFormat.replace(' and', ',')
        readableFormat = f'{readableFormat} and {seconds} seconds'
    elif seconds == 1:
        readableFormat = readableFormat.replace(' and', ',')
        readableFormat = f'{readableFormat} and 1 second'

    if readableFormat[:5] == ' and ':
        return readableFormat[5:]
    elif readableFormat[:4] == ' , ':
        return readableFormat[4:]
