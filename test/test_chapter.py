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
