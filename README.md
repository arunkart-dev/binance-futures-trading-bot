# Binance Futures Trading Bot (Python)

A CLI-based trading bot built using Python and the official Binance Futures Testnet API.

## Features
- Market order execution (BUY / SELL)
- Limit order execution
- Command-line interface
- Input validation
- Structured logging
- Error handling

## Technologies Used
- Python
- Binance Futures Testnet API
- REST APIs
- JSON
- python-binance library

 ## Project Structure

```text
binance-futures-trading-bot/
│
├── bot.py              # Main CLI trading bot (market & limit orders)
├── validators.py       # Input validation logic (symbol, quantity, price)
├── logger.py           # Centralized logging configuration
├── bot.log             # Log file for API responses and errors (ignored in Git)
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules (logs, cache, secrets)


## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/your-username/binance-futures-trading-bot.git
cd binance-futures-trading-bot
