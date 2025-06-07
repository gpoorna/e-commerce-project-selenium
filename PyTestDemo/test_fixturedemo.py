#the purpose of fixtures is use to open browser instnaces and estbalish the database connection and to perofrm something repatedly
#Note : Yeild use to perform break or alter the execution flow
#To use the fixtures from conftest file use @pytest.mark.usefixtures("methodname from conftest ")
#we can actually pass the data from the fixtures
#fixtures are used as setup and tear down methods for test cases-conftest file to generalize the fixture
#fixture make it aviliable to all test cases

import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
         print("I will execute this step later")

    def test_fixtureDemo1(self):
        print("I will execute this step in fixture 1 method")

    def test_fixtureDemo2(self):
        print("I will execute this step in fixture 2 method")

    def test_fixtureDemo3(self):
        print("I will execute this step in fixture 3 method")

