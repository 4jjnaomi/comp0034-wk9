import time

import requests
from dash.testing.application_runners import import_app
from selenium.webdriver.common.by import By


def test_server_live(dash_duo):
    """
    GIVEN the app is running
    WHEN a HTTP request to the home page is made
    THEN the HTTP response status code should be 200
    """

    # Start the app in a server
    app = import_app(app_file="paralympics_dash_multi.paralympics_app")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Get the url for the web app root
    # You can print this to see what it is e.g. print(f'The server url is {url}')
    url = dash_duo.driver.current_url

    # Requests is a python library and here is used to make a HTTP request to the sever url
    response = requests.get(url)

    # Finally, use the pytest assertion to check that the status code in the HTTP response is 200
    assert response.status_code == 200

def test_home_h1textequals(dash_duo):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading text should be "Paralympics Dashboard"
    """
    app = import_app(app_file="paralympics_dash_multi.paralympics_app")
    dash_duo.start_server(app)

    # Wait for the H1 heading to be visible, timeout if this does not happen within 4 seconds
    dash_duo.wait_for_element("h1", timeout=4)

    # Find the text content of the H1 heading element
    h1_text = dash_duo.find_element("h1").text

    # Check the heading has the text we expect
    assert h1_text == "Event Details"

def test_nav_link_charts(dash_duo):
    """
    Check the nav link works and leads to the charts page.
    """
    app = import_app(app_file="paralympics_dash_multi.paralympics_app")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)

    # Wait for the navlink to be visible
    dash_duo.wait_for_element("#nav-charts", timeout=4)

    # Click on the navlink
    dash_duo.driver.find_element(By.ID, "nav-charts").click()

    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(2)

    # Check the page url includes "charts"
    dash_duo.wait_for_element("#nav-charts", timeout=4)
    assert "charts" in dash_duo.driver.current_url

def test_nav_link_event(dash_duo):
    """
    Check the nav link works and leads to the event page.
    """
    app = import_app(app_file="paralympics_dash_multi.paralympics_app")
    dash_duo.start_server(app)
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(1)

    # Wait for the charts navlink to be visible
    dash_duo.wait_for_element("#nav-charts", timeout=4)
    # Click on the charts page navlink
    dash_duo.driver.find_element(By.ID, "nav-charts").click()
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(1)
    # Wait for the event navlink to be visible
    dash_duo.wait_for_element("#nav-event", timeout=4)
    # Click on the navlink
    dash_duo.driver.find_element(By.ID, "nav-event").click()
    # Delay just so I can visually check the page is loaded, this isn't necessary!
    time.sleep(1)

    # Check the page H1 include the words "event details"
    dash_duo.wait_for_element("H1", timeout=4)
    h1_text = dash_duo.driver.find_element(By.TAG_NAME, "H1").text
    assert h1_text.lower() == "event details"