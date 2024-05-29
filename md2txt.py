#! python3
import os
import datetime
import argparse

# MacOS: ./md2txt.py --ignore-phrase 1  --output-single-file 1 --ignore-date-before "2000-03-28"
# python ./md2txt.py --ignore-phrase 1  --output-single-file 1 --ignore-date-before "2000-03-28 14:02:54"

class Word:
    def __init__(self, time, word):
        self.time = time
        self.word = word


class Book:
    def __init__(self, title, file):
        self.title = title
        self.words = []
        self.file = file

    def add_word(self, time, word):
        self.words.append(Word(time, word))


def read_book_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Extract book title
    if "# " in content:
        book_title = content.split("\n")[0].replace("# ", "")
    else:
        book_title = "Unknown"

    book = Book(book_title, file_path)

    found_time_stamp = False
    # Extract timestamps and words
    for line in content.split("\n"):
        # if the line start with a * and end with *, inside it's a date time
        if line.startswith("*") and line.endswith("*"):
            timestamp = datetime.datetime.strptime(
                line[1:-1], "%a %b %d %H:%M:%S %Y")
            found_time_stamp = True
        # found time stamp, now the words will follow up

        if found_time_stamp and line.startswith('>'):
            found_time_stamp = False
            book.add_word(timestamp, line.replace('>', '').strip())

    return book


# Example usage
folder_path = "./"
books = []
for filename in os.listdir(folder_path):
    # ignore the macos files
    if filename.endswith(".md") and not filename.startswith("._"):
        file_path = os.path.join(folder_path, filename)
        book = read_book_from_file(file_path)
        books.append(book)

# Create the parser
parser = argparse.ArgumentParser()
parser.add_argument('--ignore-phrase', type=int, default=0)
parser.add_argument('--output-single-file', type=int, default=0)
parser.add_argument('--ignore-date-before', type=str, default=None)
args = parser.parse_args()

ignore_date_before = None
if parser.parse_args().ignore_date_before:
    date_str = parser.parse_args().ignore_date_before
    if len(date_str.strip()) == 10:
        date_str += " 00:00:00"
    ignore_date_before = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

print(f"ignore_phrase: {args.ignore_phrase}")
print(f"output_single_file: {args.output_single_file}")
print(f"ignore_date_before: {ignore_date_before}")

all_words = []


def save_book_to_file(book, args, ignore_date_before):
    print(f"Processing: {book.title}")
    # save to txt file
    # Clean the book title for file name
    if args.output_single_file != 0:
        all_words.extend(book.words)
    else:
        words = [word.word for word in book.words if not (args.ignore_phrase != 0 and ' ' in word.word) and (
            ignore_date_before is None or word.time >= ignore_date_before)]
        if len(words) == 0:
            return
        clean_title = "".join(
            c for c in book.title if c.isalnum() or c.isspace())
        with open(f"{clean_title}.txt", "w") as file:
            file.write('\n'.join(words))
            # print all the words
            # for word in words:
            #     print(word)
        print(f"{len(words)} words saved to {clean_title}.txt")


# Save each book to file
for book in books:
    save_book_to_file(book, args, ignore_date_before)

save_all_file = "all_words.txt"
# Save all words to a single file if applicable
if len(all_words) > 0:
    words = [word.word for word in all_words if not (args.ignore_phrase != 0 and ' ' in word.word) and (
        ignore_date_before is None or word.time >= ignore_date_before)]
    if len(words) > 0:
        with open(save_all_file, "w") as file:
            file.write('\n'.join(words))
            # print all the words
            # for word in words:
            #     print(word)
        print(f"{len(words)} saved to {save_all_file}")
