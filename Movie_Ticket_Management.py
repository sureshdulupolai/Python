# 🎟️ 1. Movie Ticket Booking System
# Class: Movie, Theatre, User

# Features:

# Dekho kaunse shows available hain

# Book ticket (limited seats logic)

# Cancel ticket

# Data Storage: Seat availability list, showtime dict

# Bonus: Seating layout dikhane ki koshish karo (2D list)


Movie = [
    {
        'movie_name': 'Shershaah',
        'price': '180',
        'seat': 1,
    },
    {
        'movie_name': 'Pathaan',
        'price': '220',
        'seat': 2,
    },
    {
        'movie_name': 'RRR (Hindi)',
        'price': '250',
        'seat': 3,
    },
    {
        'movie_name': 'Jawaan',
        'price': '210',
        'seat': 4,
    },
    {
        'movie_name': '3 Idiots',
        'price': '150',
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

def checkTickect():
    movieAvailable = []
    for mov in Movie:
        valueSeat = mov['seat']
        for place in seats:
            if (place['id'] == valueSeat) and (place['status'] == 'Available'):
                movieAvailable += [(mov, place)]
    
    for inAvailableMovie in movieAvailable:
        print(inAvailableMovie)

checkTickect()