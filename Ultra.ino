#include <Stepper.h>
#define ECHOPIN 3 // echo pin to pin 3
#define TRIGPIN 2 // echo pin to pin 2
//in1-11, in2-9,in3-10,in4-8
Stepper motor1(2048,8,9,10,11);
Stepper motor2(2048,4,5,6,7);
//in1-7 in2-5, in3-6 in4-4
int incomingByte =0 ;
void setup() {
  // put your setup code here, to run once:
  motor1.setSpeed(7);
  motor2.setSpeed(7);
  Serial.begin(9600);
  pinMode(ECHOPIN, INPUT);
  pinMode(TRIGPIN,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  incomingByte =Serial.read();
  digitalWrite(TRIGPIN, LOW);
  delayMicroseconds(1000);
  digitalWrite(TRIGPIN, HIGH);
  delayMicroseconds(1000);
  digitalWrite(TRIGPIN, LOW);
  
  float distance = pulseIn(ECHOPIN,HIGH);
  distance = distance/58;
  Serial.println(distance);
  
  if ( distance<5){
    motor1.step(20);
    
    
    
    
  }
  
}
