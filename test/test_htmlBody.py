from libs.document.Document import Document
from libs.document.Chapter import Chapter
from libs.html.htmlFile import getHtmlBody
import unittest


class TestHtmlBody(unittest.TestCase):
    def setUp(self):
        self.Document = Document()
        self.DocumentWithChapter = Document()

        self.FirstChapterTitle = "this is the first chapter title"

        self.FirstChapter = Chapter(self.FirstChapterTitle)
        self.FirstChapterText = "this is text in the first chapter"
        self.FirstChapter.addText(self.FirstChapterText)
        self.DocumentWithChapter.addChapter(self.FirstChapter)

        self.SecondChapterTitle = "this is the second chapter title"
        self.SecondChapter = Chapter(self.SecondChapterTitle)
        self.DocumentWithChapter.addChapter(self.SecondChapter)

    def test_htmlPageHasBodyTag(self):
        page = getHtmlBody(self.Document)
        self.assertRegex(page, "<body>.*</body>")

    def test_htmlPageHasFirstChapter(self):
        page = getHtmlBody(self.DocumentWithChapter)
        self.assertRegex(
            page, f"<body><h1>{self.FirstChapterTitle}</h1>.*</body>")

    def test_htmlPageHasFirstChapterWithCorrectText(self):
        page = getHtmlBody(self.DocumentWithChapter)
        self.assertRegex(
            page, f".*</h1>{self.FirstChapterText}.*")

    def test_htmlPageHasSecondChapter(self):
        page = getHtmlBody(self.DocumentWithChapter)
        self.assertRegex(
            page,
            f"<body><h1>.*</h1>.*<h1>{self.SecondChapterTitle}</h1>.*</body>")
