[onkyori_common]: https://github.com/jun10000/onkyori_common

# onkyori_listener2
onkyori_*** are modules what enable cooperation with the Onkyo RI system.

## Description
'Onkyori_listener2' acquires Onkyo RI signal and registers it to database.  
This module contains the Raspberry Pi daemon and the Arduino program.  
This module needs [onkyori_common] module (Ver. 0.4 or above) to operate.

## Requirement
- Requirements of [onkyori_common]
- Physical Products and Parts
    - Arduino Uno R3
    - USB 2.0 Cable Type A to B
    - Audio Cable (3.5mm Mono)
- Arduino IDE
- Python Packages:
    - PySerial 3.4

## Install
1. Connect the Onkyo RI equipment and the Arduino
    1. Use the audio cable.
    1. Plug the cable plug to the Onkyo RI equipments "RI Remote Control" jack.
    1. Connect another plug's line to the Arduino.  
       (audio) Ground <-> GND (Arduino)  
       (audio) Signal <-> PIN_2 \[Default\] (Arduino)
1. Setup the Arduino
    1. Load 'Arduino/acquire_ri/acquire_ri.ino' using the Arduino IDE.
    1. Compile the source and upload the program to the Arduino.
    1. Operate the Onkyo RI equipment to confirm the receive data.  
       If the Arduino cannot receive the data normally, you can edit the constant values in the Arduino source code.
1. Connect the Arduino Uno and the Raspberry Pi 3 via USB Cable.
1. Place this repository files into Raspberry Pi
    1. Login to Raspberry Pi.
    1. Create directory: '/var/project/onkyori_listener2/'
    1. Place this repository files to '/var/project/onkyori_listener2/'.
    1. Add execute permission to 'index.py'.
1. Install systemctl service
    1. Move 'onkyori_listener2.service' to '/usr/lib/systemd/system/'.
    1. Execute the following command to reload daemons.  
       `sudo systemctl daemon-reload`
    1. Execute the following command to start this service.  
       `sudo systemctl start onkyori_listener2`
    1. Execute the following command to set this service starting automatically.  
       `sudo systemctl enable onkyori_listener2`

## Licence
[GNU General Public License v3.0](https://github.com/jun10000/onkyori_listener2/blob/master/LICENSE)

## Author
[jun10000](https://github.com/jun10000)
