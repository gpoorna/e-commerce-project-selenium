import pytest




@pytest.mark.usefixtures("dataload")
class TestExample2:
    def test_editprofile(self, dataload):
        print(dataload)

