hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]
print('Haircut Prices: ', prices)

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_price = sum(i for i in prices)
average_price = total_price / len(prices)
print('Average Haircut Price: ', average_price)
new_prices = [num - 5 for num in prices]
print('New Prices: ', new_prices)
new_total = sum(i for i in new_prices)
new_average = new_total / len(new_prices)
print('New Average price: ', new_average)
#Revenue for Carly's Clippers (previous week)
total_revenue = 0
i = range(len(prices))
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print('Total Revenue: ', total_revenue)
avg_daily_revenue = total_revenue / 7
print('Average Daily Revenue: ', avg_daily_revenue)
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print('Cuts under 30: ', cuts_under_30)
