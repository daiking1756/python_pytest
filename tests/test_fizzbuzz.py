import pytest
from fizzbuzz import FizzBuzz

class TestFizzBuzz:
    class TestMultipleOf3IsConvertedToFizz:
        def test_3_converted_to_Fizz(self):
            assert FizzBuzz.convert(3) == 'Fizz'

    class TestMultipleOf5IsConvertedToBuzz:
        def test_5_converted_to_Fizz(self):
            assert FizzBuzz.convert(5) == 'Buzz'

    class TestMultipleOf3And5IsConvertedToFizzBuzz:
        def test_15_converted_to_FizzBuzz(self):
            assert FizzBuzz.convert(15) == 'FizzBuzz'

    class TestOtherNumber:
        def test_1_converted_to_string1(self):
            for i in range(1, 100):
                print('%s: FizzBuzz.convert(%s)', i, FizzBuzz.convert(i))

            assert FizzBuzz.convert(1) == '1'
