import json
import sys

import eliot
import requests
from eliot import (
    Message,
    start_action,
    to_file,
    write_traceback
)

to_file(sys.stdout)

PAGE_URL_LIST = [
    "https://eliot.readthedocs.io/en/1.0.0",
    "https://eliot.readthedocs.io/en/1.0.0/generating/index.html",
    "https://example.com/notfound.html"
]


def fetch_pages(url_array):
    with start_action(action_type="fetch_pages"):
        page_contents = {}
        for page_url in url_array:
            with start_action(action_type="download", url=page_url):
                try:
                    r = requests.get(page_url, timeout=30)
                    r.raise_for_status()
                except requests.exceptions.RequestException as e:
                    write_traceback()
                    continue
                page_contents[page_url] = r.text
        return page_contents


if __name__ == '__main__':
    page_contents = fetch_pages(PAGE_URL_LIST)
    with open("page_contents.json", 'w') as f_page_contents:
        json.dump(page_contents, f_page_contents, ensure_ascii=False)
    eliot.log_message(message_type="info", msg="데이터를 저장했습니다.")
