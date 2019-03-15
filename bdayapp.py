import datetime
import time

def print_header():
    print('---------------------------------------')
    print('             Birthday App')
    print('---------------------------------------')
    print()

def get_bday():
    print('Tell us when were you born: ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.datetime(year,month,day)

    return birthday

def days_diff(birthday, now):
    date1 = now
    date2 = datetime.datetime(now.year, birthday.month, birthday.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days

def print_bday_msg(days):
    if days < 0:
        print('Your birthday is in {} days'.format(-days))

    elif days > 0:
        print('Oh your birthday was {} days ago this year, belated Happy Birthday!'.format(days))

    else:
        print('Hey! Happy birthday dear')


def main():
    print_header()
    bday = get_bday()
    now = datetime.datetime.now()
    number_of_days = days_diff(bday, now)
    print_bday_msg(number_of_days)


main()
