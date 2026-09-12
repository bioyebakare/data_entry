# Zillow Rental Data Entry Bot

A Python automation script that scrapes rental listing data from Zillow and automatically fills out a Google Form with the details, no manual copy-pasting needed.

## What it does

- Uses Selenium to open Zillow search results and extract listing details (address, price per month, bedrooms/bathrooms, square footage, and listing link)
- Automatically opens a Google Form ("Renting Research") and fills in the scraped data for each listing
- Submits the form, then moves on to the next listing

## Built with

- Python
- Selenium (browser automation)
- python-dotenv (for keeping config/credentials out of the codebase)


## Notes

- Requires Google Chrome and a matching ChromeDriver version.
- Selenium locators are tied to Zillow and Google Forms' current page structure, if either site updates their layout, selectors may need adjusting.
