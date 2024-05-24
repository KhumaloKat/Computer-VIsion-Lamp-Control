#include <cvzone.h>

SerialData serialData(1,3);
int valsRec[1];

void setup() {
  serialData.begin();
    pinMode(8,OUTPUT);
    pinMode(9,OUTPUT);    
    pinMode(10,OUTPUT);    

    digitalWrite(8,1);
    digitalWrite(9,0);
}

void loop() {
  serialData.Get(valsRec);
  analogWrite(10,valsRec[0]);

}  
