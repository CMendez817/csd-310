#Cameron Mendez
#07/05/2025
#Module 7.2
#movies_queries.py

import mysql.connector

# Connect to the MySQL movies database
db = mysql.connector.connect(
    host="localhost",
    user="root",       		# <-- MySQL username
    password="Bangarang4$",   	# <-- MySQL password
    database="movies"
)

cursor = db.cursor()

# 1. Displaying Studio Records
print("-- DISPLAYING Studio RECORDS --")
cursor.execute("SELECT studio_id, studio_name FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print(f"Studio ID: {studio[0]}")
    print(f"Studio Name: {studio[1]}\n")

# 2. Displaying Genre Records
print("-- DISPLAYING Genre RECORDS --")
cursor.execute("SELECT genre_id, genre_name FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print(f"Genre ID: {genre[0]}")
    print(f"Genre Name: {genre[1]}\n")

# 3. Displaying Short Film Records (runtime < 120 mins)
print("-- DISPLAYING Short Film RECORDS --")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
short_films = cursor.fetchall()
for film in short_films:
    print(f"Film Name: {film[0]}")
    print(f"Runtime: {film[1]}\n")

# 4. Displaying Director Records in Order (grouped/sorted by director)
print("-- DISPLAYING Director RECORDS in Order --")
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
directors = cursor.fetchall()
for film in directors:
    print(f"Film Name: {film[0]}")
    print(f"Director: {film[1]}\n")

# Close connection
cursor.close()
db.close()

input("Press Enter to exit...")
