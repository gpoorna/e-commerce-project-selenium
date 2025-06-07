#Any pytest test file should start with prefix test_ or it can end with test_
#method name in pytest should start with test_
#Any code should be wrapped in the method
#we can run the py test file using test runner or command line (Command to run all files : py.test)
#command to get the imnforation of (py.test -v & to get the log info py.test -v)
#in pytest every method is treated as a test case
#in pyest if you want to run any specfic testcase or function then you should use regualar expression
#py.test -k methodname -s
#method nmae should have sense
#fixtures are used as setup and tear down methods for test cases- Conftest file to genarlize
#fixture  and make it aviliable to testcases
import pytest


#we can recongise the methods with mark , it will be useful when we wanted to perform smoke testing and regression testing

@pytest.mark.smoke
def test_firstprogram():
    msg = "Hello"
    assert msg == "Hello", "test failed because strings does not match"

def test_secondcreditprogram():
    a = 4
    b = 3
    assert a+4 == 8 ,"Addittion doesn't match "