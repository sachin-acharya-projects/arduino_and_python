String a, b, c, d, e, f, g, h, i, j, k, l;

void printData(int p[]) {
  String db;
  for(int i = 0; i < 12;i++) {
    if (i != 0) {
      db += ","+String(p[i]);
    }else {
      db += String(p[i]);
    }
  }

  Serial.println(db);
}

void init() {
  Serial.begin(9600);
  Serial.println("title_one,title_two,title_3,title_4,title_5,title_6,title_7,title_8,title_9,title_10,title_11,title_12");
}

void loop() {
  int data[12] = {
    rand(0, 100), 
    rand(0, 100),
    rand(0, 100),
    rand(0, 100),
    rand(0, 100),
    rand(0, 100),
    rand(0, 100),
    rand(0, 100),
    rand(0, 100),
    rand(0, 100),
    rand(0, 100),
    rand(0, 100)
  } 
  printData(data);
  delay(400);
}