# Domain Checker Telegram Bot

## Getting Started

1. Clone the project repository.

```bash
git clone https://github.com/domain-checker/domain-checker.git
cd domain-checker
```

2. Install the required Python packages from `requirements.txt`.

> We recommend using a [virtual environment](https://docs.python.org/3/library/venv.html) to run this project.

```bash
pip install -r requirements.txt
```

3. Create a new `.env` file and add your unique bot token from the [BotFather](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) in the following format:

```bash
export BOT_TOKEN=<INSERT-BOT-TOKEN-HERE>
```

> An example `.env` file can be found in `.env.example`.

4. Read the environment variables from the `.env` file.

```bash
source .env
```

5. Run the bot.

```bash
python3 -u bot.py
```

Congratulations! You have successfully started your Telegram bot. :tada:

## Acknowledgements

- Python libraries used: [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/index.html), [python-whois](https://pypi.org/project/python-whois/)
