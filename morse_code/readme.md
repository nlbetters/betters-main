# Morse Code CLI

The goal of this python project is to be able to encode and decode morse code using a shell, (and eventually to use this on a raspberry pi). The shell accepts commands such as listen, write, stop, and quit.

When 'listen' is entered in the shell prompt, the program listens through the microphone and tries to decode any morse code in real time. Once you type 'stop', it stops listening. The 'write' command lets you type a message in plain text, and then the program will play the Morse code version of it using beeps.

The Morse symbols (A–Z, numbers, and punctuation) are stored in a Python dictionary, where each letter or number is mapped to its Morse code equivalent (like A = .-, B = -..., and so on). The program uses that dictionary for both encoding and decoding.

It’s built with numpy and sounddevice to handle audio generation and microphone input, and everything runs in real time in the terminal. The goal was to make a simple but complete project that mixes signal processing, real-time input/output, and Python scripting — something that actually does something visual (or audible) and interactive.

## Features

* `listen` — starts decoding Morse code from microphone input

* `write` — converts text into Morse code beeps

* `stop` — ends the listening mode

* `quit` — exits the shell

Adjustable settings such as tone frequency, speed (WPM), and volume

## How to run
...
...

## Inspiration
I was thinking about projects that could include some signal processing applications like the ones I worked on in my Systems and Signals Lab, and that’s what gave me the idea for this. I thought it would be a fun way to turn some of those concepts into a real, interactive project that actually does something you can hear and experiment with.