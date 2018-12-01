year = [1955, 1956, 1957, 1958, 1959]
num = [450, 495, 518, 563, 584]
sum_num = sum(num)
sum_year = sum(year)
sum_year_2 = 0
sum_num_year = 0
for i in year:
    sum_year_2 += i**2
for i in range(len(year)):
    num1 = year[i]
    num2 = num[i]
    num3 = num1*num2
    print(i)
    sum_num_year += num3
print(sum_year, sum_num, sum_year_2, sum_num_year)

b = ((len(year)*sum_num_year)-(sum_year*sum_num))/\
((len(year)*sum_year_2)-(sum_year**2))
print(len(year))
a = ((sum_num)-(b*sum_year))/(len(year))
print(a)
print("y = %.2f + %.2f(n)" %(a, b))
z = a + (b*int(input()))
print("%.2f" %(z))