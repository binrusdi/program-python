# Assigment Expression adalah langkah untuk menetapkan nilai sekaligus membuat ekpresi dalam satu langkah

# Example Code

# Non Assigment Expression
x = 5
if x > 3:
    print("x lebih besar dari 3: ", x)

# With Assigment Expression
if( y := 5 ) > 3:
    print("y lebih besar dari 3: ", y)

# Assigment Expression dalam loop
numbers = [2, 3, 4, 6, 7, 8]
even_numbers = []
for num in numbers:
    if( result := num % 2 ) == 0:
        even_numbers.append(num)
print(even_numbers)