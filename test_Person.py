import unittest
from .person import Person

class Testing(unittest.TestCase):
    def setting_name(self):
        person = Person()
         letters = person.person.set_name('Antonio')
        self.assertEqual(letters, 7)

    def test_boolean(self):
        person = Person()
        letters = person.person.set_name('Antonio')
        name = person.get_name(0)
        self.assertEqual(name, 'Antonio')

if __name__ == '__main__':
    unittest.main()