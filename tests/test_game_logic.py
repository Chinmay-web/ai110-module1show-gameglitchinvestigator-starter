from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_single_digit_guess_too_low():
    # 9 < 50 numerically; a string secret compared "9" > "50" and said "Too High"
    result = check_guess(9, 50)
    assert result == "Too Low"

def test_guess_too_high_returns_outcome_only():
    # check_guess used to return an (outcome, message) tuple with a backwards hint
    result = check_guess(60, 50)
    assert result == "Too High"

def test_parse_guess_rejects_non_number():
    ok, guess_int, err = parse_guess("abc")
    assert ok is False
    assert guess_int is None
    assert err == "That is not a number."
