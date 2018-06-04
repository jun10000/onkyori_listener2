[onkyori_common]: https://github.com/jun10000/onkyori_common

# onkyori_listener2
onkyori_*** are modules what enable cooperation with the Onkyo RI system.

Now, I'm creating this.

<!--
## Description
The onkyori_listener is the daemon what acquires Onkyo RI signal and registers it to database.  
This daemon needs [onkyori_common] module to operate.

## Requirement
- Requirements of [onkyori_common]
- Raspberry Pi 3 Type B
    - Physical parts:
        - Resistance
            - 2kΩ x1
            - 1kΩ x1
        - Audio cable (3.5mm Mono)
    - Python packages:
        - Cython 0.28.1

## Install
1. Create electronic circuit  
    ![Electronic curcuit diagram](.readme/circuit.svg)
    - The Onkyo RI equipment's "RI Remote Control" jack uses the audio cable plug.
    - Connect the Onkyo RI equipment ground and the Raspberry Pi ground.
1. Place this repository files into Raspberry Pi
    1. Login to Raspberry Pi.
    1. Create directory: '/var/project/onkyori_listener/'
    1. Place this repository files to '/var/project/onkyori_listener/'.
    1. Add execute permission to 'index.py' and 'cython_setup.py'.
1. Compile Cython scripts
    1. Move to '/var/project/onkyori_listener/'.
    1. Execute the following command to compile Cython scripts.  
       `python3 cython_setup.py build_ext --inplace`
1. Install systemctl service
    1. Move 'onkyori_listener.service' to '/usr/lib/systemd/system/'.
    1. Execute the following command to reload daemons.  
       `sudo systemctl daemon-reload`
    1. Execute the following command to start this service.  
       `sudo systemctl start onkyori_listener`
    1. Execute the following command to set this service starting automatically.  
       `sudo systemctl enable onkyori_listener`

## Licence
[GNU General Public License v3.0](https://github.com/jun10000/onkyori_listener/blob/master/LICENSE)

## Author
[jun10000](https://github.com/jun10000)
-->