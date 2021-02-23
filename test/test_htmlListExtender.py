import libs.html.htmlFile as htmlFile
import unittest


@htmlFile.asHtmlList
def getList():
    return [2, 3]


class TestHtmlListExtender(unittest.TestCase):
    def test_htmlList(self):
        self.assertEqual(htmlFile.getListAsHtml(),
                         "<ul><li>2</li><li>3</li></ul>")
