# LAB - Class 03

## Project: Madlibs

## Author: Bradley Hower

How to initialize/run your application (where applicable)

`python3 madlib_cli/madlib.py`

### Tests

**How do you run tests?**

Run tests via `pytest`. To install, `pip install pytest`.

Any tests of note?

There are three four tests. One test confirms that the input file is read and outputs pure text. The second test confirms that the madlibs template is properly parsed so as to be properly formatted to allow new text to come in as well as to be able to user a sequeece of words needed for automatic filling. The thirds test confirms that a proper merge of user word inputs has been combined with the madlibs template. Lastly, there is a FileNotFound test to confirm that an error is thrown in case the input file path is faulty.
