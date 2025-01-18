''' 5. A transport company charges the fare according to following table:

   Distance   Charges
   1-50       8 Rs./Km
   51-100     10 Rs./Km

   > 100      12 Rs/Km   '''

# Input the distance traveled
distance = int(input("Enter the distance traveled (in km): "))

# Calculate the fare based on the distance
if distance <= 50:
    fare = distance * 8
elif distance <= 100:
    fare = (50 * 8) + (distance - 50) * 10
else:
    fare = (50 * 8) + (50 * 10) + (distance - 100) * 12

# Print the total fare
print(f"The total fare is: Rs. {fare}")

