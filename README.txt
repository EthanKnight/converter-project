The purpose of this project is for students too see how everyday numbers (Base10) apply to computers.

v1 has 2 conversion files:
  converter.py - converts Base10 to Binary, Hex, and the corresponding ASCII characters
  generator.py - converts a String to the corresponding hex segments, and Base10 for converter.py input

On the student side (converter.py), the program shows:
  Binary - What the Computer uses
  Hex - What the operating system uses
  Ascii - What a human uses

On the educator side (generator.py), the program:
  Takes user input, and converts it to Base10 for student conversion
  Shows corresponding Hex for debug purposes

Pre-install checklist:
  - Python 3.7.x (at location C:\Users\(YOUR_USER)\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7)

To run:
  Linux:
    - Move converter.py and generator.py to /usr/local/bin (disregard _debug files)
    - Open a terminal and change permissions if necessary
    - Execute program
  Windows:
    - Change Path to your Python download location
    - Execute converter.py or generator.py
    - Execute _debug batch files for debugging, holds CMD open to see error

Future version features:
  - GUI
  - Conversion of (any Base number or ASCII) to (any Base number or ASCII)

If you find any bugs or have any feedback, email me at ethantknight@gmail.com. Enjoy!
