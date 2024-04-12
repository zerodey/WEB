import pytest
from yandex_testing_lesson import is_under_queen_attack


class Test:
    def test_on_attack(self):
        assert is_under_queen_attack("a1", "a8") is True

    def test_no_attack(self):
        assert is_under_queen_attack("a1", "b8") == False

    def test_wrong_coord(self):
        with pytest.raises(ValueError):
            is_under_queen_attack("abc", "j8")

    def test_wrong_type(self):
        with pytest.raises(TypeError):
            is_under_queen_attack(1, "j8")
