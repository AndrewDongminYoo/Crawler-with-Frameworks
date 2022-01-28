import datetime
import os
import time
from mimetypes import guess_extension
from urllib.parse import urlparse

from seleniumwire import webdriver


def download_assets(requests,
                    asset_dir="temp",
                    default_fname="unnamed",
                    skip_domains=["facebook", "google", "yahoo", "agkn", "2mdn", "github", "bing", "micpn", "cdn"],
                    exts=[".png", ".jpeg", ".jpg", ".svg", ".gif", ".pdf", ".bmp", ".webp", ".ico"],
                    append_ext=False):
    asset_list = {}
    for req_idx, request in enumerate(requests):
        # request.headers
        # request.response.body is the raw response body in bytes
        if request is None or request.response is None or request.response.headers is None or 'Content-Type' not in request.response.headers:
            continue

        ext = guess_extension(request.response.headers['Content-Type'].split(';')[0].strip())
        if ext is None or ext == "" or ext not in exts:
            # Don't know the file extension, or not in the whitelist
            continue
        parsed_url = urlparse(request.url)

        skip = False
        for d in skip_domains:
            if d in parsed_url.netloc:
                skip = True
                break
        if skip:
            continue

        file_rel_path = parsed_url.path.strip()
        if file_rel_path == "":
            timestamp = str(datetime.datetime.now().replace(microsecond=0).isoformat())
            file_rel_path = f"{default_fname}_{req_idx}_{timestamp}{ext}"
        elif file_rel_path.endswith("\\") or file_rel_path.endswith("/"):
            timestamp = str(datetime.datetime.now().replace(microsecond=0).isoformat())
            file_rel_path = file_rel_path + f"{default_fname}_{req_idx}_{timestamp}{ext}"
        elif append_ext and not file_rel_path.endswith(ext):
            file_rel_path = file_rel_path + f"_{default_fname}{ext}"  # Missing file extension but may not be a problem
        if file_rel_path.startswith("\\") or file_rel_path.startswith("/"):
            file_rel_path = file_rel_path[1:]

        file_path = os.path.join(asset_dir, parsed_url.netloc, file_rel_path)
        if os.path.isfile(file_path):
            continue
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        print(f"Downloading {request.url} to {file_path}")
        asset_list[file_path] = request.url
        try:
            with open(file_path, "wb") as file:
                file.write(request.response.body)
        except:
            print(f"Cannot download {request.url} to {file_path}")
    return asset_list


# Create a new instance of the Chrome/Firefox driver
driver = webdriver.Chrome()

# Go to the page
driver.get('https://www.chewy.com/b/dry-food-388')

# Download content to temp folder
asset_dir = "static"

# Please browser the internet, it will collect the images for every second
while True:
    download_assets(driver.requests, asset_dir=asset_dir, exts=["svg"])
    time.sleep(1)
