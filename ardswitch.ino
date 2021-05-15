int ser_value =1; //value frrom serial port. initial value is 1.
void setup() {
  pinMode(12,OUTPUT); //relay pin
  Serial.begin(9600);
  digitalWrite(12,HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
     ser_value = Serial.read();
  }
    if (ser_value=='0')
    digitalWrite(12,HIGH);
    if(ser_value=='1')
    digitalWrite(12,LOW);
  

}
