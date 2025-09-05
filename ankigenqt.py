import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QLineEdit, QFileDialog, QMessageBox
)
import genanki
import uuid

class AnkiDeckGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Anki Deck Generator')
        self.setGeometry(100, 100, 500, 250)
        
        layout = QVBoxLayout()
        
        deck_name_layout = QHBoxLayout()
        deck_name_layout.addWidget(QLabel('Deck Name:'))
        self.deck_name_input = QLineEdit('Default Deck')
        deck_name_layout.addWidget(self.deck_name_input)
        layout.addLayout(deck_name_layout)
        
        file_layout = QHBoxLayout()
        file_layout.addWidget(QLabel('Definitions File:'))
        self.file_path_input = QLineEdit()
        file_layout.addWidget(self.file_path_input)
        browse_button = QPushButton('Browse')
        browse_button.clicked.connect(self.browse_file)
        file_layout.addWidget(browse_button)
        layout.addLayout(file_layout)
        
        separator_layout = QHBoxLayout()
        separator_layout.addWidget(QLabel('Separator:'))
        self.separator_input = QLineEdit(':')
        self.separator_input.setMaxLength(1)
        separator_layout.addWidget(self.separator_input)
        layout.addLayout(separator_layout)
        
        self.generate_button = QPushButton('Generate Anki Deck')
        self.generate_button.clicked.connect(self.generate_deck)
        layout.addWidget(self.generate_button)
        
        self.setLayout(layout)
        
    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Select Definitions File', '', 'Text Files (*.txt)'
        )
        if file_path:
            self.file_path_input.setText(file_path)
            
    def generate_deck(self):
        deck_name = self.deck_name_input.text().strip()
        file_path = self.file_path_input.text().strip()
        separator = self.separator_input.text()
        
        if not deck_name:
            QMessageBox.warning(self, 'Input Error', 'Please enter a deck name')
            return
            
        if not file_path:
            QMessageBox.warning(self, 'Input Error', 'Please select a definitions file')
            return
            
        if not separator:
            QMessageBox.warning(self, 'Input Error', 'Please enter a separator')
            return
            
        if not Path(file_path).exists():
            QMessageBox.critical(self, 'File Error', 'Selected file does not exist')
            return
            
        try:
            self.create_anki_deck(deck_name, file_path, separator)
            QMessageBox.information(
                self, 
                'Success', 
                f'Anki deck "{deck_name}" created successfully!'
            )
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to create deck:\n{str(e)}')
            
    def create_anki_deck(self, deck_name, file_path, separator):
        deck_id = int(str(uuid.uuid4().int)[:10])
        
        my_deck = genanki.Deck(deck_id, deck_name)
        
        my_model = genanki.Model(
            1607392319,
            'Simple Model',
            fields=[
                {'name': 'Term'},
                {'name': 'Definition'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Term}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Definition}}',
                },
            ]
        )
        
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if separator in line:
                    term, definition = line.split(separator, 1)
                    note = genanki.Note(
                        model=my_model, 
                        fields=[term.strip(), definition.strip()]
                    )
                    my_deck.add_note(note)
                elif line:  
                    print(f"Warning: Line {line_num} doesn't contain separator '{separator}': {line}")
        
        output_file = f"{deck_name.replace(' ', '_')}.apkg"
        genanki.Package(my_deck).write_to_file(output_file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnkiDeckGenerator()
    window.show()
    sys.exit(app.exec())