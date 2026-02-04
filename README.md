# LegoPriceTracker

LegoPriceTracker is a Python project that compares prices for a specific LEGO set across multiple retailers (LEGO, Target and, Best Buy) to find the cheapest option.

---

## Features
- Search by LEGO set **name or set number** (e.g., `75399`)
- Scrapes live prices from
  - LEGO
  - Target
  - Best Buy
- Automatically determines which retailer has the best deal
- Simple command-line interface (CLI)

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
Run the main script directly from root of the project
 ```bash
  python src/main.py
 ```
Then:
- Enter the LEGO set number when prompted  
- Confirm the correct set  
- The script returns retailer prices and highlights the **cheapest option**

