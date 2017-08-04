import unittest
from abstract_enum import AbstractEnum

class Greetings(AbstractEnum):
    pass

class GreetingsBase(object):
    greeting = "Hello World!"

    @classmethod
    def greet(cls):
        return cls.greeting

class BasicTest(unittest.TestCase):
    class FrenchGreeting(GreetingsBase):
        __alias__ = "FRENCH"
        greeting = "Bonjour!"

    class GermanGreeting(GreetingsBase):
        __alias__ = "GERMAN"
        greeting = "Guten Tag!"

    class ItalianGreeting(GreetingsBase):
        __alias__ = "ITALIAN"
        greeting = "Buongiorno!"

    def test_instantiation(self):
        Greetings.initialize(GreetingsBase)
        self.assertTrue(hasattr(Greetings, "GERMAN"))
        self.assertTrue(hasattr(Greetings, "FRENCH"))
        self.assertTrue(hasattr(Greetings, "ITALIAN"))

    def test_content(self):
        Greetings.initialize(GreetingsBase)
        self.assertEqual(Greetings.FRENCH.greet(), "Bonjour!")
        self.assertEqual(Greetings.ITALIAN.greet(), "Buongiorno!")

    def test_integrity(self):
        class Farewells(AbstractEnum):
            pass
        Greetings.initialize(GreetingsBase)
        Farewells.initialize(GreetingsBase)
        self.assertNotEqual(Greetings.FRENCH, Farewells.FRENCH)
        self.assertNotEqual(Greetings.ITALIAN, Farewells.ITALIAN)

if __name__ == '__main__':
    unittest.main()