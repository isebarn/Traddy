
def SL(pair_id, std_lot_profit_per_pip, price, TP_price, SL_price, min_win_ratio, percentage, margin,
			leverage=30, sunken_cost=2.7, pip_scale = 4):

	percentage *= 0.01

	# first we see how far from the current price, the SL is
	SL = abs(SL_price-price)

	# this is the number we must calculate with to compensate for 
	# comission and spread
	total_pip_to_loss = SL + sunken_cost*10**(-pip_scale)

	# then we figure out how much in dollars we're willing to lose
	total_dollar_loss = margin*percentage

	# then we figure out

	total_units_to_buy = round(total_dollar_loss/total_pip_to_loss)

	# calculate TP w.r.t min_win_ratio
	TP = round(abs(TP_price - price) * 10**pip_scale, 1)

	SL = round(total_pip_to_loss*10**pip_scale)

	return {'units': round(total_units_to_buy/1000)*1000, 'TP': TP, 'SL': SL}