"""Real browser test for a completed RPS round and replay."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_real_round_and_replay(page: Page, live_server, monkeypatch):
    """Play two rounds using the real winner rules."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    page.goto(live_server)

    # First round: rock loses to paper.
    page.get_by_role("button", name="Rock", exact=True).click()

    expect(page.get_by_label("This round’s choices")).to_be_visible()
    expect(page.get_by_text("You chose", exact=True)).to_be_visible()
    expect(page.get_by_text("Computer chose", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Computer wins")).to_be_visible()
    expect(page.locator('[data-outcome="lose"]')).to_have_count(1)

    # Second round: scissors beats paper.
    page.get_by_role("button", name="Scissors", exact=True).click()

    expect(page.get_by_label("This round’s choices")).to_be_visible()
    expect(page.get_by_role("heading", name="You win!")).to_be_visible()
    expect(page.locator('[data-outcome="win"]')).to_have_count(1)
