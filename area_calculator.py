import math

def calculate_square_area():
    sides = float(input("Enter the side length of the square: "))
    area = sides ** 2
    print(f"The area of your square is {area}.")

def calculate_rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of your rectangle is {area}.")

def calculate_triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of your triangle is {area}.")

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14159 * radius ** 2  # Approximation for π
    print(f"The area of your circle is {area}.")

def main():
    print("==================\n" + "Area Calculator 📐\n" + "==================")

    while True:
        try:
            shapes_input = int(input("Choose one operation to perform (1-4): \n"
                                     "1) Square\n"
                                     "2) Rectangle\n"
                                     "3) Triangle\n"
                                     "4) Circle\n"))

            if shapes_input == 1:
                calculate_square_area()
            elif shapes_input == 2:
                calculate_rectangle_area()
            elif shapes_input == 3:
                calculate_triangle_area()
            elif shapes_input == 4:
                calculate_circle_area()
            else:
                print("Please choose a valid option (1-4).")
                continue
            break  # Exit the loop if a valid option was selected

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()


