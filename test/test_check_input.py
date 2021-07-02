import unittest
import os, sys
import numpy as np

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
#print(SCRIPT_DIR)
#print(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
#print(os.path.expanduser(__file__))

class TestCase(unittest.TestCase):

    def test_integers_simple(self):
        from src.check_input import check_input
        options = [-220,-22,-11,-2,-1,0,1,2,11,22,220]
        for input in options:
            self.assertEqual(input, check_input(input, options))

    def test_integers_part(self):
        from src.check_input import check_input
        options = [-22,-11,-2,-1,0,1,2,11,22]
        for input in [-2,-1,0,1,2]:
            self.assertEqual(input, check_input(input, options))

    def test_integers_mismach1(self):
        from src.check_input import check_input
        options = [1,2]
        input = 1.0
        #assert input == check_input(input, options)
        self.assertEqual(input, check_input(input, options))
        input = 2.0
        self.assertEqual(input, check_input(input, options))

    def test_integers_mismash2(self):
        from src.check_input import check_input
        options = [-22,-11,-2,-1,0,1,2,11,22]
        for input in [-22.0,-11.0,-2.0,-1.0,0.0,1.0,2.0,11.0,22.0]:
            self.assertEqual(input, check_input(input, options))

    def test_integers_random(self):
        from src.check_input import check_input
        #options = np.random.choice(np.random.randint(0,1000000,10000),10,replace=False)
        options = [int(a) for a in np.random.randint(0,1000000,1000)]
        options = list(np.random.randint(0,1000000,1000))
        print(options[0].__class__)
        for input in options:
            self.assertEqual(input, check_input(input, options))

    '''
    def test_integers_mismash3(self):
        from src.check_input import check_input
        options = [-22,-11,-2,-1,0,1,2,11,22]
        for input in options:
            with self.assertRaises(TypeError):
                check_input(input, options)
    '''

    def test_floats_simple(self):
        from src.check_input import check_input
        options = [-220.9,-22.8,-11.7,-2.6,-1.5,0.4,1.3,2.2,11.1,22.0, 220.99]
        for input in options:
            self.assertEqual(input, check_input(input, options))

    def test_floats_part(self):
        from src.check_input import check_input
        options = [-22.0,-11.0,-2.0,-1.0,0.0,1.0,2.0,11.0,22.0]
        for input in [-2,-1,0,1,2]:
            self.assertEqual(input, check_input(input, options))

    def test_floats_mismash1(self):
        from src.check_input import check_input
        options = [1.0,2.0]
        input = 1
        #assert input == check_input(input, options)
        self.assertEqual(input, check_input(input, options))
        input = 2
        self.assertEqual(input, check_input(input, options))

    def test_floats_mismash2(self):
        from src.check_input import check_input
        options = [-22,-11,-2,-1,0,1,2,11,22]
        for input in [-22.0,-11.0,-2.0,-1.0,0.0,1.0,2.0,11.0,22.0]:
            self.assertEqual(input, check_input(input, options))

    def test_floats_random(self):
        from src.check_input import check_input
        options = list(np.random.random(1000)*1000000)
        print(options[0].__class__)
        for input in options:
            self.assertEqual(input, check_input(input, options))

    '''
    def test_integers_mismash3(self):
        from src.check_input import check_input
        options = [-22,-11,-2,-1,0,1,2,11,22]
        for input in options:
            with self.assertRaises(TypeError):
                check_input(input, options)
    '''

    def test_strings_simple(self):
        from src.check_input import check_input
        options = ["ahoj","alabama"]
        for input in options:
            self.assertEqual(input, check_input(input, options))

    def test_strings_capital_letters(self):
        from src.check_input import check_input
        options = ["Ahoj","ahoj"]
        self.assertEqual("ahoj", check_input("ahoj", options))
        self.assertEqual("Ahoj", check_input("Ahoj", options))
        self.assertEqual("ahoj", check_input("ahoj", options, False))
        self.assertEqual("Ahoj", check_input("Ahoj", options, False))

    def test_strings_parts1(self):
        from src.check_input import check_input
        options = ["Ahoj","ahoj",'A','a']
        #assert input == check_input(input, options)
        for input in options:
            self.assertEqual(input, check_input(input, options))

    def test_strings_parts2(self):
        from src.check_input import check_input
        options = ["Ahoj","ahoj",'Ah','ah']
        #assert input == check_input(input, options)
        for input in options:
            print(input, check_input(input[0], options))
            self.assertEqual(None, check_input(input[0], options))

    '''
    def test_integers_mismash3(self):
        from src.check_input import check_input
        options = ["Ahoj","ahoj"]
        for input in [-2,-1,0,1,2]:
            self.assertEqual(input[0], check_input(input, options))
    '''
