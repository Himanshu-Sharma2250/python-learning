import threading
import requests
import time

def download(url):
    print(f"Starts downloading image from {url}")
    res = requests.get(url=url)
    print(f"Finished downloading from {url}. Size: {len(res.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/svg",
    "https://httpbin.org/image/png",
]

threads = []
start = time.time()

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"Total time taken to download the images is {end - start:.2f} seconds")