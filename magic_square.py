# MAGIC SQUARE CREATION 

# A magic square is a square matrix of distinct numbers in which the sum of the numbers in each row , column and diagonal is the same.


""" Creating magic square of N*N where N is Odd Number ."""

def magic_square_creation(n) :
    square=[[0]*n for _ in range(n)]     # Initializing an N x N grid filled with zeros


    a,b=0,n//2  # Starting Position :- North-East (Up-Right) from the middle of the top row



#  Starting loop through numbers 1 to n*n for filling magic square
# Calculating New Position :- Move North-East (Up-Right)
    for num in range(1,n*n+1) :

        square[a][b] = num # Current number at  position (a,b)
        new_a,newb = (a-1)%n,(b+1)%n  # New Position [North-East movement, wrapping around if needed]

        if square[new_a][newb]:  # if the new position is filled move down instead (to avoid overlap)
            a+=1 # Move Down :- South

        else : 
            a,b=new_a,newb  # Otherwise Moved to new calculated position
    return square



# Printing the magic square (Function).
def printing_magic_square(square) :

# Proper Formating Printing
    for row in square :
        print(" ".join(f"{num:2}"for num in row)) # Indentation :- Width=2

# Input from the user

order=int(input("Enter the order of the Magic Square (The Number Should Be 'ODD' Number) -->  "))
if order%2==1:  # Ensuring That number is 'ODD'
    square=magic_square_creation(order)

    print("\nMagic Square --> ") # HEADER
    printing_magic_square(square)      # Printing the Magic Square
else:                                        # If the number is not 'ODD'
    print("Please enter an odd number for creating magic square .")
