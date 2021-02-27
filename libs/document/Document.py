class Document:
    def __init__(self, title = None):
        self.Title = title    
        self.Chapters = []
    
    def addChapter(self, chapter):
        self.Chapters.append(chapter)