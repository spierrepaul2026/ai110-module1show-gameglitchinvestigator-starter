from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the high/low bug ---
# On even attempts app.py passed the secret in as a string. The old code fell
# back to a string comparison, which reported the wrong direction. These make
# sure check_guess stays correct when the secret arrives as a string.

def test_too_high_with_string_secret():
    # "90" vs "30": string compare "9" > "3" is right by luck, but 90 > 30 as ints too.
    outcome, _ = check_guess(90, "30")
    assert outcome == "Too High"


def test_too_low_with_string_secret():
    # "100" vs "80": string compare "1" < "8" -> "Too Low" (wrong!). As ints 100 > 80.
    outcome, _ = check_guess(100, "80")
    assert outcome == "Too High"


def test_win_with_string_secret():
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"


def test_message_returned_with_outcome():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📈 Go HIGHER!"
