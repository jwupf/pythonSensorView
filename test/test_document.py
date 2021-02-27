from libs.document.Document import Document
import unittest


class TestDocument(unittest.TestCase):
    def test_document(self):
        doc = Document()        
        self.assertIsNotNone(doc)

    def test_DocumentHasTitle(self):
        title = "This is my title"
        doc = Document(title)
        self.assertEqual(doc.title,title)