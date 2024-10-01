const int TV = 10;  // LED connected to digital pin 13 (TV)
const int LED = 8;  // LED connected to digital pin 7 (additional LED)
const int door = 2; // Door connected to digital pin 8 (change to another pin)

void setup() {
  pinMode(TV, OUTPUT);   // Initialize the TV LED pin as an output
  pinMode(LED, OUTPUT);   // Initialize the additional LED pin as an output
  pinMode(door, OUTPUT);  // Initialize the door pin as an output

  Serial.begin(9600);       // Initialize serial communication at 9600 baud
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');  // Read the command from serial
    command.trim();                                 // Remove leading and trailing whitespaces

    if (command == "1") {
      digitalWrite(TV, HIGH);  // Turn on the TV LED
    } else if (command == "2") {
      digitalWrite(TV, LOW);   // Turn off the TV LED
    } else if (command == "3") {
      digitalWrite(door, HIGH);  // Open the door
    } else if (command == "4") {
      digitalWrite(door, LOW);   // Close the door
    } else if (command == "5") {
      digitalWrite(LED, HIGH);   // Turn on the additional LED
    } else if (command == "6") {
      digitalWrite(LED, LOW);    // Turn off the additional LED
    }
  }
}
