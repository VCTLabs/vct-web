Embedded-board Serial Console Cheatsheet
########################################

:date: 2015-12-24
:tags: embedded, BeagleBone, BBB, MinnowBoard, OLinuXino, Raspberry Pi, RPi
:category: cheatsheets
:slug: serial_console_cheatsheet
:author: Stephanie Lockwood-Childs
:summary: cheatsheet for hooking serial cables to popular embedded boards

Conventions
-------------------

* TX/RX is labeled from perspective of development host (opposite of target board), thus called "host TX" and "host RX"
* unless otherwise noted, software serial configuration is 15200 baud, 8N1, no flow control

Adafruit USB-Serial Cable
-------------------------

Adafruit PL2303 3.3V serial cable
https://www.adafruit.com/product/954

* GND      BLACK
* host TX  GREEN 
* host RX  WHITE 

Minnowboard Max
---------------

Serial port is single-row right-angle 6-pin connector J4

Schematic: http://wiki.minnowboard.org/images/6/6d/MinnowBoard_Max_RevA2_sch.pdf

Numbering below starts from the left while holding board with serial port
along top edge, so Pin 1 is closest to SATA connector

http://wiki.minnowboard.org/MinnowBoard_MAX#4-Wire_Serial_Console

=====  =======  ==============
Pin #  Role     Adafruit color
-----  -------  --------------
Pin 1  GND      BLACK 
Pin 4  host TX  GREEN 
Pin 5  host RX  WHITE 
=====  =======  ==============

Note that these are not consecutive: pins 2, 3, and 6 should be empty. 
This is standard arrangement for boards compatible with an FTDI serial cable.

Beaglebone Black
----------------

Serial port is single-row 6-pin connector J1 running along the inner side of
one of the expansion sockets for "cape" daughtercards

Schematic: https://github.com/CircuitCo/BeagleBone-Black/blob/master/BBB_SCH.pdf?raw=true

Numbering starts from the left while holding board with the serial port
towards the bottom, so Pin 1 is the one closest to 5V power connector

http://dave.cheney.net/2013/09/22/two-point-five-ways-to-access-the-serial-console-on-your-beaglebone-black note text accompanying picture uses TX/RX from target perspective

=====  =======  ==============
Pin #  Role     Adafruit color
-----  -------  --------------
Pin 1  GND      BLACK 
Pin 4  host TX  GREEN 
Pin 5  host RX  WHITE 
=====  =======  ==============

Note that these are not consecutive: pins 2, 3, and 6 should be empty.
This is standard arrangement for boards compatible with an FTDI serial cable.

Raspberry Pi
------------

Serial port is on double-row 26-pin connector J8

https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/README.md (these are only partial schematics, and nothing posted yet for RPi 2, but GPIO header is same as RPi B+)

Numbering below starts from top-row left while holding board with
serial port along top edge, so Pin 1 is at top-left corner of board (note
this is NOT the same as connector pin numbering on diagrams or board silkscreen,
which is an inconvenient arrangement for this purpose)

http://elinux.org/RPi_Serial_Connection

=====  =======  ==============
Pin #  Role     Adafruit color
-----  -------  --------------
Pin 3  GND      BLACK 
Pin 4  host RX  WHITE 
Pin 5  host TX  GREEN 
=====  =======  ==============

Note that these are consecutive, but the first 2 pins are skipped and the
RX/TX order is opposite of boards that are compatible with FTDI serial cables,
e.g. Minnowboard or BBB

iMX233 OLinuXino Maxi/Mini
--------------------------

Serial port is single-row 4-pin connector U_DEBUG

Schematic: https://github.com/OLIMEX/OLINUXINO/tree/master/HARDWARE

Numbering below starts from the left while holding board with reset and
power switches along top edge, so Pin 1 is closest to board edge

=====  =======  ==============
Pin #  Role     Adafruit color
-----  -------  --------------
Pin 1  host TX  WHITE
Pin 2  host RX  GREEN
Pin 3  GND      BLACK
=====  =======  ==============

Note that these are consecutive, but pin order is different from boards 
that are compatible with FTDI serial cables, e.g. Minnowboard or BBB
