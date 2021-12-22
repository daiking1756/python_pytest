import pytest
from fizzbuzz import FizzBuzz

class TestFizzBuzz:
    def test_1_converted_to_string1(self):
        actual = FizzBuzz.convert(1)
        assert actual == '1'

    def test_2_converted_to_string2(self):
        actual = FizzBuzz.convert(2)
        assert actual == '2'

# 3の倍数では'Fizz'という文字列に変換する
# 5の倍数では'Buzz'という文字列に変換する
# 3の倍数かつ5の倍数のときは'FizzBuzz'という文字列に変換する
# それ以外のときは数字を文字列に変換する
