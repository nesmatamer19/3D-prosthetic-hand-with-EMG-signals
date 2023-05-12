#include <Servo.h>

Servo myservo1;  // create servo object to control a servo
Servo myservo2;
Servo myservo3;
Servo myservo4;
Servo myservo5;
char reading;
int pos = 0;    // variable to store the servo positio


void setup() {
 Serial.begin(9600);
  myservo1.attach(21); 
  myservo2.attach(22); 
  myservo3.attach(23); 
  myservo4.attach(24); 
  myservo5.attach(25); 
}

void loop() {
  if(Serial.available()>0){
    reading = Serial.read();
    switch(reading){
      case 'C' : Close();break;
      case 'O' : Open();break;
      case 'P' : Point();break;
      case 'H' : Hold();break;
    }
    Serial.println(reading);
  }
}


void Open(){
  pos = 170;
    myservo1.write(pos);
    myservo2.write((pos>150)?150:pos);
    myservo3.write(pos);
    myservo4.write(pos);
    myservo5.write(pos);
}

void Close(){
  pos  = 10;
    myservo1.write(pos);
    myservo2.write((pos<63)?63:pos);
    myservo3.write((pos>150)?150:pos);
    myservo4.write(pos);
    myservo5.write(pos);              // tell servo to go to position in variable 'pos'
}

void Hold(){
  pos = 170;
    myservo1.write(pos);
    myservo2.write((pos>150)?150:pos);
    myservo3.write(pos);
  pos = 8;
    myservo4.write(pos);
    myservo5.write(pos);
}

void Point(){
  pos = 8;
    myservo1.write(pos);
    myservo2.write((pos<63)?63:pos);
    myservo3.write((pos>150)?150:pos);
    myservo4.write(pos);
    myservo5.write(170);              // tell servo to go to position in variable 'pos'
}
