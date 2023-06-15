# Discord Username Checker

This is a Python script that allows you to check the availability of Discord usernames. It utilizes multiple tokens, multithreading, and handles rate limits, connection errors, and unauthorized tokens.

## Requirements

- Python 3.7 or higher
- Dependencies listed in the `requirements.txt` file

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/discord-username-checker.git

2. pip install -r requirements.txt


## Configuration

1. Open the config.json file and specify the desired method (friends or another method) for checking usernames. 

   me - checks by submitting a Discord friend request, this is the only working method I know of as of now.

2. Prepare your tokens and wordlists:

Create a tokens.txt file and specify your Discord token(s) in it. Make sure you don't share your token with anyone.

There are several Dutch and English wordlists included in the wordlists folder. If you want to filter your own wordlists, you can use the helper.py script to split lines (for copy pasted words with the wrong formatting) or filter the word length from a list of given usernames. Make sure you put the .txt files in the wordlists folder.

Note: The wordlists included in this repository are provided as examples and may not contain an exhaustive list of usernames. You can replace them with your own wordlists for more comprehensive checks.

## Usage

python main.py -t <number_of_threads>

Replace <number_of_threads> with the desired number of threads to use for checking usernames. By default, it uses one thread.

in the tokens.txt file, specify the Discord token(s), MAKE SURE YOU DON'T SHARE YOUR TOKEN WITH ANYONE.

The script will start checking the availability of usernames in the wordlists using the provided tokens. The results will be stored in separate files: available.txt and unavailable.txt.

## License

This project is licensed under the MIT License.

## Acknowledgments

The loguru library for flexible logging: https://github.com/Delgan/loguru
