# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

**Prediction:** I chose rock, and the computer chose paper. I predict I lose because paper covers rock.

**Plan:** Implement all nine Rock, Paper, Scissors outcomes. Display both moves and the correct result. Allow another independent round without saving scores.

**Winning example:** Rock beats scissors.

**Losing example:** Paper beats rock.

**Invalid input:** The server should reject `banana` with HTTP 400 and a helpful message.

**Tests:** Check all nine outcomes, real server requests, invalid inputs, and browser replay. Run the full `check.py` before committing.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- **Issue:** https://github.com/jec87/is218-rps/issues/1
- **Pull request:** https://github.com/jec87/is218-rps/pull/2
- **CI run:** https://github.com/jec87/is218-rps/actions/runs/41564951362/job/125684120274?pr=2
- **Implementation:** Completed `determine_winner()` in [game.py](game.py), supporting all nine outcomes.
- **Unit and integration tests:** [tests/test_game.py](tests/test_game.py) — nine unit cases and one real Flask request/result test.
- **Browser test:** [tests/e2e/test_round.py](tests/e2e/test_round.py) — real Chromium round and replay.
- **Full checks:** `.venv/bin/python check.py` passed Black, Pylint, 23 non-browser tests, and 6 Chromium browser tests.
- **Test explanation:** The rock-versus-paper test checks that the result is `lose`. It would catch a mistake where the game incorrectly returns `win` or `tie`.
- **Browser observation:** I chose paper, the computer chose rock, and I won because paper covers rock. I played again with scissors, and the computer also chose scissors, resulting in a tie.
- **Keyboard observation:** Tab moved between the move buttons, and pressing Enter on Rock started another round.
- **AI assistance:** ChatGPT helped with planning, implementing the rules, writing tests, debugging, and explaining results. I ran the checks and reviewed the game locally.
