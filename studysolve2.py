#Data
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
# calculating profit (revenue - expenses)
profit= list([])
for i in range (0, len(revenue)):
 profit.append(revenue[i]- expenses[i])
print(profit)
#calculating tax (profit * 30%)
tax= [round(i*0.3,2)for i in profit]
print(tax)

#profit after tax
profit_after_tax = list([])

for i in range(0,len(profit)):
 profit_after_tax.append(profit[i]-tax[i])
 print(profit_after_tax)

#profit margin after tax
 profit_margin = list([])

for i in range(0,len(profit)):
  profit_margin.append(profit_after_tax[i]/revenue[i])

profit_margin = [round((i*100),2) for i in profit_margin]
print(profit_margin)

# profit after tax mean
mean_pat = sum(profit_after_tax)/ len(profit_after_tax)
print(mean_pat)

#good month
good_months= list([])
for i in range(0, len(profit)):
    good_months.append(profit_after_tax[i] > mean_pat)
print(good_months)

#bad month
bad_months= list([])
for i in range(0, len(profit)):
    bad_months.append(profit_after_tax[i] > mean_pat)
print(bad_months)

best_month= list([])
for i in range90,len(profit):
    best_month.append(profit_after_tax[i]==max(profit_after_tax))
print(best_month)

worse_month= list([])
for i in range(0, len(profit)):
    worse_month.append(profit_after_tax[i]==min(profit_after_tax))
print(worse_month)
