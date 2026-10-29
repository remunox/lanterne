import pytest

from lanterne.rules.abilities import ability_modifier


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (10, 0),
        (1, -5),
        (8, -1),
        (9, -1),
        (11, 0),
        (15, 2),
        (20, 5),
        (30, 10),
    ]
)

def test_ability_modifier(score: int, expected: int) -> None:
    modifier = ability_modifier(score)
    assert modifier == expected
