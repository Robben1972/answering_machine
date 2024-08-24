# Telegram Echo Bot

This is a simple Telegram bot that automatically responds with "Hello" when it receives a message with the text "Hello", "hello", "helo", or "Helo". The bot is built using the [Pyrogram](https://docs.pyrogram.org/) library.

## Prerequisites

Before running the bot, you need to have the following:

1. Python 3.7+
2. A Telegram account
3. A Telegram API ID and API Hash, which you can obtain from [Telegram's official website](https://my.telegram.org/).

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:Robben1972/answering_machine.git
   cd repo-name
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root directory of your project:**

   In the `.env` file, you need to add your Telegram API credentials.

   ```text
   API_ID=your_api_id
   API_HASH=your_api_hash
   ```

   Replace `your_api_id` and `your_api_hash` with your actual API ID and Hash obtained from [Telegram's official website](https://my.telegram.org/).

## Running the Bot

After setting up the environment and adding your API credentials:

1. **Run the bot:**

   ```bash
   python main.py
   ```
