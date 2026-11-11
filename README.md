# Geo-Guesser CLI

A command-line guessing game written in Python. A random country or capital is picked, and you guess it one letter at a time before your lives run out.

> **Version 1.** This is the first release. Version 2 is coming.

## Features

- Guess **countries** or **capitals**
- Play from the **whole world** or a **specific continent**
- **5 lives**: every wrong letter costs one
- **One hint per game**: type `hint` to reveal a random letter
- **Play again** after each round
- No external dependencies

## Requirements

- Python 3.8 or newer

## Installation

```bash
git clone https://github.com/izramkhan/geo-guesser-cli.git
cd geo-guesser-cli
```

## Usage

```bash
python main.py
```

## Project Structure

```
geo_guesser_cli/
├── main.py            # Entry point and play-again loop
├── geo_guesser.py     # Game loop for one round
├── chooser.py         # Menus for choosing what to guess
├── picker.py          # Picks a random word from the chosen list
├── data/              # Country and capital lists
├── utils/             # Helpers and input validation
└── viz/               # Display output and messages
```

## Roadmap

- **Version 1** (current): core game with hints, lives and replay
- **Version 2**: planned

## Author

Izram Khan