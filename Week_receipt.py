### IMPORTS ###
from random import randint
from datetime import datetime, timedelta
from hijri_converter import Hijri, Gregorian
from pyluach import dates
from repubcal import repubcal

media_obj = """
—————————  Mediums
——— Visual
- 

——— Aural
- Surah Yaseen

——— Academical
-
 
——— Epistorical
- StashAway's_YPFP  : ( c.2 | p.30 | para.0 )
- Memoirs_Napolean  : ( b.2 | c.25 | p.653  | para.0 ) 

- EIE.: ( lesson.1 | c.1 | u.1 ) [Web Only]
- AL.P: ( c.1 | p.047 | para.0 ) [SPL only] {252}
- GB.C: ( c.8 | p.183 | para.0 ) [SPL only] {320}
- GM.B: ( c.4 | p.140 | para.0 ) [SPL only] {153}
- KI.F: ( c.11 | p.130 | para.0 ) [SPL only] {891}
- MG.E: ( c.9 | p.103 | para.0 ) [SPL only] {153}
- HA.L: ( part.1 | c.4 | p.75 | para.0 ) [SPL only] {306}
- TA.S: ( part.2 | c.4 | p.143 | para.1 ) [SPL only] [323}
 
——— Interactive 
- Chess.com:  Rapid score [1127]
- Chess24  :  Rapid score [ ]  
- Lichess  :  Rapid score [1578]  
"""

plan_obj ="""
—————————  Plan
——————	Ehi's has beans
 I Went Bed:  <#>  Slept:
 I Left Bed:  <#>  Awoke: 

——— Progress and Obligations
Essentialising:
Exercisings:
Plannings:
Readings:
Writings:

Academics: Paused.
Shqip:
Books:
Chess:
Code:

Project:
Dailies:
Prayer:
Sleep:

Review Yesterday:
Plan for Today: . Stick to the Dopamine Detox. No V.games, no mindless entertainment, no searching or scrolling for novelty.
Review Today:
Plan for tomorrow:

al-Awal: 
Kabir:
Sagir: Read, Clean, Listen, Learn, Journal, SRS, Chess.

{Partially or in full}
Read         : , etc.
Downloaded   : , etc.
Played       : , etc.
Writen       : , etc.
Organised    : , etc.
Learnt       : , etc.
Watched      : , etc.
Listened     : , etc.
Ate & Drank  : , etc.
Travelled    : , etc.

——— Trackers, Trackers and I like trees.
Walk: [/1.5] hours.
Drink: [/7] cups of water.

Write   Shq: [/3] sentences.
Memrise Shq: [/5] times.

Chess   playing: [/1] game(s).
Chess  puzzling: [/8] tactics.

Prayer praying: [/5] prayers.
Project doing: [/1] item(s).

——————	Ehi's Agenda
Plan -  


——— Make this thing. xDONEx ()

——— Do things. …In progress… ()
Albanian: Review Ankis.
Albanian: Review Memrises.
Albanian: Talked in albanian for a minute.
Albanian: Wrote 10 words of the Albanian dictionary.
Albanian: Journaled one paragraph about my day or an event in Albanian.

Do an Intellect.
Journaled.

BETTER_BROCHURE: Watch Udemy Email thing. # 2 sets of 30 hour reps. FIRST 
BETTER_BROCHURE: Watch Udemy Email thing. # 2 sets of 30 hour reps. SECOND

BETTER_BROCHURE: Check-up, and assessment. [ PRIORITY HIGH ]
BETTER_BROCHURE: Deny work or create tally.

EHI_INCOME: Check-up, and assessment. [ PRIORITY MEDIUM ]
EHI_INCOME: Deny work or create tally.

AUTO_INVOICE: Check-up, and assessment. [ PRIORITY MEDIUM ]
AUTO_INVOICE: Deny work or create tally.

_: Check-up, and assessment.
_: Deny work or create tally.
#NON-TASK: Example Example.

Article: Read: _.
Book: Read: _.
Essay: Watched: _.
Lecture: Listened to: _.
Podcast: Listened to: _.

Collect some articles from _.
Collected Terms and takeaways.
Cliped Graphs, functions, etc.
Described in a mere sentence: _.
Bookmarked sections.
Formed Notes, Critique, Expounds, etc.

——— Stop being awesome. ~denied~ (Delete this instead)

——— Tomorrow is a day. >deffered> (Copy of what is left of the doing, usually)

——— Be finished. -failed- () 
 
 
Make my bed.
Check the Calendar.
Fill in Ribbit Tracker and the underneath the keyboard.
Plan out the day/part of it.

Make the next thing.
Evaulate today in Colornote.
Write what you expect to do tomorrow in as short a sentence as possible.

Go through emails: Main.
Go through emails: Newsletters.

Bathe ma bodeh.
Brush my teeth – (1st) Morning.
Brush my teeth – (2nd) Evening.

Wear Pant set B.
Pray Fajr.
Pray Zuhr.
Pray Asr.
Pray Maghrib.
Pray Isha.
Wear Pant set C.

Book: Read: Epistorical[i]: 1 chapter or 10 pages.
Book: Read: Epistorical[ii]: 1 chapter or 10 pages.

Voice: Talk to birds.
Voice: Tongue & pitch exercises.
Voice: Speech practice.
Voice: Recite the first 12 ayaat of Surah Ya-seen.
Voice: Repeat that paragraph by Sir Humphrey of Yes, Minister.

Attempt memorization of oral[i]
Watch: That Albanian show. (1 ep.)

SHQ: Shadow language:.
SHQ: Read: Epistorical[E.I.E]: 1 unit or sub-unit.

Play Typerace: 1.
Play Arithmetic Drill: 1.

Make Black Tea
Do Squats: 20 + 20 + 20.
Do Jumping Jacks: 50 + 50 + 50.
Do Pushups: 20 + 20 + 20.
Do leg raises: 20 + 20 + 20.
Do Grippings: 100 + 100 (L + R).

Use the Trainer App.
Revise favoured openings.

Anki: Make cards:.
Anki:

Notion: Finish one task.
Notion: Collate _:
Notion:

Code: One item off the objects from the Java book.
Code:

University: Read: Epistorical[D.fund]: | Batch 1
University: Read: Epistorical[D.sign]: | Batch 1
University:

Write with my left hand: Barely a sentence of a bio.

Commit Wind-down-time at 2200.
Stop the laptop by 0000. 
Stop electronics by 0100.
Go bed ~0200.
"""

"""
 ##### [School Schlob]
University: _: Data Collation ——— (By Sunday)
University: _: Assess the content of the Learning Guide ——— (By Sunday)
University: _: Assess the content the Discussion Forum ——— (By Sunday)
University: _: Assess the content the Assignment ——— (By Sunday)
University: _: Assess the content the Learning Journal ——— (By Sunday)

University: _: Assess Assignment 1 ——— (By Sunday)
University: _: Assess Assignment 2 ——— (By Sunday)
University: _: Assess Assignment 3 ——— (By Sunday)

University: _: Read the content of the Learning Guide ——— (By Monday)
University: _: Attempt the Self-Quiz ——— (By Monday)

University: _: Read the content of the Discussion Forum ——— (By Monday)
University: _: Seed the Discussion Forum ——— (By Monday)
University: _: Shape the Discussion Forum ——— (By Monday) 
University: _: Send the Discussion Forum ——— (By Monday)

University: _: Reply 1 in Discussion Forum ——— (By Tuesday)
University: _: Reply 2 in Discussion Forum ——— (By Tuesday) 
University: _: Reply 3 in Discussion Forum ——— (By Tuesday)

University: _: Read the content of the Assignment ——— (By Wednesday)
University: _: Seed the Assignment ——— (By Wednesday)
University: _: Shape the Assignment ——— (By Wednesday)
University: _: Send the Assignment ——— (By Wednesday)

University: _: Read the content of the Learning Journal ——— (By Thursday)
University: _: Seed the Learning Journal ——— (By Thursday)
University: _: Shape the Learning Journal ——— (By Thursday)
University: _: Send the Learning Journal ——— (By Thursday)


 ##### [Extra-curricular excess]
_: Read Chapter 1 Epistorical[iv].
_: Note Chapter 1 Epistorical[iv].
_: Summarise Chapter 1 Epistorical[iv].

_: Seed Question (Saghir) for Epistorical[iii].
_: Shape Question (Saghir) for Epistorical[iii].
_: "Send" Question (Saghir) for Epistorical[iii].
_: Seed Question (Journal) for Epistorical[iii].
_: Shape Question (Journal) for Epistorical[iii].
_: "Send" Question (Journal) for Epistorical[iii].
_: Seed Question (Kabir) for Epistorical[iii].
_: Shape Question (Kabir) for Epistorical[iii].
_: "Send" Question (Kabir) for Epistorical[iii].
_: Seed Answer (Saghir) for Epistorical[iii].
_: "Send" Answer (Saghir) for Epistorical[iii].
_: Shape Answer (Saghir) for Epistorical[iii].
_: Seed Answer (Kabir) for Epistorical[iii].
_: Shape Answer (Kabir) for Epistorical[iii].
_: "Send" Answer (Kabir) for Epistorical[iii].
_: Seed Answer (Journal) for Epistorical[iii].
_: Shape Answer (Journal) for Epistorical[iii].
_: "Send" Answer (Journal) for Epistorical[iii].

 ##### [SPL}
_: Start preparation.
_: Collect Apparel: Collared Shirt, Undershirt, Pants, Troussers.
_: Collect Acessories: Hat, Mask, Sunglasses, Sanitiser, Watch, Phone, Earbuds, Tiny Carry case, and a hankerchief.
_: Collect Luggage: Suitcase, Drawing materials and book, Thermus of cold water, Wallet, and ID.
_: Pack luggage.
_: Iron apparel.
_: Prepare the Notetaking app.
_: Create a folder in Google Drive.
_: Go forth, to the Sharjah Public Library.
_: Export any pictures taken during the trip to the Google Drive.
"""

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


def write_sequence(title, date, date_obj):
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
        w = open(title, 'wt', encoding='utf-8')
        
        print("Creating today's daily...")
        box = ['words', 'dates', media_obj, plan_obj, 'thoughts', 'rules']

        for item in box:
            
            if item == 'dates':
                w.writelines(["\n\n—————————  DATE \n"])
                w.writelines(['- In the Gregorian calendar: ', date_obj['Gregorian'], '\n'])
                w.writelines(['- In the Qamari Hijri calendar: ', date_obj['Hijri'], '\n'])
                w.writelines(['- In the ISO-8601 calendar: ', date_obj['ISO-8601'], '\n'])       
                w.writelines(['- In the Jacobin calendar: ', date_obj['Jacobin'], '\n'])
                w.writelines(['- In the Judean calendar: ', date_obj['Judean'], '\n'])
                                
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
        date: int/datetime
            the input date received from from the main function
        CS_chinese, CS_gregorian, CS_hijri, CS_ISO_8601, CS_jacobin, CS_jalali, CS_judean, CS_julian, CS_rumi : str
       
        dates_obj: dict
        
    Returns
    ---------
        dates_obj: dict
    """

    # ADD SUPPORT FOR: jalali, julian
    L_ah = Gregorian.fromisoformat(date).to_hijri()
    Heb = dates.HebrewDate.from_pydate(datetime.fromisoformat(date))
    S_ah = ''
   
    CS_chinese = ''
    CS_gregorian = datetime.fromisoformat(date).strftime('%A %B %Y-%m-%d AD')
    CS_hijri = ' '.join([L_ah.day_name('ar'), L_ah.day_name(), L_ah.month_name('ar'), L_ah.month_name(), ('-'.join([str(L_ah.year), str(L_ah.month), str(L_ah.day)])) ,  L_ah.notation('ar'), L_ah.notation()])
    CS_ISO_8601 = ' '.join(['-'.join(map( str, datetime.fromisoformat(date).isocalendar())), 'CE'])
    CS_jacobin = repubcal.RDate.fromisoformat(date).revol_strftime('%rf %rA %rB %rY %ry-%rm-%rd')
    CS_jalali = ''
    CS_judean = ' '.join( [Heb.month_name(True), Heb.month_name(), ('-'.join([str(Heb.year), str(Heb.month), str(Heb.day)]))])
    CS_julian = ''
    CS_rumi = ''
    
    # CHANGE THIS TO DICT
    dates_obj = {
                'Chinese': CS_chinese, 'Gregorian': CS_gregorian, 'Hijri': CS_hijri, 
                'ISO-8601':  CS_ISO_8601, 'Jacobin': CS_jacobin, 'Jalali': CS_jalali,
                'Judean': CS_judean, 'Julian': CS_julian, 'Rumi': CS_rumi
                }

    return dates_obj

def main():
    """
    The main function which iniates the processes to create a notepad daily.

    Parameters
    ---------
        CS_chinese, CS_gregorian, CS_hijri, CS_ISO_8601, CS_jacobin, CS_jalali, CS_judean, CS_julian, CS_rumi : str
        dates_obj: list
            incorporates all the results from the above calendrical systems.
        Today: str
            The date today in ISO format
        Tomorrow: str
            The date tomorrow ISO format

    """

    Today = datetime.now().date().isoformat()
    Tomorrow = (datetime.now().date()+ timedelta(days=1)).isoformat()

    if not read_sequence('.'.join([Today, 'txt'])):
        print("Creating today's daily...")
        write_sequence('.'.join([Today, 'txt']), Today, get_dates(Today))
    else:
        print("Creating tomorrow's daily...")
        write_sequence('.'.join([Tomorrow, 'txt']), Tomorrow, get_dates(Tomorrow))

    
saying_01 = " 'Take everything in moderation including moderation.' - Oscar Wilde "
saying_02 = "'Tempus Fugit, Carpe Diem, Memento Mori.' [Latin]"
saying_03 = " 'The saddest thing about any man is that he be ignorant. And the most exciting thing is that he knows.' - Alfred the Great "
saying_04 = " 'The truth is, in the end, everyone is going to hurt you, you just got to find the ones worth suffering for.' - Bob Marley "
saying_05 = " 'How do you tell if it’s a coincidence or a sign? By how well you use it.' - Ehsan Mujahid "
saying_06 = "'Doveray, no proveray.' [Russian]"
saying_07 = "'Avash Avash/Ngadale Ngadale.' [Turkish/Albanian]"
saying_08 = "'The dogs bark, but the caravan goes on.' [Middle Eastern]"
saying_09 = "'D E L E T E  all  G U N K'"
saying_10 = "'He who defends everything defends nothing.' - Fredrick II, Holy Roman Emperor"
saying_11 = "'He who knows not how to dissimulate, can not reign.' - Louis XI, King of France"
saying_12 = "'Weniger, aber besser.' [German]"
saying_13 = "'The wisdom of life consists in the elimination of non-essentials.' - Lin Yutang"

quotes_obj = ["\nQuote of the day (maxims tolerated): ",
                saying_01,                saying_02,
                saying_03,                saying_04,
                saying_05,                saying_06,
                saying_07,                saying_08,
                saying_09,                saying_10,
                saying_11,                saying_12,
                saying_13,              
                ]

method_01 = """
 ### THE EISENHOWER MATRIX ###
     ——————————————————————————————————
     |         |  URGENT  |    NOT    |
     |—————————|——————————|———————————|
     |   NEED  |    DO    |  DECIDE   |
     |—————————|——————————|———————————|
     |   NOT   | DELEGATE |  DELETE   |
     ——————————————————————————————————
"""
method_02 = """
 ### The Carnegie Conversation ###
    - Smile genuinely, and show genuine affection.
    - Let the other person have their dignity, even while wrong
    - Talk to listen instead of listening to talk.
    - (read more of the book, plox)
"""
method_03 = """
 ### The Feynman Technique ###
This is to understand a concept clearly, concisely.
    1. Choose a concept you want to learn about
    2. Pretend you're teaching it to a 7 year old    
    3. Identify gapsin your explanation
    4. Review and simplify as need be
"""
method_04 = """
 ### The Inception Explanation ###
This is to make people think these ideas are their own. People love that even if they hate themselves.
    1. Explain enough bits to make it a connect the dot situation
    2. Allow/Lead/Wait for them to finish their thoughts
"""
method_05 = """
 ### The Tomato timer ###
This is to not only save time, but make you want to do more.
There is a session that can last rougly 20-40m. There are short 5m breaks, and after 3-4 a long 15m break.
    1. Define what thing you will do
    2. Define how long a session will be
    3. Define how many sessions there will be
    4. Define the short breaks and long breaks
"""
method_06 = """
 ### The Napolean Answer ###
This is to save on time, effort, and worry.
It is based on the fact that most minor or even major problems can solve themselves or share a common root. 
    1. Answer if Urgent & Important
    2. Leave the rest unanswered for a bit
"""
method_07 = """
 ### The Socratic Method ###
This is to stimulate critical thinking, draw out ideas and underlying presuppositions.    
    1. Define an analogous situation
    2. Procure an agreement
    3. Advance ensuring agreement 
"""
method_08 = """ 
 ### Deliberate practice ###
    1. Define Success: so you are not chasing wild geese.
    
    2. Schedule sessions – and go through with them.
    
    3. Practice Slow: like in the gym.
    
    4. Limit your sessions for focus: No need to start off with 12 hours a day.
    
    5. Maximise Practice Time: remove barriers to start.
    
    6. Track small intervals of improvement.
    
    7. Plan, Reflect; preview & review.
    
    8. Get an accountability partner
"""
method_09 = """
 ### Dopamine detoxification ###
1. A dopamine detox must last at least 2 weeks – not 24 hours.

2. Prepare for boredom: walks, books, cleaning, chores, errands, cooking, or exercises.

3. You are allowed **SCHEDULED** and **ACTIVE** media consumption, e.g., a 'movie night', specific video watching from before the YouTube, listening to music.

4. You are not allowed **PASSIVE** and **MINDLESS** media consumption: no scrolling/searching for novelty or binge-watching: No `low-effort``dopamine-preying` activities.

5. No video games. Play board games or physical games, but video games are far too fun for the brain – remember that this is for the detox period.

6. Socialise.

7. Do not beat yourself up; do not make your failure permanent. If you have a moment you did it, notice it, stop it,  acknowledge it, circumvent it, and move on.
"""
method_10 = """
 ### The futility of saving without a plan ###
You cannot save X by replacing spending from Y1 to Y2. 

You can only do so with investment Z that either: 
    increases the value-spendable of X in the long/short run, 
    reduces the need to save X in the long/short run, 
    decreases the cost of no Yn in the long/short run, 
    reduces the need of Yn in the long/short run, 
    or has some other benefit that either immediately or eventually pays off. 

Okay, Ehi, now fill it in for time, money, or whatever resource that is at least temporarily exhaustible.
"""
method_11 = """
 ### A better way to win an argument than a hatchet job ###
1 Attempt to re-express your target’s position so clearly, vividly, and fairly that your target says, “Thanks, I wish I’d thought of putting it that way.” 
2 List any points of agreement, especially if they are not matters of general or widespread agreement. 
3 Mention anything you have learned from your target. 
4 Only then are you permitted to say so much as a word of rebuttal or criticism.
"""


rules_obj = ["\nRULES: ",
                method_01,                method_02,
                method_03,                method_04,
                method_05,                method_06,
                method_07,                method_08,
                method_09,                method_10,                          
                ]

if __name__ == '__main__':
    main()

else:
    print('This is imported as: ' + __name__)
