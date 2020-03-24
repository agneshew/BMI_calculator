print ("Hello in BMI calculator!")

data_valid = False 

while data_valid == False:
    units = int( input("Waht kind of units you choose? 1 - kilos and meters, 2 - pounds and inches "))
    if units < 1 or units > 2:
        print("Please select 1 or 2")
        continue       
    else:
        data_valid = True

data_valid = False

while data_valid == False:        
    weight = input("What is your weight? ")

    try:
        weight = float(weight)
    except:
        print("Invalid value. Use dot.")
        continue
    
    if float(weight) > 1000:
        print("Wrong value")
        continue       
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    height = input("What is your height? ")

    try:
        height = float(height)
    except:
        print("Invalid value. Use dot.")
        continue
    
    if float(height) > 100:
        print("Wrong value")
        continue       
    else:
        data_valid = True
        

bmi_km = float(weight) / (float(height) * float(height))
bmi_pi = (float(weight) / (float(height) * float(height))) * 703

if (units == 1):
    print ("Your BMI is", round(bmi_km, 2)) 
    if (bmi_km < 18.5):
        print ("Underweight")
    elif (bmi_km < 18.5 and bmi_km <= 24.9):
        print ("Normal weight")
    elif (24.9 < bmi_km <= 29.9):
        print ("Overweight")
    else:
        print ("Obesity")
elif (units == 2):
     print ("Your BMI is", round(bmi_pi,2)) 
     if (bmi_pi < 18.5):
        print ("Underweight")
     elif (18.5 < bmi_pi <= 24.9):
        print ("Normal weight")
     elif (24.9 < bmi_pi <= 29.9):
        print ("Overweight")
     else:
        print ("Obesity")

if (units == 1):
    perf_weight1 = 22 * (height * height)
    print ("Your perfect weight is ", round (perf_weight1, 2), "kg")
elif (units == 2):
    perf_weight2 = 22 * (height * height) / 703
    print ("Your perfect weight is ", round (perf_weight2, 2), "pounds")
