

from score import calculate_score


def test_score():
    ans = calculate_score([1])
    assert ans == 100

    ans = calculate_score([5])
    assert ans == 50

    ans = calculate_score([1,5])
    assert ans == 150

    ans = calculate_score([1,1])
    assert ans == 200

    ans = calculate_score([5,5])
    assert ans == 100

    ans = calculate_score([1,1,5,5])
    assert ans == 300

    # ans = calculate_score([1])
    # assert ans == 100

    ans = calculate_score([1,2,3,4,5,6])
    assert ans == 2000

    ans = calculate_score([1,2,3,4,5,3])
    assert ans == 1500

    ans = calculate_score([1,2,3,4,5,5])
    assert ans == 1550

    ans = calculate_score([1,2,3,4,5,1])
    assert ans == 1600

    ans = calculate_score([2,2,3,4,5,6])
    assert ans == 1500





    print("Tests Passed!")

if __name__=="__main__":
    test_score()