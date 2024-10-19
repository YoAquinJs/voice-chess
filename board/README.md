# Chess Board

Mecatronic chessboard for playing chess via voice commands.
This branch is divided in two, the Board Client, running in a Raspberry PI,
and the Mecatronic System, running in a microcontroller.

We split the Board Client and Mecatronic system, for decoupling the overall project,
this allow us to easily mock the hardware on the board, providing a Board Client
to the API with no mecatronic system required.

For the microcontroller we chose the Esp32, as it's cheap, small, easy to quickstart
and provides all the hardware interfaces we require.
We chose the Raspberry PI for running the Board Client, because we needed to run
STT and TTS models, and easily communicate to the microcontroller.

We decided that building the mechanic's from zero would be inviable duo to deadlines,
so we modified a personal laser cutter, swapping the laser with the electromagnet
and removing it's motherboard, so we could focus on the electronic and programming.

If you intend to build the mechanic system, we included a materials section which
lists the general pieces you need to make it work, be aware you will need more than
what's listed, as we only specified the general pieces.

## Board Client

Python program serving as an intermediari between the user, the board and the API.
Handles user voice commands, via STT and TTS AI models, API requests and fetches,
and serial communication with the Mecatronic System microcontroller to trigger movements.

### Configuration

TODO

### Usage

The Board Client can run without the Mecatronic System by passing the `TODO flag` flag,
when running with the hardware it won't handle commands if hardware is disconnected.

Check the [commands](board/client/commands.md) available for the board client.

The program dependencies are listed in the requirements.txt, it's advised
to run it in it's owned virtual environment.
One additional dependency is needed, portaudio which is required by pyaudio,
it can be installed in the Raspberry Pi via (or debian based systems):

```bash
sudo apt install portaudio19-dev
```

Start venv, install python dependencies, and run the client:

```bash
cd board/client

virtualenv
pip install -r requirements.txt

python3 src/main.py
```

## Mecatronic System

Cartesian movement system for moving the chess pieces, works by displacing an electromagnet,
which on activation, moves the ferromagnetic material attached to the chess pieces.
Receives movement commands from the Board Client via serial, queues the commands and
handles the electronic components for executing them.

### Materials

In parenthesis we specify what specific component we used

- **Mechanic:*
	- Linear rails and carriages
	- Transmission, timing belt, dented pulleys, more...
	- Mounting of the stepper motors
	- Cable distribution
	- Casing and chessboard
- **Electronics:*
	- DC Power Supply (12V 5A), and voltage regulation module
	- Raspberry PI (Model 4B with 4Gb)
	- Microcontroller compatible with the code (Esp32)
	- Stepper Motors (Nema 17 17HS4401), and their drivers (a4988), at least 2 of each
	- Electromagnet (keyStudio KS0320)
	- Display (OLED display 0.96 inc)

The motors we used work with 12V and consume less than 1A, the electromagnet works with
5V and consumes 0.3A max,

### Usage

TODO
