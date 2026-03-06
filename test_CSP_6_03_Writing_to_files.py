import CSP_6_03_Writing_to_files as hw


def read_text(filename):
    with open(filename, "r") as f:
        return f.read()


def test_writeFile():
    # Test 1
    hw.writeFile(["b", "a", "c"], "test_out.txt")
    assert read_text("test_out.txt") == "b\na\nc\n"

# Test 2
# Make sure the input file exists
def test_sortNames():
    hw.writeFile(["zoe", "amy", "bob"], "6_03_test_names.txt")

    hw.sortNames("6_03_test_names.txt", "namesNew.txt")
    assert read_text("namesNew.txt") == "amy\nbob\nzoe\n"


# test3
def test_highScore():
    hw.writeFile([50, 70], "scores.txt")

    avg = hw.highScore(80)  # should append 80, then average = (50+70+80)/3
    assert abs(avg - ((50 + 70 + 80) / 3)) < 1e-9


print("All tests passed")