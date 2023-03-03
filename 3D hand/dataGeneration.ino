// C++ code
//
byte counter=0;
byte sampling_rate=100;
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  
  Serial.println(analogRead(A0));
  delay(10);
  counter++;
  if(counter>=sampling_rate){
    //Serial.println("Please Enter");
    //if(Serial.available())
      while(Serial.read()!='1');
    counter=0;
  }
}
