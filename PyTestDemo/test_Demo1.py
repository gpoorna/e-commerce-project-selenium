#Any pytest test file should start with prefix test_ or it can end with test_
#method name in pytest should start with test_
#Any code should be wrapped in the method
#we can run the py test file using test runner or command line (Command to run all files : py.test)
#command to get the imnforation of (py.test -v & to get the log info py.test -v)
#in pytest every method is treated as a test case
#command to run specfic pytest file: py.test filename.py -v -s
#you can mark tag @test @py.test.mark.smoke and then run with -m
#you cam skip the test with tag @pytest.mark.skip
#data driven and paramterization can be done with retrun statements in tuple format
#when you define scope to class only, it will run once before class is intiated and at end
#to generate the html reports use the following command py.test --html=report.html

import pytest


@pytest.mark.smoke
def test_firstprogram():
    print("hello")


@pytest.mark.xfail
def test_greetsecondcreditCard():
    print("Good morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
