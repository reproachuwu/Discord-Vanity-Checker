# Discord Vanity URL Checker

This Python script allows you to check the availability of Discord vanity URLs. It can operate in both automatic and manual modes, providing flexibility for different use cases.

## Features

- Automatic checking of random common words as vanity URLs
- Manual input option for specific vanity URL checks
- Discord webhook integration for notifications
- Rate limiting to avoid API restrictions
- Results logging to a text file
- Token-based authentication support

## Prerequisites

Before running this script, make sure you have the following installed:

- Python 3.7+
- aiohttp
- nltk

You can install the required packages using pip:

- pip install aiohttp nltk


Also, you need to download the NLTK words corpus:

- python
- import nltk
- nltk.download('words')


## Configuration

1. Open `main.py` and set the following variables:
   - `Authorization`: Your Discord user token (if using token mode)
   - `Notify`: Your Discord webhook URL for notifications
   - `token_mode`: Set to `True` to use token-based authentication, `False` otherwise

## Usage

Run the script using Python:

- python main.py


You will be prompted to choose between two modes:
1. Automatic mode: Randomly checks common words as vanity URLs
2. Manual input mode: Allows you to input specific vanity URLs to check

## Output

- Console output for each checked vanity URL
- Discord webhook notifications with embed messages

## Disclaimer

Please note that this script does not check for banned or unavailable URLs and may flag them as available. Use responsibly and in accordance with Discord's terms of service.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

[reproachuwu] - Initial work - [reproachuwu](https://github.com/reproachuwu)
