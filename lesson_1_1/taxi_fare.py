start_charge = 3
mile_cost = 3.5
minute_cost = 0.7
fixed_surcharges = 0.5 + 1 + 2.5
miles = float(input("What are running miles? "))
minutes = float(input("What are slow minutes? "))
tip_percent = int(input("What is tip percent? "))
meter_fare = start_charge + (miles * mile_cost) + (minutes * minute_cost)
tip = meter_fare * (tip_percent / 100)
total = fixed_surcharges + meter_fare + tip
print(f"Meter fare:           ${meter_fare:.2f}")
print(f"Surcharges:           ${fixed_surcharges:.2f}")
print(f"Tip ({tip_percent}%):            ${tip:.2f}")
print(f"TOTAL:                ${total:.2f}")
price_per_mile = total / miles
price_per_km = price_per_mile / 1.60934
print(f"Price per mile:       ${price_per_mile:.2f}")
print(f"Price per km:         ${price_per_km:.2f}")
