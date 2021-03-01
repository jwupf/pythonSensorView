from libs.document.Document import Document
from libs.document.Chapter import Chapter
from libs.html.htmlFile import getHtmlPage
import unittest


class TestHtmlFile(unittest.TestCase):
    def setUp(self):
        self.Title = "this is the page title"
        self.Document = Document(self.Title)

        self.DocumentWithChapter = Document(self.Title)        

        self.FirstChapterTitle = "this is the first chapter title"
        self.FirstChapterText = "this is text in the first chapter"
        self.FirstChapter = Chapter(self.FirstChapterTitle)
        self.DocumentWithChapter.addChapter(self.FirstChapter)

        self.SecondChapterTitle = "this is the second chapter title"
        self.SecondChapterText = "this is text in the second chapter"
        self.SecondChapter = Chapter(self.SecondChapterTitle)     
        self.DocumentWithChapter.addChapter(self.SecondChapter)

    def test_htmlPageHasDocType(self):
        page = getHtmlPage(self.Document)
        self.assertRegex(page, "^<!DOCTYPE html>")

    def test_htmlPageHasHtmlTag(self):
        page = getHtmlPage(self.Document)
        self.assertRegex(page, ".*<html>.*</html>")

    def test_htmlPageHasHeadTag(self):
        page = getHtmlPage(self.Document)
        self.assertRegex(page, ".*<html><head>")

    def test_htmlPageHasBodyTag(self):
        page = getHtmlPage(self.Document)
        self.assertRegex(page, ".*</head><body>.*</body>")

    def test_htmlPageHasFirstChapter(self):
        page = getHtmlPage(self.DocumentWithChapter)
        self.assertRegex(page, f".*</head><body><h1>{self.FirstChapterTitle}</h1>.*</body>")

    def test_htmlPageHasSecondChapter(self):
        page = getHtmlPage(self.DocumentWithChapter)
        self.assertRegex(page, f".*</head><body><h1>.*</h1>.*<h1>{self.SecondChapterTitle}</h1>.*</body>")

    def test_htmlPageHasGivenTitle(self):
        head = getHtmlPage(self.Document)
        self.assertRegex(head, f"<title>({self.Title})</title>")
