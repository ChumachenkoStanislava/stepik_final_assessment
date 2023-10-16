from selenium.webdriver.chrome.options import Options
import pytest
from core.utils import get_chrome


def pytest_adoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = get_chrome(options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

