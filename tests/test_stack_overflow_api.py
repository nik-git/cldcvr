"""
pytest test_stack_overflow_api.py --html="../output/report.html" --self-contained-html --log-level INFO
"""

import pytest
import requests
import logging

log = logging.getLogger(__name__)
BADGES_PARAMS = {"order": "desc", "sort": "rank", "site": "stackoverflow"}
BADGES_URL = "https://api.stackexchange.com/2.2/users/5049903/badges"
BADGE_ID_URL = "https://api.stackexchange.com/2.2/badges/{}"
BADGE_ID_NAME_DICT = {1:'Teacher'}

@pytest.mark.P1
def test_badge_api():
    session = requests.Session()
    response = session.get(BADGES_URL, params=BADGES_PARAMS)
    badges_dict = response.json()
    log.info(badges_dict['items'][0]['user']['user_id'])
    assert 5049903 == badges_dict['items'][0]['user']['user_id']

@pytest.mark.P1
def test_badge_teacher():
    url = BADGE_ID_URL.format(1)
    session = requests.Session()
    response = session.get(url, params=BADGES_PARAMS)
    items_dict = response.json()
    log.info(items_dict)
    assert BADGE_ID_NAME_DICT[1] == items_dict['items'][0]['name']

@pytest.mark.P1
def test_badge_recipients():
    url = "https://api.stackexchange.com/2.2/badges/recipients"
    session = requests.Session()
    response = session.get(url, params=BADGES_PARAMS)
    items_dict = response.json()
    log.info(items_dict)


