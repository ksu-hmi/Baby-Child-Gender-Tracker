#import libraries first
import statistics as s

#add constants next
Moms = {'Ronda Broome':'***','Betty White':'***','Susan Black':'***', 'Sharon Stone':'***', 'Mary Joseph':'***', 'Melissa Smith':'***'}

Babies = {'Paul Joseph':["Male"],
            'Barbara Black':["Female"],
            'Michelle Stone':["Binary"],
            'Molly Smith':["Non-Binary"],
            'Draymond White':["Male"],
            'Raven Broome':["Female and loves both her mom and dad"]
             }
            



#now define functions
def enterBaby():
    nameToEnter = input('Baby name: ')
    SexToEnter = input('Age of Baby: ')

    if nameToEnter in Babies:
        print('Adding age for'  "," + nameToEnter)
        Babies[nameToEnter]
        print(str(nameToEnter)+  ',' ' is this gender:')
        print(Babies[nameToEnter])
    else:
        print('Baby not found. Please check your spelling or call Mom ASAP!')


def removebaby():
    nameToRemove = input('Who do you want to remove? ')
    if nameToRemove in Babies:
        print('Removing '+nameToRemove)
        del Babies[nameToRemove]
        print(Babies)
    else:
        print('Baby not found.')




def main():
    print("User: " + login)
    print("""
    Welcome to our HMI 7540 Baby Gender Tracker. See instructions below!

    [1] - Enter Baby Name
    [2] - Remove Baby Name
    [3] - Exit
    
    """)

    action = input('What would you like to do? (Enter a number) ')

    if action == '1':
        #print('1 selected')
        enterBaby()
    elif action == '2':
        #print('2 selected')
        removebaby()
    
    elif action == '3':
        #print('4 selected')
        exit()
    else:
        print('Valid option not selected.') #need to cause it to reprompt

login = input('Name_of_Mother: ')
password = input('Password: ')

if login in Moms:
    if Moms[login] == password:
        print('Welcome,',login)
        #now run the code
        while True:
            main()
    else:
        print('Invalid password.')
else:
    print('Congrats. Expecting Mom!')


