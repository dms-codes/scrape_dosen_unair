# Web Scraping with Python

This Python script is used for web scraping data from the Universitas Airlangga (Unair) faculty directory. The script fetches faculty URLs, generates pages URLs for each faculty, and extracts information from lecturer pages. The collected data is then saved to a CSV file.

## Prerequisites

Before running the script, ensure you have the necessary packages installed. You can install them using pip:

```
pip install requests beautifulsoup4
```

## Usage

1. Update the `BASE_URL` constant with the URL of the Unair faculty directory.
2. Set the desired `TIMEOUT` value for requests.
3. Run the script using Python:

```
python your_script_name.py
```

## Script Explanation

- `extract_text`: A function to extract and clean text from an element.

- `extract_faculties`: A function to extract faculty URLs from the main page.

- `extract_pages`: A function to generate pages URLs for each faculty.

- `extract_dosen_pages`: A function to extract lecturer information from their respective pages.

- The script initializes a session and sends a GET request to the specified `BASE_URL`.

- It extracts faculty URLs, generates pages URLs for each faculty, and extracts information from lecturer pages.

- The collected data is saved to a CSV file named `data_dosen_unair.csv`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Requests library](https://docs.python-requests.org/en/master/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
```

Make sure to customize the README with appropriate file names, paths, and additional information if needed.
