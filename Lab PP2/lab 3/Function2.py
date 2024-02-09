# Dictionary of movies
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#ex 1
def imdb(movies):
    for movie in movies:
        imdb = movies["imdb"]
        if imdb > 5.5:
            return True
        return False
    print("Ex1: ", ex1(movies), "\n")


#ex 2
def above_5_5(movies):
    mylist=[]
    for movie in movies:
        imdb=movie["imdb"]
        if imdb>5.5:
            mylist.append(True)
        else:
            mylist.append(False)
    return mylist
print(above_5_5(movies), "\n")


#ex 3
def category(movies):
    category_need=str(input("Enter one of categories (Thriller, Action, Adventure,Drama, Romance, War, Crime, Comedy or Suspense): "))
    for movie in movies:
        cate=movie["category"]
        if cate==category_need:
            print(movie["name"])
category(movies)


#ex 4
def avarage_IMDB(movies):
    avarage = 0
    for movie in movies:
        avarage += movie["imdb"]
    return avarage/len(movies)
print(avarage_IMDB(movies))


#ex 5
def avarage_of_category(movies):
    imdb=0
    category_need=str(input("Enter one of categories (Thriller, Action, Adventure,Drama, Romance, War, Crime, Comedy or Suspense): "))
    for movie in movies:
        cate=movie["category"]
        film=movie["imdb"]
        if cate==category_need:
            imdb+=film

    return imdb/len(movies)
print(avarage_of_category(movies))