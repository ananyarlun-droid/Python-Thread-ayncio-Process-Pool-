import threading
import time

def download_file(name, sec):
    print(f"Start download {name}")
    time.sleep(sec)
    print(f"Finish download {name}")

files = [
    ("fileA", 2),
    ("fileB", 3),
    ("fileC", 1),
]

threads = []

for name, sec in files:
    t = threading.Thread(target=download_file, args=(name, sec))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All downloads completed")
