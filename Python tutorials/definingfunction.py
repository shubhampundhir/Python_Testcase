def calculate_total(exp):   #function arguement
    total = 0
    for item in exp:
        total = total + item
    return total   #return value

tom_total_exp = [2100,3440,2300]
joe_total_exp = [2200,3700,2400]

toms_total = calculate_total(tom_total_exp)#function call
joes_total = calculate_total(joe_total_exp)#function call

print("tom's total expenses:",toms_total) #call function and pass the list of tom's total expenses to local variabe exp.
print("joe's total expenses:",joes_total)#call function and pass the value of joe's total expenses to local variable exp.


#total = 0
#for item in tom_total_exp:
#    total = total + item
#   print("tom's total exp: ",total)

#total = 0
#for item in joe_total_exp:
#    total = total + item
#    print("joe's total exp: ",total)


