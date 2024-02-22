import unittest
from human import Human

class HumanTest(unittest.TestCase):

    def test_human(self):
        human = Human(name='John Doe', age=24, gender='M', height_in_inches=56, weight_in_pounds=155, eye_count=2, teeth_count=23, hair_style='short', eye_color='blue', teeth_color='yellow', hair_color='blonde', skin_tone=3, hair_length=3, energy_percentage=100)
        self.assertEqual(human.name, 'John Doe')
        self.assertEqual(human.age, 24)
        self.assertEqual(human.gender, 'M')
        self.assertEqual(human.height, 56)
        self.assertEqual(human.weight, 155)
        self.assertEqual(human.eye_count, 2)
        self.assertEqual(human.teeth_count, 23)
        self.assertEqual(human.hair_style, 'short')
        self.assertEqual(human.eye_color, 'blue')
        self.assertEqual(human.teeth_color, 'yellow')
        self.assertEqual(human.hair_color, 'blonde')
        self.assertEqual(human.skin_tone, 3)
        self.assertEqual(human.hair_length, 3)
        self.assertEqual(human.energy_percentage, 100)

    def test_repr(self):
        human = Human(name='John Doe', age=24, gender='M', height_in_inches=56, weight_in_pounds=155, eye_count=2, teeth_count=23, hair_style='short', eye_color='blue', teeth_color='yellow', hair_color='blonde', skin_tone=3, hair_length=3, energy_percentage=100)
        expected = f'Human(John Doe, 24,\n    M, 56, 155, 2,\n    23, short, blue,\n    yellow, blonde, 3, 3, 100)'
        self.assertEqual(repr(human), expected)

    def test_str(self):
        human = Human(name='John Doe', age=24, gender='M', height_in_inches=56, weight_in_pounds=155, eye_count=2, teeth_count=23, hair_style='short', eye_color='blue', teeth_color='yellow', hair_color='blonde', skin_tone=3, hair_length=3, energy_percentage=100)
        expected = f'name John Doe,\n    24 M, 56 155 \n    2 23 short  blue\n    yellow blonde 3 3 100'
        self.assertEqual(str(human), expected)

if __name__ == '__main__':
    unittest.main()