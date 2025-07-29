# AI Web Scraper

An intelligent web scraping tool that combines web scraping capabilities with AI-powered content parsing. This application uses Selenium for web scraping and Ollama's LLaMA model for intelligent content extraction and analysis.

## Features

- **Web Scraping**: Automated website scraping using Selenium WebDriver
- **Content Cleaning**: Intelligent extraction and cleaning of webpage content
- **AI-Powered Parsing**: Use natural language descriptions to extract specific information from scraped content
- **Interactive UI**: User-friendly Streamlit interface
- **Batch Processing**: Handles large content by splitting into manageable chunks

## Technology Stack

- **Frontend**: Streamlit
- **Web Scraping**: Selenium WebDriver with Chrome
- **Content Parsing**: BeautifulSoup4
- **AI Processing**: LangChain with Ollama (LLaMA 3.1)
- **Language**: Python 3.13

## Prerequisites

Before running the application, ensure you have:

1. **Python 3.13** installed
2. **Chrome browser** installed
3. **ChromeDriver** (included in the project)
4. **Ollama** installed with LLaMA 3.1 model

### Installing Ollama

1. Download and install Ollama from [https://ollama.ai](https://ollama.ai)
2. Install the LLaMA 3.1 model:
   ```bash
   ollama pull llama3.1
   ```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd AI-WebScraper
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv ai
   ai\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**:
   ```bash
   streamlit run "AI WebScraper/main.py"
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
├── README.md
└── AI WebScraper/
    ├── main.py          # Streamlit application entry point
    ├── scrape.py        # Web scraping functionality
    ├── parse.py         # AI-powered content parsing
    ├── requirements.txt # Python dependencies
    ├── chromedriver.exe # Chrome WebDriver
    └── ai/              # Virtual environment
```

## Core Components

### `main.py`
- Streamlit web interface
- Manages user interactions and session state
- Coordinates scraping and parsing operations

### `scrape.py`
- **`scrape_website()`**: Uses Selenium to fetch webpage content
- **`extract_body_content()`**: Extracts body content from HTML
- **`clean_body_content()`**: Removes scripts, styles, and cleans text
- **`split_dom_content()`**: Splits large content into 6000-character chunks

### `parse.py`
- **`parse_with_ollama()`**: Uses LangChain and Ollama for AI-powered parsing
- Processes content chunks and extracts information based on natural language descriptions

## Example Use Cases

- **Product Information**: Extract product names, prices, and descriptions from e-commerce sites
- **News Articles**: Parse headlines, authors, and publication dates from news websites
- **Contact Information**: Extract email addresses, phone numbers, and addresses
- **Social Media**: Parse user profiles, posts, and engagement metrics
- **Research Data**: Extract specific data points from research papers or reports

## Configuration

The application uses the following default settings:

- **Chrome Driver**: `./chromedriver.exe`
- **AI Model**: LLaMA 3.1 via Ollama
- **Content Chunk Size**: 6000 characters
- **Wait Time**: 10 seconds for page loading

## Troubleshooting

### Common Issues

1. **ChromeDriver Issues**:
   - Ensure Chrome browser is installed
   - Update ChromeDriver if Chrome version has changed
   - Check ChromeDriver path in `scrape.py`

2. **Ollama Connection Issues**:
   - Verify Ollama is running: `ollama serve`
   - Confirm LLaMA 3.1 model is installed: `ollama list`

3. **Streamlit Issues**:
   - Check if port 8501 is available
   - Try running with different port: `streamlit run main.py --server.port 8502`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is for educational and research purposes. Always respect website terms of service and robots.txt files when scraping. Be mindful of rate limiting and avoid overloading servers.

