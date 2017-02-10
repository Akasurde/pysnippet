equities = {}
for (portfolio, equity) in data:
    if portfolio in equities:
        equities[portfolio].append(equity)
    else:
        equities[portfolio] = [equity]

print(equities)

equities = {}
for (portfolio, equity) in data:
    equities.setdefault(portfolio, []).append(
                                         equity)

