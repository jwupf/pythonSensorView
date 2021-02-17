import htmlFile
import unittest


class TestAddMethod(unittest.TestCase):

    def test_html(self):
        self.assertEqual(htmlFile.getHtmlPage(), "<!DOCTYPE html><html></html>")


    def test_value(self):
        self.assertEqual(htmlFile.getValue(), 3)

    def test_list(self):
        self.assertListEqual(htmlFile.getList(), [2,3])

    def test_htmlList(self):
        self.assertEqual(htmlFile.getListAsHtml(), "<ul><li>2</li><li>3</li></ul>")

if __name__ == '__main__':
    unittest.main()