from libs.document.Document import Document
from libs.document.Chapter import Chapter

import unittest


class TestDocument(unittest.TestCase):
    def test_document(self):
        doc = Document()
        self.assertIsNotNone(doc)

    def test_DocumentHasTitle(self):
        title = "This is my title"
        doc = Document(title)
        self.assertEqual(doc.Title, title)

    def test_AddChapterToDocument(self):
        doc = Document()
        chapterTitle = "A new beginning"
        chapter = Chapter(chapterTitle)
        doc.addChapter(chapter)
        self.assertIn(chapter, doc.Chapters)
