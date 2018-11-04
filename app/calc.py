
def SL(price, units_per_pip, TP_price, SL_price, min_win_ratio, percentage, margin,
			leverage=30, sunken_cost=2.7):
	
	percentage *= 0.01


	# first we see how far from the current price, the SL is
	SL = round(1e4*(abs(SL_price-price)), 1)
	total_pip_to_profit = 1e4*(abs(TP_price-price))

	# this is the number we must calculate with to compensate for 
	# comission and spread
	total_pip_to_loss = SL + sunken_cost

	# then we figure out how much in dollars we're willing to lose
	total_dollar_loss = margin*percentage

	# then we figure out the 'value' of each PIP
	pip_max_value = total_dollar_loss/total_pip_to_loss
	
	# calculate how many units to buy
	total_units_to_buy = pip_max_value * units_per_pip
	total_units_to_buy = int(round(total_units_to_buy, -3))

	# calculate TP w.r.t min_win_ratio
	TP = min_win_ratio * total_dollar_loss / pip_max_value
	TP = round(TP, 1)

	if (TP > total_pip_to_profit):
		print("Not enough money")
		return



	return {'units': total_units_to_buy, 'TP': TP, 'SL': SL}


print(SL(1.0, 1e4, 1.005, 0.9990, 1.5, 1, 1e4))