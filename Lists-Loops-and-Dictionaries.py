#create a list[] with [item1,item2,etc.]
fav_nos = [9,3,25]
#can grab any item you want from the list by returning function[0,1,etc.]
print(fav_nos[0])

#example list:

fav_movies = ["Little Miss Sunshine", "Fox and the Hound", "Howl's Moving Castle"]
#find length (len) of list (how many items are on your list)
print(len(fav_movies))
#add something new to list (.append(new item))
fav_movies.append("Iron Man")
#add new item to list in specific place (.insert(where like 0, item))
fav_movies.insert(2,"Batman")
print(len(fav_movies))
#get rid of list item(s) (del(function[0]))
del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])

print(fav_movies)
#make a loop
for number in range(10):
    print(number)
for movie in fav_movies:
    print(movie)
for number in range(40):
    print ((number+1)*2)

#dictionaries{key:value,} ("key value pairs"-the key= the term (the word you're looking up) -the value= the definition)
cats = {"Mowgli":3,"Bagheera":6,"Sheeba":7}
#in this case, our term/key is the cat's name and the definition is their age
#now we'll add another cat to the definitions
cats["Jones"] = 8
#delete an item from the list
del(cats["Jones"])
#length of a dictionary
len(cats)
print(cats)

define = {"ennui":"boredom","saudade":"sad longing for something/someone you love"}
print(define["saudade"])
#you can only return the key(term), not the value(def)

idk = {5:True, 10:False, 25:False}
print(idk[5])
