### IMPORTS ###
from random import randint
from datetime import datetime, timedelta
from Texts import media_obj, plan_obj, quotes_obj, rules_obj
import calendrical

### FUNCTIONS ###
def read_sequence(title):
    """Searches for the correct file and returns True or False depending on success or failure.
    
     Parameters
     ----------
     title: str
        The name of the file as instructed by the current date.

     Returns
     ---------- 
     Boolean

    """

    print("Reading today's daily...")
    try:
        with open(title, mode='rt', encoding='utf-8') as r:
            print("Success !")
            return True
    except:
        print("Failure !")
        return False


def write_sequence(date, date_obj):
    """ This writes the daily by using a for loop to write out the sections and ensure they are divided by a long divider.

    Parameters
    ----------
    title: str
        What the daily will be called in the end.
    dates: str
        Gregorian date in ISO format
    date_obj: dict
        A collection of dates
     box: list
        A list that determines the order of what will be written out.
    """

    try:
        print('Opening Connection now...')
        w = open('.'.join([date, 'txt']), 'wt', encoding='utf-8')
        
        print("Creating the daily for {}...".format(date))
        box = ['words', 'dates', media_obj, plan_obj, 'thoughts', 'rules']

        for item in box:
            
            if item == 'dates':
                w.writelines(["\n\n—————————  Dates \n"])
                w.writelines(['- In the Gregorian calendar: ', date_obj['Gregorian'], '\n'])
                w.writelines(['- In the Qamari Hijri calendar: ', date_obj['Hijri'], '\n'])
                w.writelines(['- In the Shamsi Hijri calendar: ', date_obj['Jalali'], '\n'])
                w.writelines(['- In the ISO-8601 calendar: ', date_obj['ISO-8601'], '\n'])       
                w.writelines(['- In the Jacobin calendar: ', date_obj['Jacobin'], '\n'])
                w.writelines(['- In the Judean calendar: ', date_obj['Judean'], '\n'])
                w.writelines(['- In the Yin calendar: ', date_obj['Chinese'], '\n'])
                                
                continue
                # REMOVE ABOVE CONTINUE ONCE ALL DATES HAVE BEEN ADDED.
                #
                
                for i in date_obj:
                    w.write('\n')
                    w.writelines(i)
                    w.write('\n')
                    print(f'The date by this calendar is {i}')
                
                continue

            if item == 'thoughts':
                w.writelines(['\n — Thoughts and Things for the date of ',str(date), ' —  \n \n'])
                continue

            if item == 'rules':
                w.writelines([ rules_obj[0], rules_obj[randint(1, len(rules_obj) - 1)] ])
                continue
            
            if item == 'words':
                w.writelines([ quotes_obj[0], quotes_obj[randint(1, len(quotes_obj) - 1)] ])
                continue
                
            w.writelines(item)
        
    finally:
        print("Closing connection now...")
        w.close()


def main():
    """
    The main function which iniates the processes to create a notepad daily.

    Parameters
    ---------
        Today: str
            The date today in ISO format
        Tomorrow: str
            The date tomorrow ISO format

    """

    Today = datetime.now().date()
    Tomorrow = datetime.now().date() + timedelta(days=1)

    if not read_sequence('.'.join([Today.isoformat(), 'txt'])):
        print("Creating today's daily...")
        write_sequence(Today.isoformat(), calendrical.get_dates(Today))
    else:
        print("Creating tomorrow's daily...")
        write_sequence(Tomorrow.isoformat(), calendrical.get_dates(Tomorrow))



if __name__ == '__main__':
    main()

else:
    print('This is imported as: ' + __name__)
