from queries.query_reader import read_queries
from scraper.amazon_scraper import AmazonScraper
from storage.json_writer import save_to_json

def main():
    queries = read_queries("../user_queries.json")
    scraper = AmazonScraper()

    for query in queries:
        print(f"Scraping data for query: {query}")
        products = scraper.scrape(query, pages=20)
        save_to_json(query, products)

if __name__ == "__main__":
    main()
