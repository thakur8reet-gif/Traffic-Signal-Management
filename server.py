import socket
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print("Server listening on port 5005...")

traffic_data = {}
congestion_counter = {}
packet_count = 0
start_time = time.time()

while True:
    data, addr = sock.recvfrom(1024)
    msg = data.decode()
    packet_count += 1
    print(f"\nFrom {addr}: {msg}")

    if "Lane=" in msg:
        lane = msg.split(",")[0].split("=")[1]
        count = int(msg.split("=")[2])

        traffic_data[lane] = count
        print("Traffic State:", traffic_data)

        if lane not in congestion_counter:
            congestion_counter[lane] = 0

        if count > 20:
            congestion_counter[lane] += 1
        else:
            congestion_counter[lane] = 0

        if congestion_counter[lane] >= 3:
            print(f"🚨 CONGESTION at {lane}")

        if len(traffic_data) == 4:
            total = sum(traffic_data.values())
            max_lane = max(traffic_data, key=traffic_data.get)
            print(f"Total Vehicles: {total}")
            print(f"Most Congested Lane: {max_lane}")
            if total > 80:
                print("🚨 INTERSECTION OVERLOAD")

    current_time = time.time()
    if current_time - start_time >= 1:
        print(f"\n📊 Throughput: {packet_count} packets/sec")
        packet_count = 0
        start_time = current_time