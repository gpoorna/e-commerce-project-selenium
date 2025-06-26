import os
import re

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture( scope="function" )
def browserInstance(request):
    global driver
    browser_name = request.config.getoption( "browser_name" )
    service_obj = Service()
    if browser_name == "chrome":  #firefox
        driver = webdriver.Chrome( service=service_obj )
    elif browser_name == "firefox":
        driver = webdriver.Firefox( service=service_obj )
    driver.maximize_window()
    driver.implicitly_wait( 5 )
    driver.get( "https://rahulshettyacademy.com/loginpagePractise/" )
    yield driver  #Before test function execution
    driver.close()  #post your test function execution

#hook implematition is to capture failure scanrios
@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname( __file__ ), 'poornareports') #reports is a folder name

            os.makedirs(reports_dir, exist_ok=True)

            # Fix the mixed path separators issue
            clean_nodeid = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            # Remove problematic characters
            clean_nodeid = re.sub(r'[<>:"/\\|?*\[\]]', '_', clean_nodeid)
            file_name = os.path.normpath(os.path.join(reports_dir, clean_nodeid + ".png"))
            #file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    try:
        driver.get_screenshot_as_file(file_name)
        print(f"Screenshot saved: {file_name}")
    except Exception as e:
        print(f"failed to capture the screen shot: {e}")

