#so the purpose of conftest file is used to avoid repatitive task
#exmaple when there is a browser invokation of 100 test cases the conftest can be used to avoid invoaking berowser 100 times
#so to use the fixture we should use the @pytest.fixture annoation
#to define something at a class level then use scope="class" that will help us to avoid mulitiple number of execution
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup():
    print("I Will execute this step first")
    yield
    print("I will execute after executing all the methods")


@pytest.fixture()
def dataload():
    print("user profile is being created")
    return ["Ravi", "teja", "Poorna"]

#data driven and paramterization can be done with retrun statements in tuple format

@pytest.fixture(params=[("chrome","Rahul"),("Microsoft Edge","Ravi")])
def crossBrowser(request):
    return request.param

@pytest.fixture()
def browserInstance():
    options = webdriver.Chrome()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.quit()




