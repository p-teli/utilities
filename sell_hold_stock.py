
def calculate_net_aftertax(capital, profit_percentage, tax_rate):

  gross_profit = capital * profit_percentage / 100
  tax_amount = gross_profit * tax_rate / 100
  net_profit = gross_profit - tax_amount
  return capital + net_profit

def calculate_net_afterdrop(capital, profit_percentage,price_drop_percentage):

  gross_profit = capital * profit_percentage / 100
  net_worth = capital + gross_profit
  drop = net_worth * price_drop_percentage / 100
  return net_worth - drop
 
def main():
  capital = 1000
  tax_rate = 25
  price_drop_percentage = 10

  for profit_percentage in range(10, 1001, 10):
    net_aftertax = calculate_net_aftertax(capital, profit_percentage, tax_rate)
    net_afterdrop = calculate_net_afterdrop(capital, profit_percentage,price_drop_percentage)
    diff = net_aftertax - net_afterdrop
    print(f"At {profit_percentage}% profit, the net_aftertax is {net_aftertax}.")
    print(f"At {profit_percentage}% profit, the net_afterdrop is {net_afterdrop}.")
    print(f"At {profit_percentage}% profit, the difference is {diff}.")
    if net_afterdrop > net_aftertax:
      print(f"At {profit_percentage}% profit, it's better to hold the stock.")
    else:
      print(f"At {profit_percentage}% profit, it's better to sell the stock.")

    if net_afterdrop == net_aftertax:
      print(f"At {profit_percentage}% profit, the tax paid equals the price drop.")

if __name__ == "__main__":
  main()
