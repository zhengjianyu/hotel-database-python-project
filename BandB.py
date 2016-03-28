def Bedrooms():  # nothing -> interaction
    """ Main program """
    print("Welcome to the hotel program!")
    All = {}
    Bedrooms = []
    Reservations = []
    [Bedrooms, Reservations] = handle_commands(Bedrooms, Reservations)
    Room = [Bedrooms, Reservations][0]
    Reservation = [Bedrooms, Reservations][1]
    A = '---------------------Bedrooms---------------------\n'
    B = 'Number of bedrooms in sevice: {}\n'.format(len(Room))
    C = '\n\n\n---------------------Reservations---------------------\n'
    D = 'No. Rm.   Arrive      Depart   Guest\n'
    E = '--------------------------------------------------\n'
    outfile = open('data.txt', 'w')
    outfile.write(A)
    outfile.write(B)
    for i in Room:
        outfile.write(str(i)+'\n')
    outfile.write(C)
    outfile.write(D)
    outfile.write(reservation_print(Reservation))
    outfile.close()
    print("\nthe information has been saved in the txt file 'data'.")
    print("Thank you.  Good-bye.")

MENU = """
Choose one command by enter the two non-whitespace keys:
AB: Add a new room with the specified room number.
BL: Print a list of the rooms currently available.
PL: Input a string and return it.
BD: Delete the specified room from total rooms.
NR: Add reservations to rooms.
RL: Print all the reservations.
RD: Delete the specified reservation.
RB: Lists all reservations for a given bedroom.
RC: List all reservations for a given guest.
LA: Print a list of all guests arriving on the specified date.
LD: Print a list of all guests departing on the specified date.
LF: List all bedrooms that are free each night for a guest arriving on the first\n    date and departing on the second.
LO: List all bedrooms that are occupied for at least one night between the given\n    arrival and departure dates. 
QT: Quit.
-------------------------------------------------------------------
"""

def handle_commands(C: list, R:list) -> list:
    """ Display menu, accept and process commands """
    while True:
        response = input(MENU)
        if response.upper() == 'QT':
            return [C, R]
        elif response.upper() == 'AB':
            while True:
                confirm = input('Add a new bedroom? Enter Y/N ').upper()
                if confirm.upper() == 'Y':
                    r = int(input('Please enter the room number of the bedroom you want to add: '))
                    if r in C:
                        print('Sorry, room {} is already in the room list'.format(r))
                    else:
                        C = Bedroom_add(C, r)
                elif confirm.upper() == 'N':
                    break
                else:
                    invalid_command(confirm)
        elif response.upper() =='BL':
            print('Number of bedrooms in sevice: {}'.format(len(C)))
            print('-------------------------------------')
            print_bedrooms(C)
        elif response.upper() =='PL':
            r = print_line()
            print(r)
        elif response.upper() == 'BD':
            n = int(input("Please enter the room number you want to remove:  "))
            if n in C:
                C = Bedroom_delete(C, n)
                print('room {} has been deleted.'.format(n))
            else:
                invalid_rooms(n)
        elif response.upper() == 'RL':
            print('Number of reservations:  {}'.format(len(R)))
            print('No. Rm.   Arrive      Depart   Guest')
            print('--------------------------------------------------')
            print(reservation_print(R))
        elif response.upper() == 'RD':
            n = int(input('Please enter the confirmation number of the reservation you want to delete:  '))
            if n in list_of_confirmation(R):
                R = reservation_delete(R, n)
                print('reservation (which confirmation is {}) has been deleted.'.format(n))
            else:
                print('Sorry, there is no reservation which confirmation is #{}'.format(n))
        elif response.upper() == 'RB':
            n = int(input('Please enter the room number: '))
            print('Room: {}    Number of reservations: {}'.format(n, len(reservations_by_bedrooms(n, R))))
            print('No. Rm.   Arrive      Depart   Guest')
            print('--------------------------------------------------')
            for i in reservations_by_bedrooms(n, R):
                print(i, end='')
        elif response.upper() == 'RC':
            n = input("lease enter the guest's name:  ")
            print('Guest: {}    Number of reservations: {}'.format(n, len(reservations_by_guests(n, R))))
            print('No. Rm.   Arrive      Depart    Guest')
            print('--------------------------------------------------')
            for i in reservations_by_guests(n, R):
                print(i, end='')
        elif response.upper() == 'NR':
            while True:
                YN = input('Are you sure to add a new reservation? Enter Y/N ').upper()
                if YN.upper() == 'Y':
                    n = int(input('Please enter the room number you want to add reservation:  '))
                    if n in C:
                        r = add_reservation(R, n)
                        R = collect_reservation(R, r)
                    else:
                        invalid_rooms(n)
                elif YN.upper() == 'N':
                    break
                else:
                    invalid_command(YN)
        elif response.upper() == 'LA':
            L = ask_time()
            print('Guests arriving on {}/{}/{}:'.format(L[0], L[1], L[2]))
            for i in list_arrivals(L[0], L[1], L[2], R):
                print('{}  (room {})'.format(i.name, i.room))
        elif response.upper() == 'LD':
            L = ask_time()
            print('Guests departing on {}/{}/{}:'.format(L[0], L[1], L[2]))
            for i in list_departures(L[0], L[1], L[2], R):
                print('{}  (room {})'.format(i.name, i.room))
        elif response.upper() == 'LF':
            L = ask_all()
            print('Bedrooms free between {}/{}/{} to {}/{}/{} :'.format(L[0], L[1], L[2], L[3], L[4], L[5]))
            for i in list_free_bedrooms(L[0], L[1], L[2], L[3], L[4], L[5], R):
                print('   {}'.format(i))
        elif response.upper() == 'LO':
            L = ask_all()
            print('Bedrooms free between {}/{}/{} to {}/{}/{} :'.format(L[0], L[1], L[2], L[3], L[4], L[5]))
            for i in list_occupied_bedrooms(L[0], L[1], L[2], L[3], L[4], L[5], R):
                print('   {}'.format(i))
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")

def Bedroom_add(C: list, number: int) -> list:
    '''return a list of bedroom number'''
    if 99 < number < 1000:
        C.append(number)
    else:
        print('Invalid. Room number should be in three digits.')
    return C

def print_bedrooms(C: list):
    '''print every bedrooms in the room list'''
    for i in C:
        print(i)

def print_line() -> str:
    '''input anything as a reports or something'''
    return input('Please enter the string you want to input:\n')

def Bedroom_delete(C: list, n: int) -> list:
    '''takes a room number and a list of rooms, returns the list without that room with that number'''
    result = []
    for i in C:
        if i != n:
            result.append(i)
    return result

def invalid_rooms(n: int) -> str:
    '''print message for invalid room numbers'''
    print('Sorry, there is no room which number is {}.'.format(n))

from collections import namedtuple
Reservation = namedtuple('Reservation', 'room confirmation name amonth aday ayear dmonth dday dyear')

def room_number_reserved(R: list) -> list:
    '''returns a list of room number'''
    result = []
    for i in R:
        result.append(i.room)
    return result

def list_of_confirmation(R: list) -> list:
    '''returns a list of confirmation'''
    result = []
    for i in R:
        result.append(i.confirmation)
    return result

def confirm(R: list) -> int:
    '''return a confirmation'''
    count = len(R) + 1
    for i in R:
        while count == i.confirmation:
            count += 1
    return count

def add_reservation(R: list, n: int) -> Reservation:
    confirmation = confirm(R)
    name = input("Please enter the guest's name:  ")
    arrivalmonth = int(input('Please enter the arrival month(in digital form): '))
    while arrivalmonth > 12:
        print('Invalid month.\n')
        arrivalmonth = int(input('Please enter the arrival month again(in digital form): '))
    arrivalday = int(input('Please enter the arrival date: '))
    while arrivalday > 31:
        print('Invalid date.\n')
        arrivalday = int(input('Please enter the arrival date again: '))
    arrivalyear = int(input('Please enter the arrival year: '))
    while arrivalyear < 1500:
        print('Invalid year.\n')
        arrivalyear = int(input('Please enter the arrival year again: '))
    departuremonth = int(input('Please enter the departure month(in digital form): '))
    while departuremonth > 12:
        print('Invalid month.\n')
        departuremonth = int(input('Please enter the departure month again(in digital form): '))
    departureday = int(input('Please enter the departure date: '))
    while departureday > 31:
        print('Invalid date.\n')
        departureday = int(input('Please enter the departure date again: '))
    departureyear = int(input('Please enter the departure year: '))
    while arrivalyear > departureyear:
        print('Invalid year.\n')
        departureyear = int(input('Please enter the departure year again: '))
    if arrivalyear < departureyear:
        print('Reserving room {} for {} ---- Confirmation #{}\n  (arriving {}/{}/{}, departing {}/{}/{})\n'.format(
               n, name, confirmation, arrivalmonth, arrivalday, arrivalyear, departuremonth, departureday, departureyear))
        return Reservation(n, confirmation, name, arrivalmonth, arrivalday, arrivalyear,
                          departuremonth, departureday, departureyear)
    if arrivalyear == departureyear:
        if arrivalmonth < departuremonth:
            print('Reserving room {} for {} ---- Confirmation #{}\n  (arriving {}/{}/{}, departing {}/{}/{})\n'.format(
                   n, name, confirmation, arrivalmonth, arrivalday, arrivalyear, departuremonth, departureday, departureyear))
            return Reservation(n, confirmation, name, arrivalmonth, arrivalday, arrivalyear,
                          departuremonth, departureday, departureyear)
        elif arrivalmonth == departuremonth:
            if arrivalday <= departureday:
                print('Reserving room {} for {} ---- Confirmation #{}\n  (arriving {}/{}/{}, departing {}/{}/{})\n'.format(
                       n, name, confirmation, arrivalmonth, arrivalday, arrivalyear, departuremonth, departureday, departureyear))
                return Reservation(n, confirmation, name, arrivalmonth, arrivalday, arrivalyear,
                          departuremonth, departureday, departureyear)
            else:
                print('Invalid. Arrival date is later than the departure date.\n')
        else:
            print('Invalid. Arrival date is later than the departure date.\n')

def reservations_by_bedrooms(n: int, R: list) -> list:
    '''returns a list that list all the reservation for a given room'''
    result = []
    for i in R:
        if i.room == n:
            result.append(reservation_str(i))
    return result

def reservations_by_guests(n: str, R: list) -> list:
    '''returns a list that list all the reservation for a given guest'''
    result = []
    for i in R:
        if i.name == n:
            result.append(reservation_str(i))
    return result

def list_arrivals(a: int, b: int, c: int, R: list) -> list:
    '''takes the arrival date and returns all guests arriving on the specified date'''
    result = []
    for i in R:
        if a == i.amonth and b == i.aday and c == i.ayear:
            result.append(i)
    return result        

def collect_reservation(R: list, r: Reservation) -> list:
    R.append(r)
    return R

def reservation_print(R: list) -> str:
    '''return a string representing the whole collection'''
    s = ''
    for r in R:
        s = s + reservation_str(r)
    return s

def reservation_str(r: Reservation) -> str:
    '''return a string representing the reserved room'''
    return ('{:3d} {} {:2d}/{:02d}/{:4d} {:2d}/{:02d}/{:4d} {}\n'.format(r.confirmation,
        r.room, r.amonth, r.aday, r.ayear, r.dmonth, r.dday, r.dyear, r.name))

def reservation_delete(R: list, n: int) ->list:
    '''takes a confirmation number and the reservation list, returns the list without that room with that confirmation number'''
    result = []
    for i in R:
        if i.confirmation != n:
            result.append(i)
    return result
    
def list_departures(a: int, b: int, c: int, R: list) -> list:
    '''takes the departure date and returns all guests depart on the specified date'''
    result = []
    for i in R:
        if a == i.dmonth and b == i.dday and c == i.dyear:
            result.append(i)
    return result

def list_occupied_bedrooms(a: int, b: int, c: int, d: int, e:int, f: int, R: list) -> list:
    '''takes two dates, returns all bedrooms that that are occupied for at
       least one night between the given arrival and departure dates'''
    result = []
    rooms = []
    for i in R:
        if ((a-1)*30 + b + (c-1)*365) <= ((i.amonth-1)*30 + i.aday + (i.ayear-1)*365) <= ((d-1)*30 + e + (f-1)*365):
            result.append(i)
        elif ((a-1)*30 + b + (c-1)*365) <= ((i.dmonth-1)*30 + i.dday + (i.dyear-1)*365) <= ((d-1)*30 + e + (f-1)*365):
            result.append(i)
    for r in result:
        rooms.append(r.room)
    return list(set(rooms))

def list_free_bedrooms(a: int, b: int, c: int, d: int, e:int, f: int, R: list) -> list:
    '''takes two dates, and returns all bedrooms that are free each night for a
       guest arriving on the first date and departing on the second'''
    result = []
    rooms = []
    for i in R:
        if ((d-1)*30 + e + (f-1)*365) < ((i.amonth-1)*30 + i.aday + (i.ayear-1)*365) and ((d-1)*30 + e + (f-1)*365) < ((i.dmonth-1)*30 + i.dday + (i.dyear-1)*365):
            result.append(i)
        elif ((a-1)*30 + b + (c-1)*365) > ((i.amonth-1)*30 + i.aday + (i.ayear-1)*365) and ((a-1)*30 + b + (c-1)*365) > ((i.dmonth-1)*30 + i.dday + (i.dyear-1)*365):
            result.append(i)
        elif ((a-1)*30 + b + (c-1)*365) > ((i.dmonth-1)*30 + i.dday + (i.dyear-1)*365):
            result.append(i)
        elif ((d-1)*30 + e + (f-1)*365) < ((i.amonth-1)*30 + i.aday + (i.ayear-1)*365):
            result.append(i)
    for r in result:
        rooms.append(r.room)
    return list(set(rooms))

def ask_time() -> list:
    arrivalmonth = int(input('Please enter the arrival month(in digital form): '))
    while arrivalmonth > 12:
        print('Invalid month.\n')
        arrivalmonth = int(input('Please enter the arrival month again(in digital form): '))
    arrivalday = int(input('Please enter the arrival date: '))
    while arrivalday > 31:
        print('Invalid date.\n')
        arrivalday = int(input('Please enter the arrival date again: '))
    arrivalyear = int(input('Please enter the arrival year: '))
    while (arrivalyear < 1500 or arrivalyear > 2016):
        print('Invalid year.\n')
        arrivalyear = int(input('Please enter the arrival year again: '))
    return [arrivalmonth, arrivalday, arrivalyear]

def ask_all() -> list:
    arrivalmonth = int(input('Please enter the arrival month(in digital form): '))
    while arrivalmonth > 12:
        print('Invalid month.\n')
        arrivalmonth = int(input('Please enter the arrival month again(in digital form): '))
    arrivalday = int(input('Please enter the arrival date: '))
    while arrivalday > 31:
        print('Invalid date.\n')
        arrivalday = int(input('Please enter the arrival date again: '))
    arrivalyear = int(input('Please enter the arrival year: '))
    while arrivalyear < 1500:
        print('Invalid year.\n')
        arrivalyear = int(input('Please enter the arrival year again: '))
    departuremonth = int(input('Please enter the departure month(in digital form): '))
    while departuremonth > 12:
        print('Invalid month.\n')
        departuremonth = int(input('Please enter the departure month again(in digital form): '))
    departureday = int(input('Please enter the departure date: '))
    while departureday > 31:
        print('Invalid date.\n')
        departureday = int(input('Please enter the departure date again: '))
    departureyear = int(input('Please enter the departure year: '))
    while arrivalyear > departureyear:
        print('Invalid year.\n')
        departureyear = int(input('Please enter the departure year again: '))
    return [arrivalmonth, arrivalday, arrivalyear, departuremonth, departureday, departureyear]


if __name__ == '__main__':
    Bedrooms()





