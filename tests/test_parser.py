from unittest import TestCase
from _parser import parse, parse_conditional


class TestParse(TestCase):

    """

    Expression tests

    """

    def test_single_expression(self):

        source = ['print("Test")']
        expected = ['print("Test")']
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_multiple_expression(self):

        source = ['print("Test one")',
                  'print("Test two")']

        expected = ['print("Test one")', 'print("Test two")']
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    """

    Conditional tests

    """

    def test_single_if(self):

        source = ['if True:',
                  '    print("Test")']

        expected = [['if True:', 'print("Test")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_multiple_if(self):

        source = ['if True:',
                  '    print("Test one")',
                  'if True:',
                  '    print("Test two")']

        expected = [['if True:', 'print("Test one")'], ['if True:', 'print("Test two")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_nested_if(self):

        source = ['if True:',
                  '    print("Test one")',
                  '    if True:',
                  '        print("Test two")']

        expected = [['if True:', 'print("Test one")'], ['if True:', 'print("Test two")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_expression_following_if(self):

        source = ['if True:',
                  '    print("Test one")',
                  'print("Test two")']

        expected = [['if True:', 'print("Test one")'], 'print("Test two")']
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_if_following_expression(self):

        source = ['print("Test one")',
                  'if True:',
                  '    print("Test two")']

        expected = ['print("Test one")', ['if True:', 'print("Test two")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_if_else(self):

        source = ['if True:',
                  '    print("Test one")',
                  'else:',
                  '    print("Test two")']

        expected = [['if True:', 'print("Test one")'], ['else:', 'print("Test two")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_if_elif(self):

        source = ['if True:',
                  '    print("Test one")',
                  'elif False:',
                  '    print("Test two")']

        expected = [['if True:', 'print("Test one")'], ['elif False:', 'print("Test two")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_if_elif_else(self):

        source = ['if True:',
                  '    print("Test one")',
                  'elif False:',
                  '    print("Test two")',
                  'else:',
                  '    print("Test three")']

        expected = [['if True:', 'print("Test one")'], ['elif False:', 'print("Test two")'], ['else:', 'print("Test three")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_if_multiple_elif(self):

        source = ['if True:',
                  '    print("Test one")',
                  'elif False:',
                  '    print("Test two")',
                  'elif True:',
                  '    print("Test three")']

        expected = [['if True:', 'print("Test one")'], ['elif False:', 'print("Test two")'], ['elif True:', 'print("Test three")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_if_multiple_elif_else(self):

        source = ['if True:',
                  '    print("Test one")',
                  'elif False:',
                  '    print("Test two")',
                  'elif True:',
                  '    print("Test three")',
                  'else:',
                  '    print("Test four")']

        expected = [['if True:', 'print("Test one")'], ['elif False:', 'print("Test two")'], ['elif True:', 'print("Test three")'], ['else:', 'print("Test four")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    # TODO write the rest of the elif and else unit tests

    """
    Loop tests
    """

    def test_single_while(self):

        source = ['while True:',
                  '    print("Test")']

        expected = [['while True:', 'print("Test")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_single_foreach(self):

        source = ['for x in ["Test one", "Test two"]:',
                  '    print("Test")']

        expected = [['for x in ["Test one", "Test two"]:', 'print("Test")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    def test_single_for(self):

        source = ['for x in range(0, 10):',
                  '    print("Test")']

        expected = [['for x in range(0, 10):', 'print("Test")']]
        parsed_source = parse(source)

        self.assertEqual(expected, parsed_source)

    # TODO write the rest of the while and for loop unit tests

    """
    Function tests
    """

    # TODO write the function unit tests

    """
    Class tests
    """

    # TODO write the class unit tests
