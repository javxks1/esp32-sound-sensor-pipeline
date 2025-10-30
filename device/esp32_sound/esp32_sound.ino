#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Javxks_IoT";
const char* password = "Codmw321";
const char* endpoint = "http://192.168.68.61:5000/ingest";

const int SOUND_PIN = 39; 
int SOUND_BASELINE = 50;

int readSoundAvg() {
  const int N = 32;
  long acc = 0;
  for (int i = 0; i < N; i++) {
    acc += analogRead(SOUND_PIN);
    delay(2);
  }
  return acc / N;
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi OK");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  int soundRaw = readSoundAvg();

  int soundAdj = soundRaw - SOUND_BASELINE;
  if (soundAdj < 0) soundAdj = 0;

  Serial.print("soundRaw=");
  Serial.print(soundRaw);
  Serial.print(" | soundAdj=");
  Serial.println(soundAdj);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(endpoint);
    http.addHeader("Content-Type", "application/json");

    String payload = "{";
    payload += "\"device\":\"esp32-sound\",";
    payload += "\"sound_raw\":" + String(soundRaw) + ",";
    payload += "\"sound_adj\":" + String(soundAdj) + ",";
    payload += "\"ts_ms\":" + String((long)millis());
    payload += "}";

    int code = http.POST(payload);
    Serial.print("HTTP code: ");
    Serial.println(code);
    http.end();
  }

  delay(2000);
}
