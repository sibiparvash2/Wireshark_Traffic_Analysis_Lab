import socket
import threading
import time

TARGET_IP = "192.168.x.x"
TARGET_PORT = 80
REQUESTS_PER_THREAD = 100
THREADS = 10

def send_requests(thread_id):
    for i in range(REQUESTS_PER_THREAD):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            request = b"GET / HTTP/1.1\r\nHost: test\r\nConnection: close\r\n\r\n"
            s.send(request)
            s.close()   
except:
            pass
    print(f"Thread {thread_id} finished")

threads = []

print("Starting traffic simulation...")
start = time.time()

for i in range(THREADS):
    t = threading.Thread(target=send_requests, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print("Traffic simulation complete")
print("Total Requests Sent:", THREADS * REQUESTS_PER_THREAD)
print("Duration:", round(end - start, 2), "seconds")
