from urllib.parse import urljoin
from collections import deque
from datetime import date
from requests import get
from lxml import html


TARGET_URL = "http://52.136.215.164/broken-links/"
BASE_URL = "http://52.136.215.164/"


def is_good_response(response):
    try:
        response.raise_for_status()
    except:
        return False
    return True


def get_filtered_urls(content):
    try:
        return [urljoin(TARGET_URL, href) for href in html.fromstring(content).xpath("//a/@href")]
    except:
        return []


def get_hrefs(url):
    response = get(url)
    return response.status_code, is_good_response(response), get_filtered_urls(response.content)


def print_report(report):
    with open("good.txt", "w") as good, open("bad.txt", "w") as bad:
        counter = {
            good.name: 0,
            bad.name: 0,
        }
        for url, status in report.items():
            status_code, is_good = status
            f = good if is_good else bad
            counter[f.name] += 1
            f.write(f"{url} [{status_code}]\n")

        today = date.today()
        good.write(f"\nTotal: {counter[good.name]} Date: {today.strftime('%d/%m/%Y')}\n")
        bad.write(f"\nTotal: {counter[bad.name]} Date: {today.strftime('%d/%m/%Y')}\n")


def make_report():
    status, is_good, hrefs = get_hrefs(TARGET_URL)

    processed_urls = {TARGET_URL}
    queue = deque(list(set([href for href in hrefs if BASE_URL in href])))

    report = {}
    while queue:
        url = queue.popleft()
        if url[:7] == "mailto:" or url[:4] == "tel:":
            continue
        if url in processed_urls:
            continue
        status, is_good, urls = get_hrefs(url)
        processed_urls.add(url)
        report[url] = status, is_good
        if BASE_URL in url:
            queue.extend(list(set(urls)))
    return report


def main():
    print_report(make_report())


if __name__ == "__main__":
    main()
