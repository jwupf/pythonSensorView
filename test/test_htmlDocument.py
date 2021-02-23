import libs.html.htmlFile as htmlFile
import unittest


class TestHtmlDocument(unittest.TestCase):
    def test_htmlPageHasDocType(self):
        page = htmlFile.getHtmlPage()
        self.assertRegex(page, "^<!DOCTYPE html>")

    def test_htmlPageHasHtmlTag(self):
        page = htmlFile.getHtmlPage()
        self.assertRegex(page, ".*<html>.*</html>")

    def test_htmlPageHasHeadTag(self):
        page = htmlFile.getHtmlPage()
        self.assertRegex(page, ".*<html><head>")

    def test_htmlPageHasBodyTag(self):
        page = htmlFile.getHtmlPage()
        self.assertRegex(page, ".*</head><body>.*</body>")

    def test_htmlPageHasGivenTitle(self):
        title = "this is the page title"
        head = htmlFile.getHtmlPage(title)
        self.assertRegex(head, f"<title>({title})</title>")
