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


@htmlFile.asHtmlList
def getList():
    return [2, 3]


class TestHtmlListExtender(unittest.TestCase):
    def test_htmlList(self):
        self.assertEqual(htmlFile.getListAsHtml(),
                         "<ul><li>2</li><li>3</li></ul>")


if __name__ == '__main__':
    unittest.main()
