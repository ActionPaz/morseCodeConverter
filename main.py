# A text-based Python program to convert Strings into Morse Code.
import sys
import time
import wave
import pyaudio

morse_code = {"A": ". _   ", "B": "_ . . .   ", "C": "_ . _ .   ", "D": "_ . .   ", "E": ".   ", "F": ". . _ .   ",
              "G": "_ _ .   ", "H": ". . . .   ", "I": ". .   ", "J": ". _ _ _   ", "K": "_ . _   ", "L": ". _ . .   ",
              "M": "_ _   ", "N": "_ .   ", "O": "_ _ _   ", "P": ". _ _ .   ", "Q": "_ _ . _   ", "R": ". _ .   ",
              "S": ". . .   ", "T": "_   ", "U": ". . _   ", "V": ". . . _   ", "W": ". _ _   ", "X": "_ . . _   ",
              "Y": "_ . _ _   ", "Z": "_ _ . .   ", "1": ". _ _ _ _   ", "2": ". . _ _ _   ", "3": ". . . _ _   ",
              "4": ". . . . _   ", "5": ". . . . .   ", "6": "_ . . . .   ", "7": "_ _ . . .   ", "8": "_ _ _ . .   ",
              "9": "_ _ _ _ .   ", "0": "_ _ _ _ _   ", " ": "    "}


CHUNK = 1024


def play_dash():
    with wave.open("dash.wav", "rb") as wf:

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                        rate=wf.getframerate(), output=True)

        while len(data := wf.readframes(CHUNK)):
            stream.write(data)

        stream.close()
        p.terminate()


def play_dot():
    with wave.open("dot.wav", "rb") as wf:

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                        rate=wf.getframerate(), output=True)

        while len(data := wf.readframes(CHUNK)):
            stream.write(data)

        stream.close()
        p.terminate()


while True:
    user_input = input("Enter your message or type '/exit' to exit program: ").upper()

    coded_message = ""

    if user_input == "/EXIT":
        sys.exit()
    else:
        for letter in user_input:
            if letter in morse_code:
                coded_message += morse_code[letter]
            else:
                print(
                    "Only international letters and numbers are included in the Morse Code. Please alter your message."
                    "\n")

    print(f"Code: {coded_message}\n")

    for symbol in coded_message:
        if symbol == ".":
            play_dot()
        elif symbol == "_":
            play_dash()
        else:
            time.sleep(0.06)


