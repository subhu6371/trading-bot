import argparse
from rich.console import Console
from rich.table import Table
from bot.orders import execute_order
from bot.validators import validate_order_input

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot CLI")
    parser.add_argument("--symbol", "-s", required=True, type=str, help="Trading pair, e.g., BTCUSDT")
    parser.add_argument("--side", required=True, type=str, help="BUY or SELL")
    parser.add_argument("--type", dest="order_type", required=True, type=str, help="MARKET or LIMIT")
    parser.add_argument("--qty", "-q", required=True, type=float, help="Amount to trade")
    parser.add_argument("--price", "-p", type=float, default=None, help="Required if type is LIMIT")
    
    args = parser.parse_args()
    
    try:
        # 1. Validate Input
        validate_order_input(args.order_type, args.price)
        
        # 2. Execute Order
        response = execute_order(args.symbol, args.side, args.order_type, args.qty, args.price)
        
        # 3. Print Enhanced UI Table
        table = Table(title="Order Execution Summary")
        table.add_column("Order ID", style="cyan", no_wrap=True)
        table.add_column("Symbol", style="magenta")
        table.add_column("Side", style="blue")
        table.add_column("Status", style="green")
        table.add_column("Executed Qty", style="yellow")
        
        table.add_row(
            str(response.get("orderId", "N/A")),
            response.get("symbol", args.symbol),
            response.get("side", args.side),
            response.get("status", "N/A"),
            str(response.get("executedQty", args.qty))
        )
        
        console.print(table)
        console.print("[bold green]✔ Transaction completed successfully.[/bold green]\n")

    except ValueError as e:
        console.print(f"\n[bold red]Validation Error:[/bold red] {e}")
    except Exception as e:
        console.print(f"\n[bold red]✖ Order failed.[/bold red] Reason: {str(e)}")
        console.print("[dim]Please check bot.log for full details.[/dim]\n")

if __name__ == "__main__":
    main()