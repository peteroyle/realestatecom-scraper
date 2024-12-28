"""
This example run script shows how to run the realestate.com.au scraper defined in ./realestate.py
It scrapes ads data and saves it to ./results/

To run this script set the env variable $SCRAPFLY_KEY with your scrapfly API key:
$ export $SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
"""
import asyncio
import json
import realestate
from pathlib import Path

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)


async def run():
    # enable scrapfly cache for basic use
    realestate.BASE_CONFIG["cache"] = True

    print("running Realestate.com.au scrape and saving results to ./results directory")

    properties_data = await realestate.scrape_properties(
        urls=[
            "https://www.realestate.com.au/property-house-vic-eaglemont-146584336",
            "https://www.realestate.com.au/property-house-vic-eaglemont-145607856",
            "https://www.realestate.com.au/property-house-vic-viewbank-146895688",
        ]
    )
    with open(output.joinpath("properties.json"), "w", encoding="utf-8") as file:
        json.dump(properties_data, file, indent=2, ensure_ascii=False)

    search_data = await realestate.scrape_search(
        # you can change "buy" to "rent" in the search URL to search for properties for rent
        url="https://www.realestate.com.au/buy/property-house-with-2-bedrooms-size-600-5000-between-900000-any-in-eaglemont,+vic+3084/list-1?numParkingSpaces=1&numBaths=1&newOrEstablished=established&activeSort=list-date&sourcePage=rea:buy:srp-map&sourceElement=tab-headers",
        max_scrape_pages=3,
    )
    with open(output.joinpath("search.json"), "w", encoding="utf-8") as file:
        json.dump(search_data, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    asyncio.run(run())
