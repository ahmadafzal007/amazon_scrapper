# Amazon Product Scraper

## Description
A Python script to scrape product details from Amazon for a set of search queries.

## Features
- Scrapes titles, reviews, prices, and images.
- Saves results to JSON files named after the query.
- Modular design for scalability and readability.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`

## Usage
Run the script: `python src/main.py`

## Input File Format
`user_queries.json`: A JSON file containing an array of search queries (e.g., ["headphones", "smartphones"]).

## Output
JSON files for each query will be saved in the `output/` directory.