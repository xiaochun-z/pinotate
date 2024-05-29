## Motivation for md2txt.py

As an English learner I need to expand my vocabulary, so I am using an app on iPhone to memorize some new words every day, I also read English books, and found a lot of new words in these books.
After found a new word, I highlight this word in iBooks, which is good, but I also need to review these new words regularly, thus I need to export all the words to my iPhone app so I can memorize them.

Md2txt.py is a script to read the content from all the .md files in the current directory, and re-export them to a .txt file, I will use this .txt file to import these words to my iPhone App to study these words.

I read English books every day, and every day I’ll meet new words, so I have to re-export these new words and import the new one, I need to do export multiple times a week.

So I added -ignore-date-before parameter to ignore some words by a specific date, so I don’t need to re-import the imported words, but just new words.

```bash
# md2txt.py parameters:
# --ignore-phrase(0 or 1): only export the words, ignore the phrases or sentences. 
# --output-single-file(0 or 1): output all the words to a single .txt file instead of seperated .txt files.
# --ignore-date-before: a date time string: '2000-03-28' or "2000-03-28 15:32:06", if the word was highlighted before this date, then ignore this word, it will not be exported to txt file.
./md2txt.py --ignore-phrase 1  --output-single-file 1 --ignore-date-before 2000-03-28
./md2txt.py --ignore-phrase 1  --output-single-file 1 --ignore-date-before "2000-03-28 15:32:06"
```
