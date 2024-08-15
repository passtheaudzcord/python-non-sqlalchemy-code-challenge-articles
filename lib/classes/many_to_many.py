class Article:
    #class attribute all, keeps track of article instances
    all = []

    #Article intialized with an Author instance, a magazine instance, and title
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    #decorator for title
    @property 
    def title(self):
        return self._title 

    #setter validates if string is between 5 and 50 characters, and is only set once
    @title.setter
    def title(self, value):
        if (isinstance(value, str) and 5 <= len(value) <= 50 and not hasattr(self, 'title')):
            self._title = value

    #decorator for author
    @property
    def author(self):
        return self._author
    
    #setter ensures author is an instance of "Author" class
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    #decorator for magazine
    @property
    def magazine(self):
        return self._magazine

    #setter ensures magazine is an instance of "Magazine"
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value 
        
class Author:
    #Author initialized with name
    def __init__(self, name):
        self.name = name

    #decorator for name
    @property
    def name(self):
        return self._name
    
    #setter for author's name, validating it is not an empty string and is only set once
    @name.setter
    def name(self, value):
        if(isinstance(value, str) and len(value) > 0 and not hasattr(self, 'name')):
            self._name = value

    #Returns a list of written by an author
    def articles(self):
        return [article for article in Article.all if article.author == self]

    #Returns a list of magazines the author has written for
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    #Creates and returns a new "Article" instance, relating to the author
    def add_article(self, magazine, title):
        return Article(self, magazine,title)
        #if isinstance(title, str) and 5 <= len(title) <= 50:
            #self.articles.append(title)
        #return Article(magazine, title)

    #Returns a unique list of categories of magazines the author wrote.
    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([article.magazine.category for article in self.articles()]))

class Magazine:
    #Magazine initialized with a name and a category
    def __init__(self, name, category):
        self.name = name
        self.category = category

    #decorator for name
    @property
    def name(self):
        return self._name

    #set name attribute, validates by checking if the 'value' is 2-16 characters.
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    #decorator for category
    @property
    def category(self):
        return self._category

    #set category attribute, validates if 'value' is a string that isn't empty.
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    #iterate over Article.all
    #Retrieves all articles associated with this magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    #Retrieves a list of unique authors who have contributed to this magazine.
    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    #call articles method to get all articles in this magazine
    #return none if no articles are found
    #extract titles from article
    def article_titles(self):
        if not self.articles():
            return None
        return list(set([article.title for article in self.articles()]))

    #retrieve list of authors who have contributed to this magazine
    #only if two or more distinct authors are found
    def contributing_authors(self):
        if len([article.author for article in self.articles()]) <= 2:
            return None
        return [article.author for article in self.articles()]