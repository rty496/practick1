# Write the body of the function to make the script work without errors
def grade(score: int) -> str:
    pass


if __name__ == "__main__":
    # Do not change the below asserts
    assert grade(95) == "A"
    assert grade(85) == "B"
    assert grade(75) == "C"
    assert grade(65) == "D"
    assert grade(50) == "F"