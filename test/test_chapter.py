from libs.document.Chapter import Chapter
import unittest


class TestChapter(unittest.TestCase):
    def test_chapter(self):
        chap = Chapter()
        self.assertIsNotNone(chap)

    def test_ChapterHasTitle(self):
        title = "This is my title"
        chap = Chapter(title)
        self.assertEqual(chap.Title, title)

    def test_ChapterCanLiveWithoutTitle(self):
        chap = Chapter()
        self.assertEqual(chap.Title, None)

    def test_ChapterCanAddText(self):
        text = "blahBlah"
        chap = Chapter()
        chap.addText(text)
        self.assertIn(text, chap.Text)

    def test_canAddMoreText(self):
        chap = Chapter()
        text1 = "text1 blahBlah"
        chap.addText(text1)
        text2 = "text2 blahBlah"
        chap.addText(text2)
        self.assertIn(text1, chap.Text)
        self.assertIn(text2, chap.Text)
