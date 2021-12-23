import pytest
from integer_closed_interval import IntegerClosedInterval

class TestIntegerClosedInterval():
    def test_has_lower_endpoint_3(self):
            assert IntegerClosedInterval().lower_endpoint == 3

# 整数閉区間クラスの仕様(`IntegerClosedInterval``)
    # メンバ変数
        # - [] 整数閉区間クラスは下端点(`lower endpoint`)をメンバ変数に持つ
        # - [] 整数閉区間クラスは上端点(`upper endpoint``)をメンバ変数に持つ
    # メソッド
        # - [] 整数閉区間クラスは文字列表記を返すメソッド(`get_integer_closed_interval_as_string()`)を持つ
            # 例: 下端点 3, 上端点 7 の整数閉区間の文字列表記は "[3,7]"
        # - [] 整数閉区間クラスは指定した整数を含むかどうかを判定し、Boolean値(true/false)を返すメソッド(`is_contain()`)を持つ
