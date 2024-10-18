# Voice Chess

# Overview

IoT ChessBoard, built to help people with mobility impairments,
consists of a mechanical cartesian movement system, which displaces
an electromagnet, moving the chess pieces, the board connects to an
API which stores user data (game hisotory, stats, etc) to a DB, we
also provide a web interface for user data visualization

# Features

- **Voice-Automated Board:** Play entirely with voice commands.
- **Real-Time Games:** Play with other board client in real-time.
- **Backend API:** API for communicating boards, user data CRUD and integrations.
- **Web Interface:** Web Page for user data visualization and board configs.

# Usage

To fully use the project you need to build the board, for which we provide a guide in
[board guide](board/README.md), you can also mock the hardware and setup a board
client which interacts with the API as if it were a board.

Follow the [API guide](board/README.md) to set it up, as well as setting the DB.

Follow the [frontend guide](board/README.md) to set up the web interface.

