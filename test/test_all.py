import libs.html.htmlFile as htmlFile
import unittest


@htmlFile.asHtmlList
def getList():    
    return [2,3]

def getValue():
    return 3

class TestAddMethod(unittest.TestCase):

    def test_html(self):
        self.assertEqual(htmlFile.getHtmlPage(), "<!DOCTYPE html><html></html>")


    def test_value(self):
        self.assertEqual(getValue(), 3)

    def test_list(self):
        self.assertListEqual(getList(), [2,3])

    def test_htmlList(self):
        self.assertEqual(htmlFile.getListAsHtml(), "<ul><li>2</li><li>3</li></ul>")

if __name__ == '__main__':
    unittest.main()