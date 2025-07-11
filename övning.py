'''
Create a book class that has the following attributes:
title
author
price

get_description method will retun
"THe book 'title' by 'author' cost 'price'

'''

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def war(self):
        return f"The book '{self.title}' by {self.author} costs {self.price}"
    
horus = Book("40000k", "The Emperor", 400000)

print(horus.war())

#andra sättet
