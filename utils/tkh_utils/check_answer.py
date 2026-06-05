import hashlib
import base64

# Answer key encoded in base64
# Students cannot read these directly
ENCODED_ANSWERS = {
    "A": "QQ==",
    "B": "Qg==",
    "C": "Qw==",
    "D": "RA==",
}

def _encode_answer(letter):
    """Encode an answer letter in base64."""
    return base64.b64encode(
        letter.upper().strip().encode()
    ).decode()

def make_answer_key(answers_dict):
    """
    Create an encoded answer key for a lab.

    Parameters:
    -----------
    answers_dict : dict
        Maps question keys to correct letters
        e.g. {'q1': 'C', 'q2': 'B', 'q3': 'A'}

    Returns:
    --------
    dict: encoded answer key

    Example:
    --------
    _ak = make_answer_key({
        'q1': 'C',
        'q2': 'B',
        'q3': 'A',
        'q4': 'D'
    })
    """
    return {
        k: _encode_answer(v)
        for k, v in answers_dict.items()
    }

def check_answer(student_answer, encoded_correct):
    """
    Check a multiple choice answer without
    revealing the correct answer to students.

    Parameters:
    -----------
    student_answer : str
        The student's answer (A, B, C, or D)
    encoded_correct : str
        The base64 encoded correct answer
        (from make_answer_key())

    Returns:
    --------
    bool : True if correct, False otherwise

    Example:
    --------
    _ak = make_answer_key({'q1': 'C'})
    assert check_answer(q1_answer, _ak['q1']), \\
        "Not quite!"
    """
    if student_answer == "___":
        raise ValueError(
            "Don't forget to fill in "
            "your answer!"
        )
    return _encode_answer(
        str(student_answer)
    ) == encoded_correct

def make_grading_summary(checks, total):
    """
    Print a self-grading summary for Section A.

    Parameters:
    -----------
    checks : list of tuples
        Each tuple: (student_answer,
                     encoded_correct,
                     question_label)
    total : int
        Total number of questions

    Example:
    --------
    make_grading_summary([
        (q1_answer, _ak['q1'],
         "Q1: Central tendency"),
        (q2_answer, _ak['q2'],
         "Q2: Dispersion"),
    ], total=2)
    """
    score = 0
    print("Section A Results:")
    print("="*40)

    for answer, encoded, label in checks:
        if answer == "___":
            print(f"○ {label} — "
                  f"not answered yet")
        elif check_answer(answer, encoded):
            score += 1
            print(f"✓ {label}")
        else:
            print(f"✗ {label} — "
                  f"review this concept")

    print(f"\nScore: {score}/{total}")
    print("-"*40)

    if score == total:
        print("🎉 Perfect score on Section A!")
    elif score >= total * 0.75:
        print("💪 Strong work! Review any "
              "missed questions.")
    else:
        print("📚 Review the working session "
              "notebooks for missed concepts "
              "— that's what they're for!")

    print("\nSection B & C: "
          "check ✓ marks above")
    print("Section D: for your own reflection")
