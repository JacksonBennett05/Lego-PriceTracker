# Lego Price Comparator

LegoPriceTracker is a Python project that compares prices for a specific LEGO set across multiple retailers (LEGO, Target, and Walmart) to find the cheapest option.

---

## Features

* Search by LEGO set **name or set number** (e.g., `75399`)
* Fetches live prices using a variety of APIs

  * LEGO (via Brickset API)
  * Target (via Target RedSky API)
  * Walmart
* Automatically determines which retailer has the best deal
* Simple command-line interface (CLI)

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/LegoPriceTracker.git
cd LegoPriceTracker
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## API Keys & Environment Variables

This project relies on third-party APIs. **API keys are required** and should be stored in a `.env` file in the root of the project.

### 1. Create a `.env` file

In the project root (same level as `requirements.txt`), create a file named:

```
.env
```

### 2. Add the following variables

```env
# Brickset (LEGO) API
BRICKSET_API_KEY=your_brickset_api_key
BRICKSET_USER=your_brickset_username
BRICKSET_PASS=your_brickset_password

# ScraperAPI (used for Walmart scraping)
SCRAPER_API=your_scraperapi_key

# Target RedSky API (public Target product API)
# No API key required
```

### 3. Where to get the keys

**Brickset API (LEGO prices)**

* Sign up: [https://brickset.com/tools/webservices](https://brickset.com/tools/webservices)
* Create an API key in your Brickset account
* Use your Brickset **username and password** (required for login)

**ScraperAPI (Walmart scraping)**

* Sign up: [https://www.scraperapi.com/](https://www.scraperapi.com/)
* Copy your API key from the dashboard

**Target RedSky API (Target pricing)**

* Uses Target's public RedSky product API
* No API key is required
* Requests are made directly to Target endpoints


---

## Running the CLI

Run the main script from the root of the project:

```bash
python src/main.py
```

Then:

* Enter the LEGO set number when prompted
* Confirm the correct set
* View prices from each retailer
* The script highlights the **cheapest option**

---

## Notes

* Prices depend on API availability and retailer page structure
* Walmart and Target results may vary if multiple listings exist
* Brickset data is generally the most stable source

---

## License

MIT License
