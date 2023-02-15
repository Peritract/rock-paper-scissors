import pytest

from rps import get_computer_choice, score_game, get_player_choice

def test_computer_choice_is_valid():
    """Checks if the computer only chooses R, P, or S"""
    for i in range(1000):
        assert get_computer_choice() in ['R', 'P', 'S']

test_data = [
    ['R', 'S', 'player_win'],
    ['P', 'P', 'draw'],
    ['R', 'R', 'draw']
]

@pytest.mark.parametrize("player,computer,expected", test_data)
def test_scoring_accuracy(player, computer, expected):

    assert score_game(player, computer) == expected

@pytest.mark.parametrize("value", ["R", "P", "S"])
def test_player_choice_is_valid(monkeypatch, value):
    """Checks that the player choice is R, P, or S"""

    monkeypatch.setattr('builtins.input', lambda x: value)

    assert get_player_choice() == value