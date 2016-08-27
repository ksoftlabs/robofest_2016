#include <Stepper.h>
//in1-11, in2-9,in3-10,in4-8
Stepper motor1(2048,8,9,10,11);
Stepper motor2(2048,4,5,6,7);
int incomingByte =0 ;
void setup() {
  // put your setup code here, to run once:
  motor1.setSpeed(7);
  motor2.setSpeed(7);
  Serial.begin(9600);


}

void loop() {
  // put your main code here, to run repeatedly:
  incomingByte =Serial.read();
  if ( incomingByte>10){
    motor1.step(2048);
    delay(800);
    motor2.step(2048);
    delay(800);
    motor1.step(-2048);
    delay(800);
    
    
  }
  
}
