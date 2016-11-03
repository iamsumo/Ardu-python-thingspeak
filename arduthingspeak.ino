int a;
void setup() {
  Serial.begin(1200);  

}

void loop() {
a=analogRead(0);
delay(100);
Serial.println(a);
delay(100);
}
