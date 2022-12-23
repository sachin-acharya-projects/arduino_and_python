int red_data_pin = 11;
int green_data_pin = 10;
int blue_data_pin = 9;
// String reading_data;
String rv, gv, bv;
int red_v, green_v, blue_v;

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
    String read_data = Serial.readString();
    rv = read_data.substring(0, 3);
    gv = read_data.substring(4, 7);
    bv = read_data.substring(8, 11);

    Serial.println(rv + " " + gv + " " + bv);
    red_v = rv.toInt();
    green_v = gv.toInt();
    blue_v = bv.toInt();

    color_rgb(blue_v, red_v, green_v); // BLUE RED GREEN
    // color_rgb(red_v, green_v, blue_v); // Green
  }
}

void color_rgb(int red, int green, int blue) {
  analogWrite(red_data_pin, red);
  analogWrite(green_data_pin, green);
  analogWrite(blue_data_pin, blue);
}