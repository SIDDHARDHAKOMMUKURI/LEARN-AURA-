LearnAuraBot 🤖📚

LearnAuraBot is an AI-powered Telegram bot designed to make learning interactive, easy, and fun. It integrates AI Q&A, search, textbooks, and file transfer features to provide a complete educational experience on Telegram.

Features

/start – Welcomes the user and provides a brief overview of the bot.

/learn – Offers curated learning content by subjects (Coding, Social, Science, etc.).

/ask – Ask any question and get AI-generated answers via Gemini AI.

/search – Search for any topic using SerpAPI for accurate results.

Textbooks – Access NCERT textbooks by class and subject with options to:

Read Online

Download PDF

File Transfer – Upload files from local storage or Google Drive and convert between:

PDF ↔ Word

PPT ↔ PDF

TXT ↔ PDF

Image → Text

User Manual – Provides detailed instructions for all commands and features.

Screenshots

Add some screenshots of your bot interface here (optional).

Installation

Clone the repository:

git clonehttps://github.com/SIDDHARDHAKOMMUKURI/LEARN-AURA-BOT.git
cd LearnAuraBot


Install dependencies:

pip install -r requirements.txt


Set up environment variables:

Create a .env file and add:

BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
SERPAPI_KEY=your_serpapi_key
MONGO_URI=your_mongodb_connection_string


Run the bot:

python main.py

Usage

Start the bot on Telegram using /start.

Use /learn to explore learning content by subject.

Ask any question using /ask.

Use /search to find information on the web.

Access textbooks and read online or download PDFs.

Upload files and convert them using the File Transfer feature.

Project Structure
LearnAuraBot/
│
├── main.py                # Entry point of the bot
├── handlers/
│   ├── start.py           # /start command handler
│   ├── ask.py             # /ask command handler
│   ├── learn.py           # /learn command handler
│   ├── search.py          # /search command handler
│   ├── textbook.py        # Textbook handler
│   └── file_transfer.py   # File transfer handler
├── utils/
│   └── helpers.py         # Helper functions
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

Technologies Used

Python 3.10+

python-telegram-bot – Telegram Bot API

Gemini AI API – AI question-answering

SerpAPI – Web search API

MongoDB – For user data storage

NCERT textbooks – Official learning content

Contributing

Contributions are welcome! Feel free to:

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/your-feature)

Open a Pull Request

License

This project is licensed under the MIT License – see the LICENSE
 file for details.

Contact

Developer: Siddhardha Kommukuri


