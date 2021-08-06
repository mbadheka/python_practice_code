name = input("Enter your name : ")
age = int(input("enter your age : "))
fav_movies = input("enert name of movies ").split(",")
fav_songs = input("enert name of songs ").split(",")

dict1 = {
    'name' : name,
    'age' : age,
    'fav_movies' : fav_movies,
    'fav_songs' : fav_songs
}

for i,j in dict1.items():
    print(f" {i} is {j}")