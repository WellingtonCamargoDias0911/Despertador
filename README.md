# Pythonic Alarm

This is a simple alarm application developed in Python using the Tkinter library for the graphical interface and the `datetime` function to control the alarm trigger time. The program allows the user to set an hour, minute, and second so that an alarm sound is played when the selected time is reached.

## Features

- Set the alarm time (hour, minute, second).  
- Trigger the alarm by playing an audio file (`Alarm.wav`) when the set time is reached.  
- Simple graphical interface using Tkinter.  

## How It Works

1. The user sets the desired alarm time through three dropdown menus (hour, minute, and second).  
2. After pressing the "Set" button, the program enters an infinite loop checking the current time.  
3. When the system time matches the set alarm time, the alarm is triggered, playing the `Alarm.wav` file.  
4. The program uses `sleep` to wait one second between time checks.  

## How to Use

1. Clone or download this code.  
2. Save an audio file named `Alarm.wav` in the same folder as the script or change the file path in the code.  
3. Run the script. A window will open, allowing you to set the alarm time.  
4. Set the desired hour, minute, and second, then press the "Set" button.  
5. The alarm will trigger when the configured time is reached.  

## Requirements

- Python 3.x  
- `tkinter` library (usually pre-installed with Python).  
- An audio file (`Alarm.wav`) for the alarm sound.  

## How to Run

To run the program, execute the following command in the terminal or command prompt:

```sh
python filename.py
