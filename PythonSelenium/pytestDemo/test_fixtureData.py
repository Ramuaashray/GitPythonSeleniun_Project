import pytest

from pytestDemo.conftest import getdata

@pytest.mark.usefixtures("getdata")
class TestExamole:

    def test_editprofile(self, getdata):
        print(getdata)

        print(getdata[0])
        print(getdata[2])
