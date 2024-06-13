BUY = 1
SELL = -1

class Order():
    def __init__(self) -> None:
        self.symbol: str = ''
        self.side: int = 0
        self.qty: int = 0
        self.fill_price: float = 0
        self.pnl: float = 0

class Account():
    def __init__(self) -> None:
        self.working_orders = []
        self.completed_orders = []
        self.trades = []

    def market_buy(
            self,
            symbol: str,
            side: int,
            qty: int,
            price: float):
        pass

    def market_sell(
            self,
            symbol: str,
            side: int,
            qty: int,
            price: float):
        pass

    def limit_buy(
            self,
            symbol: str,
            side: int,
            qty: int,
            price: float):
        pass

    def limit_sell(
            self,
            symbol: str,
            side: int,
            qty: int,
            price: float):
        pass
    