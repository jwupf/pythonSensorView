import libs.html.htmlFile as htmlFile
import unittest


@htmlFile.asHtmlList
def getList():    
    return [2,3]

class TestAddMethod(unittest.TestCase):

    def test_htmlPageHasDocType(self):
        page = htmlFile.getHtmlPage()
        self.assertRegex(page,"^<!DOCTYPE html>")
    
    def test_htmlPageHasHtmlTag(self):
        page = htmlFile.getHtmlPage()
        self.assertRegex(page,".*<html>.*</html>")
    
    def test_htmlPageHasHeadTag(self):
        page = htmlFile.getHtmlPage()
        self.assertRegex(page,".*<html><head>.*</head>")

    def test_htmlPageHasTitleTag(self):
        page = htmlFile.getHtmlPage()
        self.assertRegex(page,".*<head><title>.*</title>")

    def test_htmlPageHasNonEmptyTitle(self):
        page = htmlFile.getHtmlPage()
        self.assertRegex(page,"<title>.+</title>")

    def test_htmlPageHasBodyTag(self):
        page = htmlFile.getHtmlPage()
        self.assertRegex(page,".*</head><body>.*</body>")

    def test_htmlList(self):
        self.assertEqual(htmlFile.getListAsHtml(), "<ul><li>2</li><li>3</li></ul>")

    
if __name__ == '__main__':
    unittest.main()