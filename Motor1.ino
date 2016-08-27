void setup() {
  // put your setup code here, to run once:
 pinMode(9,OUTPUT);//Forward R
 pinMode(8,OUTPUT);//Backward R
 pinMode(7,OUTPUT);// Modulation R
 pinMode(6,OUTPUT);//Forward L
 pinMode(5,OUTPUT);//Backward L
 pinMode(4,OUTPUT);// Modulation L
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(9,HIGH);
  digitalWrite(8,LOW);
  digitalWrite(7,00);
  delay(1000);
  // R Forward
  digitalWrite(9,LOW);
  digitalWrite(8,HIGH);
  digitalWrite(7,00);
  delay(1000);
  // R Backward
}
