const int sensorVaga1 = 22; //PINO DIGITAL UTILIZADO PELO SENSOR
const int sensorVaga2 = 24;
const int sensorVaga3 = 26;
const int sensorVaga4 = 28;
const int sensorVaga5 = 30;
const int sensorVaga6 = 32;
const int sensorVaga7 = 34;
const int sensorVaga8 = 38;
const int sensorVaga9 = 40;
const int sensorVaga10 = 42;
String dados[9];// variavel que enviara os dados para o Python
String estado1 = "livre";
String estado2 = "livre";
String estado3 = "livre";
String estado4 = "livre";
String estado5 = "livre";
String estado6 = "livre";
String estado7 = "livre";
String estado8 = "livre";
String estado9 = "livre";
String estado10 = "livre";
void setup() {
  pinMode(sensorVaga1, INPUT); //DEFINE O PINO COMO ENTRADA
  pinMode(sensorVaga2, INPUT);
  pinMode(sensorVaga3, INPUT);
  pinMode(sensorVaga4, INPUT);
  pinMode(sensorVaga5, INPUT);
  pinMode(sensorVaga6, INPUT);
  pinMode(sensorVaga7, INPUT);
  pinMode(sensorVaga8, INPUT);
  pinMode(sensorVaga9, INPUT);
  pinMode(sensorVaga10, INPUT);
  //delay(9000);//espera o sensor ligar
  Serial.begin(9600);
}
void loop(){
  if (digitalRead(sensorVaga1) == LOW && estado1 != "ocupada") {//SE A LEITURA DO PINO FOR IGUAL A LOW, FAZ
    estado1 = "ocupada";
    dados[0] = "1 ocupada";
    Serial.println("1 ocupada");
    //delay(1000);
  } else if (digitalRead(sensorVaga1) == HIGH && estado1 != "livre") {//SENÃO, FAZ
    estado1 = "livre";
    dados[0] = "1 livre";
    Serial.println(dados[0]);
    //delay(1000);
  }if (digitalRead(sensorVaga2) == LOW && estado2 != "ocupada") {//IF VAGA 2
    estado2 = "ocupada";
    dados[1] = "2 ocupada";
    Serial.println(dados[1]);
    //delay(1000);
  }else if (digitalRead(sensorVaga2) == HIGH && estado2 != "livre") {//SENÃO, FAZ
    estado2 = "livre";
    dados[1] = "2 livre";
    Serial.println(dados[1]);
    //delay(1000);
  }if (digitalRead(sensorVaga3) == LOW && estado3 != "ocupada") {//IF VAGA 3
    estado3 = "ocupada";
    dados[2] = "3 ocupada";
    Serial.println(dados[2]);
   // delay(1000);
  }else if (digitalRead(sensorVaga3) == HIGH && estado3 != "livre") { //SENÃO, FAZ
    estado3 = "livre";
    dados[2] = "3 livre";
    Serial.println(dados[2]);
    //delay(1000);
  }if (digitalRead(sensorVaga4) == LOW && estado4 != "ocupada") { //SE A LEITURA DO PINO FOR IGUAL A LOW, FAZ
    estado4 = "ocupada";
    dados[3] = "4 ocupada";
    Serial.println(dados[3]);
    //delay(1000);
  }else if (digitalRead(sensorVaga4) == HIGH && estado4 != "livre") { //SENÃO, FAZ
    estado4 = "livre";
    dados[3] = "4 livre";
    Serial.println(dados[3]);
    //delay(1000);
  }if (digitalRead(sensorVaga5) == LOW && estado5 != "ocupada") {
    estado5 = "ocupada";
    dados[4] = "5 ocupada";
    Serial.println(dados[4]);
    //delay(1000);
  }else if (digitalRead(sensorVaga5) == HIGH && estado5 != "livre") {
    estado5 = "livre";
    dados[4]= "5 livre";
    Serial.println(dados[4]);
    //delay(1000);
  }if(digitalRead(sensorVaga6) == LOW && estado6 != "ocupada") {
    estado6 = "ocupada";
    dados[5] = "6 ocupada";
    Serial.println(dados[5]);
    //delay(1000);
  }else if (digitalRead(sensorVaga6) == HIGH && estado6 != "livre") {
    estado6 = "livre";
    dados[5] = "6 livre";
    Serial.println(dados[5]);
    //delay(1000);
  }if (digitalRead(sensorVaga7) == LOW && estado7 != "ocupada") {
    estado7 = "ocupada";
    dados[6] = "7 ocupada";
    Serial.println(dados[6]);
    //delay(1000);
  }else if (digitalRead(sensorVaga7) == HIGH && estado7 != "livre") {
    estado7 = "livre";
    dados[6] = "7 livre";
    Serial.println(dados[6]);
    //delay(1000);
  }if (digitalRead(sensorVaga8) == LOW && estado8 != "ocupada") {
    estado8 = "ocupada";
    dados[7] = "8 ocupada";
    Serial.println(dados[7]);
    //delay(1000);
  }else if (digitalRead(sensorVaga8) == HIGH && estado8 != "livre") {
    estado8 = "livre";
    dados[7] = "8 livre";
    Serial.println(dados[7]);
    //delay(1000);
  }if (digitalRead(sensorVaga9) == LOW && estado9 != "ocupada") {
    estado9 = "ocupada";
    dados[8] = "9 ocupada";
    Serial.println(dados[8]);
    //delay(1000);
  }else if (digitalRead(sensorVaga9) == HIGH && estado9 != "livre") {
    estado9 = "livre";
    dados[8] = "9 livre";
    Serial.println(dados[8]);
    //delay(1000);
  }////////////////////lembrar de mudar a quantidade de caracteres no python pois o "dados10" tem 1 caractere a mais
  if (digitalRead(sensorVaga10) == LOW && estado10 != "ocupada") {
    estado10 = "ocupada";
    dados[9] = "10 ocupada";
    Serial.println(dados[9]);
    //delay(1000);
  }else if (digitalRead(sensorVaga10) == HIGH && estado10 != "livre") {
    estado10 = "livre";
    dados[9] = "10 livre";
    Serial.println(dados[9]);
    //delay(1000);
  }
}
