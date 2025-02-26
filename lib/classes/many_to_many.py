class Article:
    # Class variable to store all instances of Article
    all = []

    # Constructor method to initialize the article with author, magazine, and title
    def __init__(self, author, magazine, title):  
        self.author = author       # Set the author of the article 
        self.magazine = magazine     # Set the magazine in which the article was published 
        self._title = title   # Set the title of the article 
        Article.all.append(self)   # Add this article instance to the list of all articles

    # Getter for the title property
    @property
    def title(self):
        return self._title

    # Setter for the title property (empty in this case, as setting is not allowed)
    @title.setter
    def title(self, value):
        pass  # No implementation (cannot change the title)


class Author:
    # Constructor of initializing the author with a name
    def __init__(self, name):
        self._name = name         # Set the author's name

    # Getter for the name property
    @property
    def name(self):
        return self._name

    # Setter for the name property (empty in this case, as setting is not allowed)
    @name.setter
    def name(self, value):
        pass  # No implementation (cannot change the name)

    # Method to get all articles written by this author
    def articles(self):
        return [article for article in Article.all if article.author == self] # returns all specific articles written by the specific author

    
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))  # Returns the list of magazines where the the writer has written articles

    # Method to add an article to the author
    def add_article(self, magazine, title):
        return Article(self, magazine, title)  # Creates and returns a new Article instance

    # Method to get the topic areas of the magazines this author has written for
    def topic_areas(self):
        if not self.articles():  #  Returns none if the author has no article
            return None 
        return list(set(magazine.category for magazine in self.magazines()))  # Gets unique category of the magazine where the author has written the articles


class Magazine:
    # Constructor to initialize a magazine with a name and category
    def __init__(self, name, category):
        self._name = name         # Set the magazine's name
        self._category = category # Set the magazine's category

    # Getter for the name property
    @property
    def name(self):
        return self._name

    # Setter for the name property, only allowing strings between 2 and 16 characters
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    # Getter for the category property
    @property
    def category(self):
        return self._category

    # Setter for the category property, ensuring the category is a non-empty string
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0: #  Ensures that the value being assigned to the category is a string
            self._category = value

    # Method to get all articles in this magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Method to get all contributors (authors) for this magazine
    def contributors(self):
        return list(set(article.author for article in self.articles()))  # Unique authors

    # Method to get all titles of articles in the magazine
    def article_titles(self):
        articles = self.articles()  # Get the list of articles for this magazine
        return [article.title for article in articles] if articles else None  # Return titles or None

    # Method to find authors contributing more than 2 articles to this magazine
    def contributing_authors(self):
        author_counts = {}  # Dictionary to count articles per author
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1  # Count articles by each author

        # Get authors who have contributed more than 2 articles
        authors = [author for author, count in author_counts.items() if count > 2]
        return authors if authors else None  # Return authors or None if none found
