# Anki Deck Generator

A simple desktop application built with PySide6 (Qt for Python) to generate Anki flashcard decks from text files.

## Features

- Create Anki decks from text files containing term-definition pairs
- Customizable deck names and separators
- Simple and intuitive graphical user interface
- Generates standard `.apkg` files compatible with Anki

## Requirements

- Python 3.6+
- PySide6
- genanki

## Installation

1. Clone this repository:
```bash
git clone https://github.com/andreipirone/Anki-Deck-Generator.git
cd Anki-Deck-Generator
```

2. Install the required dependencies:
```bash
pip install PySide6 genanki
```

## Usage

1. Run the application:
```bash
python ankigenqt.py
```

2. Enter a name for your deck in the "Deck Name" field.

3. Select a text file containing your terms and definitions using the "Browse" button.

4. Specify the separator character (default is `:`) used in your text file to separate terms from definitions.

5. Click "Generate Anki Deck" to create your Anki deck file.

### Input File Format

Your definitions file should be a plain text file with each line formatted as:
```
term:definition
```

Example:
```
Python:A high-level programming language
Variable:A named storage location in memory
Function:A block of organized, reusable code
```

The separator can be customized in the application (default is `:`).

## Output

The application generates an `.apkg` file with the same name as your deck (with spaces replaced by underscores). This file can be imported directly into Anki.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with [PySide6](https://wiki.qt.io/Qt_for_Python) (Qt for Python)
- Uses [genanki](https://github.com/kerrickstaley/genanki) for Anki deck generation
- Anki is a trademark of Ankitects Pty Ltd
