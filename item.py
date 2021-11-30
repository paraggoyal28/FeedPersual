import html


class Item:
    def __init__(self, title, description, link):
        self.title = title
        self.description = description
        self.link = link

    def __str__(self):
        return (f'---------------\nTitle: {self.title}\nDescription: {self.description}\nLink: {self.link}\n-----------------------\n')
