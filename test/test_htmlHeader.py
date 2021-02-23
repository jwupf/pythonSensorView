import libs.html.htmlFile as htmlFile
import unittest


class TestHtmlHeader(unittest.TestCase):
    def test_htmlHeaderHasHeadTag(self):
        head = htmlFile.getHtmlHeader()
        self.assertRegex(head, "^<head>.*</head>")

    def test_htmlHeaderHasTitleTag(self):
        head = htmlFile.getHtmlHeader()
        self.assertRegex(head, "^<head><title>.*</title>")

    def test_htmlHeaderHasNonEmptyTitle(self):
        head = htmlFile.getHtmlHeader()
        self.assertRegex(head, "<title>.+</title>")

    def test_htmlHeaderHasGivenTitle(self):
        title = "this is the page title"
        head = htmlFile.getHtmlHeader(title)
        self.assertRegex(head, f"<title>({title})</title>")
