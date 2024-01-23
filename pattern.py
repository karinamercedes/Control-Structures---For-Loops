# Declare control variables
i = 0
star = "*"

for i in range(1 ,10): # Range that define number of rows (excluding 0 as we want to first row to have one star)
    # If condition to have increasing number of stars every row until the fifth row
    if i < 6 :
        print(star * i)
    #Else condition to have decreasing number of stars from the sixth row until the ninth 
    else:
        print(star * (10-i))
# End-of-file (EOF)