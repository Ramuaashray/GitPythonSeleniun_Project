#any pytest file should start with test_
import pytest


def test_demo_2():
    msg = "hello"
    assert msg == "hi"


@pytest.mark.smoke
def test_secondprogram(setup):
    a = 4
    b = 6
    assert a+2 == 6, "addition is doesnt match"
    print("sum all a+b : ", a+b)

@pytest.mark.skip
def test_sampleofskip():
    print("skiping ")
