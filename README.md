# 🚦 Smart Traffic Monitoring System

A real-time IoT traffic monitoring system using an **ESP32 microcontroller** as the client and a **Python UDP server** for centralized data aggregation, congestion detection, and performance analysis.

---

## 📌 Overview

This project simulates a smart intersection management system where an ESP32 continuously sends vehicle count data for four lanes (NORTH, SOUTH, EAST, WEST) over UDP to a Python server. The server processes this data in real time to detect congestion, identify overloaded intersections, and measure packet throughput.

---

## 🗂️ Project Structure

```
smart-traffic-monitor/
│
├── client/
│   └── esp32_client.ino        # ESP32 Arduino sketch (UDP sender)
│
├── server/
│   └── traffic_server.py       # Python UDP server (aggregator + analyzer)
│
└── README.md
```

---

## ⚙️ How It Works

```
[ ESP32 Client ]
     │
     │  UDP Packets → "Lane=NORTH,Vehicles=24"
     ▼
[ Python UDP Server ]
     ├── Central Aggregation   → Tracks vehicle count per lane
     ├── Congestion Detection  → Flags lanes with count > 20 for 3+ consecutive readings
     ├── Intersection Analysis → Identifies the most congested lane across all 4
     └── Performance Metrics  → Reports packet throughput every second
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Microcontroller | ESP32 (Arduino Framework) |
| Communication Protocol | UDP (User Datagram Protocol) |
| Server Language | Python 3 |
| Network | Wi-Fi (2.4 GHz) |

---

## 🚀 Getting Started

### Prerequisites

- **Arduino IDE** with ESP32 board support installed
- **Python 3.x** installed on your machine
- Both devices on the **same Wi-Fi network**

---

### 1. Client Setup (ESP32)

1. Open `client/esp32_client.ino` in Arduino IDE.
2. Update the following fields with your network credentials and server IP:

```cpp
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
const char* udpAddress = "YOUR_SERVER_IP";  // e.g., 192.168.1.100
const int udpPort = 5005;
```

3. Flash the sketch to your ESP32.
4. Open the Serial Monitor at **115200 baud** to verify connection.

---

### 2. Server Setup (Python)

1. Navigate to the `server/` directory.
2. No external dependencies required — uses Python's built-in `socket` library.
3. Run the server:

```bash
python traffic_server.py
```

4. The server will begin listening on port `5005` and printing real-time traffic analysis.

---

## 📡 UDP Packet Format

Packets are plain text strings sent from the ESP32 in the following format:

```
Lane=NORTH,Vehicles=24
Lane=SOUTH,Vehicles=7
Lane=EAST,Vehicles=19
Lane=WEST,Vehicles=30
```

---

## 📊 Server Output Example

```
Server listening on port 5005...

From ('10.202.131.109', 5005): Lane=NORTH,Vehicles=25
Traffic State: {'NORTH': 25}

From ('10.202.131.109', 5005): Lane=SOUTH,Vehicles=22
Traffic State: {'NORTH': 25, 'SOUTH': 22}
🚨 CONGESTION at SOUTH

From ('10.202.131.109', 5005): Lane=EAST,Vehicles=18
From ('10.202.131.109', 5005): Lane=WEST,Vehicles=28
Total Vehicles: 93
Most Congested Lane: WEST
🚨 INTERSECTION OVERLOAD

📊 Throughput: 20 packets/sec
```

---

## 🔍 Features

- **Real-time UDP Communication** between ESP32 and Python server
- **Congestion Detection** — triggers alert after 3 consecutive high-count readings per lane
- **Intersection Overload Alert** — fires when total vehicles across all lanes exceed 80
- **Live Throughput Monitoring** — calculates and displays packets per second
- **High-Stress Simulation** — ESP32 sends data every 200ms for rapid testing

---

## 📝 Configuration Reference

| Parameter | Default | Description |
|-----------|---------|-------------|
| `udpPort` | `5005` | UDP port for communication |
| `delay()` | `200ms` | Packet send interval on ESP32 |
| Congestion threshold | `> 20 vehicles` | Per-lane congestion trigger |
| Congestion persistence | `3 readings` | Consecutive readings before alert |
| Overload threshold | `> 80 vehicles` | Total intersection vehicle count |

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
