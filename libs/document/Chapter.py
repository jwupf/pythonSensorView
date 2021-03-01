class Chapter:
    def __init__(self, title = None):
        self.Title = title    
        self.Text = []

    def addText(self, text):
        self.Text.append(text)
    