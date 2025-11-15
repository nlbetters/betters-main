# Morse Code CLI

The goal of this python project is to be able to encode and decode morse code using a shell, (and eventually to use this on a raspberry pi). The shell currently accepts commands such as `encode`, `decode`, `help`, and `quit`. In the future, it will also support `listen`, `write`, and `stop` for audio input/output (**Not implemented yet**).

When `listen` is entered in the shell prompt, the program will listen through the microphone and try to decode any morse code in real time. Once you type `stop`, it will stop listening. The `write` command will let you type a message in plain text, and then the program will play the Morse code version of it using beeps. (**These audio features are planned, but Not implemented yet.**)

The Morse symbols (A–Z, numbers, and punctuation) are stored in a Python dictionary, where each letter or number is mapped to its Morse code equivalent (like A = .-, B = -..., and so on). The program uses that dictionary for both encoding and decoding.

It’s built with numpy and sounddevice to handle audio generation and microphone input, and everything runs in real time in the terminal. The goal was to make a simple but complete project that mixes signal processing, real-time input/output, and Python scripting — something that actually does something visual (or audible) and interactive. (The audio/detector parts are **Not implemented yet**.)

## Features

### Currently implemented

* `encode` — converts text into Morse code symbols printed in the terminal  
* `decode` — converts Morse code symbols back into plain text  
* `help` — shows the list of available commands  
* `quit` — exits the shell  

### Planned (Not implemented yet)

* `listen` — starts decoding Morse code from microphone input (**Not implemented yet**)  
* `write` — converts text into Morse code beeps (**Not implemented yet**)  
* `stop` — ends the listening mode (**Not implemented yet**)  

Adjustable settings such as tone frequency, speed (WPM), and volume (**Not implemented yet**)

## How to run

From the project root, run:

`python3 -m morse.cli`

or:

`python3 morse/cli.py`

Once the shell starts, you can use commands like `encode`, `decode`, `help`, and `quit`.

## Inspiration

I was thinking about projects that could include some signal processing applications like the ones I worked on in my Systems and Signals Lab, and that’s what gave me the idea for this. I thought it would be a fun way to turn some of those concepts into a real, interactive project that actually does something you can hear and experiment with.