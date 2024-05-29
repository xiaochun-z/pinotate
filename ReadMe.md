# Pinotate

Pinotate is a Python-based tool designed to export highlights from iBooks. It offers both a command-line interface and a GUI version for user flexibility.

## Features
- **Export highlights**: Ability to export all highlights per book.
- **Export highlights of a specified book**: Ability to export highlights of a book with a specific title.
- **List books**: Display all book titles.
- **Markdown headings**: Add headings to the markdown export.
- **Sort options**: Sort the highlights either by location or by time.

## Usage

To use Pinotate, run the following command:

```
usage: pinotate.py [-h] [-o OUT] [-l] [--headings] [-s] [title]
```

- **Positional Argument**:
  - `title`: Export highlights of the book with a specific title (optional).
  
- **Optional Arguments**:
  - `-h, --help`: Show the help message and exit.
  - `-o OUT, --out OUT`: Specify the output directory.
  - `-l, --list`: Print book titles.
  - `--headings`: Add headings to markdown.
  - `-s, --sort`: Sort by location instead of time.

To export all highlights to the current directory, simply run:

```
pinotate.py
```

### Requirements

- Python 3

## Pinotate GUI

For those who prefer a graphical interface, Pinotate also offers a GUI version.

### Setup and Run

```shell
python3 -m venv .pyenv
source .pyenv/bin/activate
pip install -r requirements.txt
./pinotate-gui.py
```

### Requirements for GUI

- Python 3
- [wxPython](https://wxpython.org/download.php#osx)
- [markdown](https://pypi.org/project/Markdown/)


### Export words from .md to text file
#### Motivation for md2txt.py
As an English learner I need to expand my vocabulary, so I am using an app on iPhone to memorize some new words every day, I also read English books, and found a lot of new words in these books.
After found a new word, I highlight this word in iBooks, which is good, but I also need to review these new words regularly, thus I need to export all the words to my iPhone app so I can memorize them.
Md2txt.py is a script to read the content from all the .md files in the current directory, and re-export them to a .txt file, I will use this .txt file to import these words to my iPhone App to study these words.
I read English books every day, and every day I’ll meet new words, so I have to re-export these new words and import the new one, I need to do export multiple times a week.
So I added -ignore-date-before parameter to ignore some words by a specific date, so I don’t need to re-import the imported words, but just new words.

```console
# md2txt.py parameters:
# --ignore-phrase(0 or 1): only export the words, ignore the phrases or sentences. 
# --output-single-file(0 or 1): output all the words to a single .txt file instead of seperated .txt files.
# --ignore-date-before: a date time string: '2000-03-28' or "2000-03-28 15:32:06", if the word was highlighted before this date, then ignore this word, it will not be exported to txt file.
./md2txt.py --ignore-phrase 1  --output-single-file 1 --ignore-date-before 2000-03-28
./md2txt.py --ignore-phrase 1  --output-single-file 1 --ignore-date-before "2000-03-28 15:32:06"
```

## License

This project is licensed under the terms of the MIT license. You can find the full license in the `LICENSE.txt` file located in the root directory.
