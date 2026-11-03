"""Unit tests for Rock, Paper, Scissors."""

import pytest

import app as web

from game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_all_nine_outcomes(player, computer, expected):
    """Verify all nine possible game outcomes."""
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
def test_real_round_rock_loses_to_paper(monkeypatch):
    """A real request uses the game rules and displays the correct loss."""
    web.app.config.update(TESTING=True)

    # Fix only the computer's random choice.
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    client = web.app.test_client()
    response = client.post("/", data={"move": "rock"})
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "You chose" in page
    assert "Computer chose" in page
    assert "Rock" in page
    assert "Paper" in page
    assert "Computer wins" in page
    assert 'data-outcome="lose"' in page
