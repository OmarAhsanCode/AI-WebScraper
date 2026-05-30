# AI Web Scraper

An intelligent web scraping tool that combines web scraping capabilities with AI-powered content parsing. This application is optimized for deployment on Streamlit Cloud, utilizing a headless Chromium driver for web scraping and the Groq API (running `llama-3.1-8b-instant`) for intelligent content extraction and analysis.

## Features

- **Web Scraping**: Automated website scraping using Selenium WebDriver (configured for headless Linux execution on Streamlit Cloud)
- **Content Cleaning**: Intelligent extraction and cleaning of webpage content
- **AI-Powered Parsing**: Use natural language descriptions to extract specific information from scraped content via Groq API
- **Interactive UI**: User-friendly Streamlit interface
- **Batch Processing**: Handles large content by splitting into manageable chunks

## Technology Stack

- **Frontend**: Streamlit
- **Web Scraping**: Selenium WebDriver (with headless Chromium/chromedriver)
- **Content Parsing**: BeautifulSoup4
- **AI Processing**: Groq Python SDK (LLaMA 3.1 8B Instant)
- **Language**: Python 3.13

## Prerequisites / Configuration

Before running the application:

1. **Groq API Key**: You need an API key from Groq.
2. **Streamlit Secrets**:
   - For local testing, create `app/.streamlit/secrets.toml` with the following content:
     ```toml
     GROQ_API_KEY = "your_actual_groq_api_key"
     ```
   - For Streamlit Cloud, configure `GROQ_API_KEY` under the app secrets settings.

> [!NOTE]
> The headless Selenium setup expects system-level Chromium and ChromeDriver installed (which are specified in `packages.txt` for Streamlit Cloud). Running the scraper locally on Windows/macOS may require adjusting the driver paths in `scrape.py` to match your local installation.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd AI-WebScraper
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate # On Linux/macOS use: source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r "app/requirements.txt"
   ```

## Usage

1. **Start the application**:
   ```bash
   cd "app"
   streamlit run main.py
   ```

2. **Using the Web Interface**:
   - Enter a website URL in the input field
   - Click "Scrape Site" to extract content from the webpage
   - Review the scraped DOM content in the expandable section
   - Describe what specific information you want to extract
   - Click "Parse Content" to use AI for intelligent content extraction

## Project Structure

```
AI-WebScraper/
├── packages.txt           # Installs Chromium & Chromedriver on Streamlit Cloud
├── requirements.txt       # Python dependencies (root-level for deploy)
├── README.md              # Documentation
├── .gitignore             # Git ignored files
├── .gitattributes         # Git attributes
└── app/
    ├── main.py            # Streamlit application entry point
    ├── scrape.py          # Web scraping functionality (headless Chrome setup)
    ├── parse.py           # AI-powered content parsing using Groq
    ├── requirements.txt   # Python dependencies
    └── .streamlit/
        └── secrets.toml   # Streamlit secrets (local API key, git-ignored)
```

## Core Components

### `main.py`
- Streamlit web interface
- Manages user interactions and session state
- Coordinates scraping and parsing operations

### `scrape.py`
- **`get_driver()`**: Configures Selenium with headless options and specifies binary paths suitable for Streamlit Cloud.
- **`scrape_website()`**: Uses Selenium to fetch webpage content safely inside try/finally blocks.
- **`extract_body_content()`**: Extracts body content from HTML.
- **`clean_body_content()`**: Removes scripts, styles, and cleans text.
- **`split_dom_content()`**: Splits large content into 6000-character chunks.

### `parse.py`
- **`parse_with_ollama()`**: Uses Groq client to call `llama-3.1-8b-instant` for AI-powered parsing.
- Processes content chunks and extracts information based on natural language descriptions.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is for educational and research purposes. Always respect website terms of service and robots.txt files when scraping. Be mindful of rate limiting and avoid overloading servers.
