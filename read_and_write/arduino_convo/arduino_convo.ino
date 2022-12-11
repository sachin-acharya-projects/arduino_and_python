String incoming_data;

void setup() {
  // Initializing Serial Port
  Serial.begin(115200);
}

void loop() {
  Serial.println("Reading Data from Client(Python)");
  while (true) {
    if(Serial.available() > 0) break;
  }
  // Reading Data from Client (Python)
  incoming_data = Serial.readString();
  if (strcmp(incoming_data.c_str(), "Sachin Acharya") == 10) {
    Serial.println(String("Hello, Mr. ") + incoming_data);
  }
}
