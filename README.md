# Binance Futures Testnet Trading Bot

## Setup

pip install -r requirements.txt

Create .env

BINANCE_API_KEY=...
BINANCE_API_SECRET=...

## Run

Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000

Logs are stored in:

logs/trading.log
