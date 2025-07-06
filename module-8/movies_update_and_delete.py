#Cameron Mendez
#07/06/2025  
#Module8.2 Assignment
#movies_update_and_delete.py

import mysql.connector

# Function to show films with inner joins
def show_films(cursor, title):
    # inner join query to get readable names from genre and studio
    cursor.execute("""
        SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)
    
    films = cursor.fetchall()
    
    print("\n  -- {} --".format(title))
    
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]))

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",       # MySQL username
    password="Bangarang4$",   # MySQL password
    database="movies"
)

cursor = db.cursor()

# Display initial film records
show_films(cursor, "DISPLAYING FILMS")

# Insert a new film, using existing studio 
cursor.execute("""
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES ('Nope', '2022', 130, 'Jordan Peele', 2, 2)
""")
db.commit()

# Display after insert
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update Alien to Horror genre (genre_id = 1)
cursor.execute("""
    UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'
""")
db.commit()

# Display after update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

# Delete Gladiator
cursor.execute("""
    DELETE FROM film WHERE film_name = 'Gladiator'
""")
db.commit()

# Display after delete
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Close teh connection
cursor.close()
db.close()

# Keep window open when opening from file
input("Press Enter to exit...")
