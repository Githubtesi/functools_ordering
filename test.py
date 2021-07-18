"""
https://docs.python.org/ja/3/library/functools.html#functools.total_ordering
"拡張比較 (rich comparison)の簡易入力"
x< y は x.__lt__(y)　x<=y は x.__le__(y)
x==y は x.__eq__(y)　x!=y は x.__ne__(y)
x> y は x.__gt__(y)　x>=y は x.__ge__(y)
注意：実行時間が遅い場合ここを書き換えると高速化されることが多々ある
"""

from functools import total_ordering


@total_ordering
class Student:
    """名前を設定"""

    def __init__(self, firstname, lastname):
        self.lastname = lastname
        self.firstname = lastname

    def _is_valid_operand(self, other):
        """ otherのインスタンス変数にlastnameとfirstnameを持っているか """
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))

    def __eq__(self, other):
        """ == x==y は x.__eq__(y) """
        if not self._is_valid_operand(other):
            return NotImplemented
        return all([
            self.lastname.lower() == other.lastname.lower(),
            self.lastname.lower() == other.lastname.lower()]
        )

    def __lt__(self, other):
        """ x<y は x.__lt__(y) """
        if not self._is_valid_operand(other):
            return NotImplemented
        return all([
            self.lastname.lower() < other.lastname.lower(),
            self.lastname.lower() < other.lastname.lower()]
        )

    @property
    def show(self):
        print(self.firstname, self.lastname)


if __name__ == '__main__':
    a = Student("edogawa", "konan")
    b = Student("mituhiko", "mituhiko")
    c = Student("genta", "genta")

    a == c
    l = [a, b, c]
    l.sort()  # ソートの実行
    for student in l:
        student.show
