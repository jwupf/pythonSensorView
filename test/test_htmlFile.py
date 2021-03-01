from libs.document.Document import Document
from libs.html.htmlFile import getHtmlPage
import unittest


class TestHtmlFile(unittest.TestCase):
    def setUp(self):
        self.Title = "this is the page title"
        self.Document = Document(self.Title)

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

    def test_htmlPageHasGivenTitle(self):
        head = getHtmlPage(self.Document)
        self.assertRegex(head, f"<title>({self.Title})</title>")
