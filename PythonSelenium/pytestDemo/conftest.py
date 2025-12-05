import pytest


@pytest.fixture(scope="class")
def setup():
    print(" i will excute first ")
    yield
    print("i will excute last ")


@pytest.fixture()
def getdata():
    print(" I will execute in getdat method")
    return ["ramu", "Meenuga", "rahushettyacedemy.com"]


@pytest.fixture(params=[("chrome","ramu","wabtec"), "firfox", "IE"])
def crossBrowser(request):
    return request.param