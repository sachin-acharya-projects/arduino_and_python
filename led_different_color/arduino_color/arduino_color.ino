int red_data_pin = 11;
int green_data_pin = 10;
int blue_data_pin = 9;
// String reading_data;
long rv, gv, bv;

int * getColorCoordinates(String colorString) {
  static int color[3];
  int index = colorString.indexOf(",");
  return {index};
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(red_data_pin, OUTPUT);
  pinMode(green_data_pin, OUTPUT);
  pinMode(blue_data_pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    rv = Serial.readString().toInt();
    gv = Serial.readString().toInt(); 
    bv = Serial.readString().toInt();

    color_rgb(rv, gv, bv);
  }
}

void color_rgb(long red, long green, long blue) {
  analogWrite(red_data_pin, red);
  analogWrite(green_data_pin, green);
  analogWrite(blue_data_pin, blue);
}