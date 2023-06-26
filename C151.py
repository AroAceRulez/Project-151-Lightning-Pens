
months = ("January", "February", "March", "April", "May", "June", 
         "July", "August", "September", "October", "November", "December")

profits = (1200, 1000000, 7981, 7874999, 9748163, 7656548, 978456726, 375957, 734687, 982349, 67345234, 897871457134)

print(len(profits))

max_p= max(profits)
index_max_p= profits.index(max_p)
month_max= months[index_max_p]

print ("The maximum profit of", max_p, "was made in the month of ", month_max)


min_p= min(profits)
index_min_p= profits.index(min_p)
month_min= months[index_min_p]

print ("The minimum profit of", min_p, "was made in the month of ", month_min)