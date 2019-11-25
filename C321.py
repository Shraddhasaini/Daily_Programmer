time2word = {
    '00': '',
    '0': 'oh',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'fourty',
    '50': 'fifty',
}
def talkingAlarm(x=00)
    hour, minute = s.split(':')
    period = 'am' if int(hour) < 12 else 'pm'
    hour = time2word[str((int(hour) % 12) or 12)]
    try:
        minute = time2word[minute]
    except KeyError:
        t, o = divmod(int(minute), 10)
        minute = '{0} {1} '.format(time2word[str(t*10)], time2word[str(o)])
    return "It's {0} {1}{2}".format(hour, minute, period)

if __name__ == '__main__':
    print talkingAlarm(raw_input('Time: '))
