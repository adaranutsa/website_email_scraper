# Website Email Scraper
Python Website Email Scraper

## Purpose
A simple website email scraper. It's sole purpose is for practicing unittests in python.

## Requirements

- Python 3.6+
- virtualenv

## Setup

The recommended practice is to set up a virtual environment. Clone this repository and following the instructions.

```bash
cd website_email_scraper
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

## Usage

It's a simple commandline execution.

Executing with 1 url:
```bash
python main.py --urls  https://creativecommons.org/about/contact/
```

Executing with 3 urls:
```bash
python main.py --urls  https://creativecommons.org/about/contact/,https://www.google.com/,https://www.msn.com/
```

## Testing

Simple execute the `test_main.py` for performing unittests.

```bash
python test_main.py
```