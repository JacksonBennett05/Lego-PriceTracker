# LegoPriceTracker

LegoPriceTracker is a Python project that compares prices for a specific LEGO set across multiple retailers (LEGO, Target, Walmart, BestBuy) to find the cheapest option.

---

## Features
- Search by LEGO set name or number (e.g., `75192`)
- Scrapes live prices from LEGO, Target, and Walmart
- Displays which store currently has the best deal

---

## Installation
1. Clone this repository:
 ```bash
  git clone https://github.com/yourusername/LegoPriceTracker.git
  cd LegoPriceTracker
  ```
2. Create a virtual environment
```bash
  python -m venv venv
  source venv/bin/activate   # macOS/Linux
  venv\Scripts\activate      # Windows
```
3. Install Dependencies
```bash
  pip install -r requirements.txt
```

## Running CLI
1. Run the main script directly from root of the project
 ```bash
  python src/main.py
 ```
2. Enter Set number when Prompted
3. Confirm correct set or try again
