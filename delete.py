from matplotlib import pyplot as plt


starting = 150000
yearly_increase = 1.07
yearly_contribution = 23500 * 2
years = []
totals = []
current_total = starting
for i in range(38):
    if i == 0:
        pass
    else:
        current_total = current_total * yearly_increase
        current_total += yearly_contribution
        totals.append(current_total / 1e6)
        years.append(i)


plt.plot(years, totals)
plt.grid()
plt.xlabel("Years")
plt.ylabel("Million")
plt.show()
