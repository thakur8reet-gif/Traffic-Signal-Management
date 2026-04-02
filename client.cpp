#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "<ssid>";
const char* password = "<password>";
const char* udpAddress = "<ip address>";
const int udpPort = 5005;

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  Serial.println("STARTING...");
  WiFi.begin(ssid, password);
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(500);
    Serial.print(".");
    attempts++;
  }
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nConnected!");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("\nWiFi FAILED");
  }
}

void loop() {
  Serial.println("LOOP RUNNING");
  sendLane("NORTH", random(0, 30));
  sendLane("SOUTH", random(0, 30));
  sendLane("EAST",  random(0, 30));
  sendLane("WEST",  random(0, 30));
  delay(200);
}

void sendLane(String lane, int count) {
  String msg = "Lane=" + lane + ",Vehicles=" + String(count);
  udp.beginPacket(udpAddress, udpPort);
  udp.print(msg);
  udp.endPacket();
  Serial.println(msg);
}
