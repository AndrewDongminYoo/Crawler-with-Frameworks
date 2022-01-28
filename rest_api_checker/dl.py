import datetime
import os
import time
from mimetypes import guess_extension
from urllib.parse import urlparse

from seleniumwire import webdriver  # Import from seleniumwire


def download_assets(requests,
                    asset_dir="temp",
                    default_fname="unnamed",
                    skip_domains=["facebook", "google", "yahoo", "agkn", "2mdn"],
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
            # Don't know the file extention, or not in the whitelist
            continue
        parsed_url = urlparse(request.url)

        skip = False
        for d in skip_domains:
            if d in parsed_url.netloc:
                skip = True
                break
        if skip:
            continue

        frelpath = parsed_url.path.strip()
        if frelpath == "":
            timestamp = str(datetime.datetime.now().replace(microsecond=0).isoformat())
            frelpath = f"{default_fname}_{req_idx}_{timestamp}{ext}"
        elif frelpath.endswith("\\") or frelpath.endswith("/"):
            timestamp = str(datetime.datetime.now().replace(microsecond=0).isoformat())
            frelpath = frelpath + f"{default_fname}_{req_idx}_{timestamp}{ext}"
        elif append_ext and not frelpath.endswith(ext):
            frelpath = frelpath + f"_{default_fname}{ext}"  # Missing file extension but may not be a problem
        if frelpath.startswith("\\") or frelpath.startswith("/"):
            frelpath = frelpath[1:]

        fpath = os.path.join(asset_dir, parsed_url.netloc, frelpath)
        if os.path.isfile(fpath):
            continue
        os.makedirs(os.path.dirname(fpath), exist_ok=True)
        print(f"Downloading {request.url} to {fpath}")
        asset_list[fpath] = request.url
        try:
            with open(fpath, "wb") as file:
                file.write(request.response.body)
        except:
            print(f"Cannot download {request.url} to {fpath}")
    return asset_list


# Create a new instance of the Chrome/Firefox driver
driver = webdriver.Chrome()

# Go to the Google home page
driver.get('https://www.chewy.com/b/dry-food-388')

# Download content to temp folder
asset_dir = "static"

while True:
    # Please browser the internet, it will collect the images for every second
    time.sleep(1)
    download_assets(driver.requests, asset_dir=asset_dir)

driver.close()
