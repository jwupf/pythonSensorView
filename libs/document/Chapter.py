class Chapter:
    def __init__(self, title=None):
        self.Title = title
        self.Text = []
        self.Lists = []

    def addText(self, text):
        self.Text.append(text)

    def addList(self, data):
        self.Lists.append(data)
