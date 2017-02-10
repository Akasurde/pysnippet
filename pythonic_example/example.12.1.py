data = [('RIL', 12, 1), ('REDHAT', 123, 2)]
prices = { 12: 1000, 123: 10000}
navs = {}
for (portfolio, equity, position) in data:
    navs.setdefault(portfolio, 0)
    navs[portfolio] += position * prices[equity]
print(navs)
