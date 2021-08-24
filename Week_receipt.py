### IMPORTS ###
from random import randint
from datetime import datetime, timedelta
from hijri_converter import Gregorian
from pyluach import dates
from repubcal import repubcal
from Texts import media_obj, plan_obj, quotes_obj, rules_obj
from lunarcalendar import Lunar

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

def chinese_zodiac(year):
    animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']

    year -= 1984
    return elements[year//2 % 5] + " " + animals[year % 12]

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


def get_dates(date):
    """
    The point of this function is to return all the dates

    Parameters
    ---------
        date: datetime
            the input date received from from the main function
        CS_chinese, CS_gregorian, CS_hijri, CS_ISO_8601, CS_jacobin, CS_jalali, CS_judean, CS_julian : str
       
        dates_obj: dict
        
    Returns
    ---------
        dates_obj: dict
    """

    # ADD SUPPORT FOR: jalali, julian
    L_ah = Gregorian.fromdate(date).to_hijri()
    Heb = dates.HebrewDate.from_pydate(date)
    S_ah = ''
    Chi = Lunar.from_date(date)

    CS_chinese = ' '.join([ '{}-{}-{}'.format(Chi.year, Chi.month, Chi.day), 'year of the', chinese_zodiac(Chi.year)])
    CS_gregorian = date.strftime('%A %B %Y-%m-%d AD')
    CS_hijri = ' '.join([L_ah.day_name('ar'), L_ah.day_name(), L_ah.month_name('ar'), L_ah.month_name(), '{}-{}-{}'.format(L_ah.year, L_ah.month, L_ah.day) ,  L_ah.notation('ar'), L_ah.notation()])
    CS_ISO_8601 = ' '.join(['-'.join(map( str, date.isocalendar())), 'CE'])
    CS_jacobin = repubcal.RDate.fromisoformat(date.isoformat()).revol_strftime('%rf %rA %rB %rY %ry-%rm-%rd')
    CS_jalali = ''
    CS_judean = ' '.join( [Heb.month_name(True), Heb.month_name(), '{}-{}-{}'.format(Heb.year, Heb.month, Heb.day)])
    CS_julian = ''
    
    dates_obj = {
                'Chinese': CS_chinese, 'Gregorian': CS_gregorian, 'Hijri': CS_hijri, 
                'ISO-8601':  CS_ISO_8601, 'Jacobin': CS_jacobin, 'Jalali': CS_jalali,
                'Judean': CS_judean, 'Julian': CS_julian,
                }

    return dates_obj

def main():
    """
    The main function which iniates the processes to create a notepad daily.

    Parameters
    ---------
        CS_chinese, CS_gregorian, CS_hijri, CS_ISO_8601, CS_jacobin, CS_jalali, CS_judean, CS_julian,  : str
        dates_obj: list
            incorporates all the results from the above calendrical systems.
        Today: str
            The date today in ISO format
        Tomorrow: str
            The date tomorrow ISO format

    """

    Today = datetime.now().date()
    Tomorrow = datetime.now().date() + timedelta(days=1)

    if not read_sequence('.'.join([Today.isoformat(), 'txt'])):
        print("Creating today's daily...")
        write_sequence(Today.isoformat(), get_dates(Today))
    else:
        print("Creating tomorrow's daily...")
        write_sequence(Tomorrow.isoformat(), get_dates(Tomorrow))




if __name__ == '__main__':
    main()

else:
    print('This is imported as: ' + __name__)
