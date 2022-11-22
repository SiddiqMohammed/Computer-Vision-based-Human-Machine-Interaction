// Run main.py from powershell [admin]

String serialData;
String rString;
int receivedChar;
boolean newData = false;

int ledPin = 11;

void setup() {
  // initialize digital pins as an outputs.
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  Serial.println("<Arduino is ready>");
}

void loop() {
  delay(10);

  while (Serial.available()) {
    char c = Serial.read();  //gets one byte from serial buffer
    rString += c; //makes the String readString
    delay(2);  //slow looping to allow buffer to fill with next character
  }

  if (rString.length() > 0) {
    Serial.println(rString);  //so you can see the captured String
    ledCode();
    Serial.write("E");
    rString = "";
  }
}

void ledCode() {
  //Relay stuff
  int xxx = rString.toInt();
  if (xxx >= 255) {
    xxx = 255;
  }
  if (xxx <= 0) {
    xxx = 0;
  }
  analogWrite(ledPin, xxx);
}
