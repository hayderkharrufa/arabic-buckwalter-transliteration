import unittest
from arabic_buckwalter_transliteration.transliteration import buckwalter_to_arabic, arabic_to_buckwalter

class TestTransliteration(unittest.TestCase):
    
    def test_buckwalter_to_arabic(self):
        self.assertEqual(buckwalter_to_arabic('Aalos~alAmu Ealayokumo yaA Sadiyqiy'),
                         'اَلْسَّلامُ عَلَيْكُمْ يَا صَدِيقِي')

    def test_arabic_to_buckwalter(self):
        self.assertEqual(arabic_to_buckwalter('اَلْسَّلامُ عَلَيْكُمْ يَا صَدِيقِي'),
                         'Aalos~alAmu Ealayokumo yaA Sadiyqiy')

if __name__ == '__main__':
    unittest.main()