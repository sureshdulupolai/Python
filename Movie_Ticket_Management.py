# 🎟️ 1. Movie Ticket Booking System

Movie = [
    {
        'movie_name': 'Shershaah',
        'price': 180,
        'seat': 1,
    },
    {
        'movie_name': 'Pathaan',
        'price': 220,
        'seat': 2,
    },
    {
        'movie_name': 'RRR (Hindi)',
        'price': 250,
        'seat': 3,
    },
    {
        'movie_name': 'Jawaan',
        'price': 210,
        'seat': 4,
    },
    {
        'movie_name': '3 Idiots',
        'price': 150,
        'seat': 5,
    },
]

seats = [
    {
        'id': 1,
        'available': 75,
        'total': 100,
        'book': 25,
        'status': 'Available'
    },
    {
        'id': 2,
        'available': 120,
        'total': 150,
        'book': 30,
        'status': 'Available'
    },
    {
        'id': 3,
        'available': 60,
        'total': 100,
        'book': 40,
        'status': 'Available'
    },
    {
        'id': 4,
        'available': 0,
        'total': 100,
        'book': 100,
        'status': 'Full'
    },
    {
        'id': 5,
        'available': 90,
        'total': 120,
        'book': 30,
        'status': 'Available'
    },
]

# Django Structure of Movie Ticket
# -------------------------------------------------------------------------------------------
def CombineMovieSeats(seatUpgrade = 0, seatsFor = 0):
    movieAvailable = []
    for mov in Movie:
        valueSeat = mov['seat']
        for place in seats:
            if (place['id'] == valueSeat) and (place['status'] == 'Available'):
                movieAvailable += [(mov, place)]
            if (seatUpgrade != 0) and (seatsFor != 0):
                if place['id'] == seatsFor:
                    place['book'] += 1
                    place['available'] -= 1

    return movieAvailable

CMS = CombineMovieSeats()
# print(CMS)

def ListOfNameMovieData():
    lstOfUserMovieAvailable = []
    for CMSCheck in CMS:
        for NewData in range(1):
            lstOfUserMovieAvailable += [(CMSCheck[0]['movie_name'], CMSCheck[0]['price'], CMSCheck[1]['available'], CMSCheck[1]['total'], CMSCheck[1]['book'])]
    
    return lstOfUserMovieAvailable

ListOfMovieData = ListOfNameMovieData()

def UserNameMovie():
    lstOfMovies = []
    for ListData in ListOfMovieData:
        lstOfMovies += [
            (
                "Movie", ':', ListData[0],
                "Price", ':', ListData[1],
                "Remeaning Seats", ':', ListData[2],
                "Total Seats", ':', ListData[3],
                "Booked Seats", ':', ListData[4],
            )
        ]
    
    print('\n-- Available Movie Showen in Django Templates --\n')
    for Movies in lstOfMovies:
        print(*Movies)

# Check Available Movie Status
# ------------------------------------------------------------------------
# UserNameMovie()

def Movies():
    try:
        UserName = input('Enter Your Name : ')
        EnterYourAge = int(input('Enter Your Age : '))
        UserNameMovie()
        movieName = int(input('\nWhich ticket you need to book : '))
        movieSeatsBook = int(input('How many seats you need to book : '))
        CheckCondition = int(input('Conform you need to book this ticket : '))
        # print(bool(CheckCondition == 1))
        if CheckCondition == 1:
            CombineMovieSeats(seatUpgrade=movieSeatsBook, seatsFor=movieName)
            print('Your Ticket Booked Successfully Mr/Ms {}'.format(UserName))
            UserNameMovie()
        else:
            print('The Movie Does Not Exist, Id Not Matched!!')
    
    except:
        print('The Input Does Not Match With Any Feild!')