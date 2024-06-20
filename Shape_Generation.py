# Import necessary modules
import random  # For generating random numbers
import os  # For creating directories and interacting with the file system
import csv  # For reading and writing CSV files
from PIL import Image, ImageDraw  # For creating and drawing on images

# Create a directory named "result" if it doesn't already exist
os.makedirs("result", exist_ok=True)

# Define the dimensions of the images
width, height = 100, 100

# Function to generate a filename for the images
def generate_filename(number):
    return f'result/random_shapes_{number}.png'

# Function to draw a random circle on the given drawing context
def draw_random_circle(draw):
    diameter = random.randint(10, 50)  # Random diameter between 10 and 50
    x = random.randint(0, width - diameter)  # Random x coordinate
    y = random.randint(0, height - diameter)  # Random y coordinate
    x_min, y_min = x, y  # Top-left corner of the circle
    x_max, y_max = x + diameter, y + diameter  # Bottom-right corner of the circle
    outline_width = random.randint(1, 3)  # Random outline width between 1 and 3
    draw.ellipse([x_min, y_min, x_max, y_max], outline='black', width=outline_width)  # Draw the circle
    return x_min, y_min, x_max, y_max  # Return the coordinates

# Function to draw a random rectangle on the given drawing context
def draw_random_rectangle(draw):
    rect_width = random.randint(10, 50)  # Random width between 10 and 50
    rect_height = random.randint(10, 50)  # Random height between 10 and 50
    x = random.randint(0, width - rect_width)  # Random x coordinate
    y = random.randint(0, height - rect_height)  # Random y coordinate
    x_min, y_min = x, y  # Top-left corner of the rectangle
    x_max, y_max = x + rect_width, y + rect_height  # Bottom-right corner of the rectangle
    outline_width = random.randint(1, 3)  # Random outline width between 1 and 3
    draw.rectangle([x_min, y_min, x_max, y_max], outline='black', width=outline_width)  # Draw the rectangle
    return x_min, y_min, x_max, y_max  # Return the coordinates

# Function to draw a random triangle on the given drawing context
def draw_random_triangle(draw):
    # Random coordinates for the three vertices of the triangle
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    x3 = random.randint(0, width)
    y3 = random.randint(0, height)
    # Ensure that all coordinates are within the image bounds
    while any(coord < 0 or coord > 100 for coord in [x1, y1, x2, y2, x3, y3]):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        x3 = random.randint(0, width)
        y3 = random.randint(0, height)
    outline_width = random.randint(1, 3)  # Random outline width between 1 and 3
    draw.polygon([x1, y1, x2, y2, x3, y3], outline='black', width=outline_width)  # Draw the triangle
    # Determine the bounding box of the triangle
    x_min = min(x1, x2, x3)
    y_min = min(y1, y2, y3)
    x_max = max(x1, x2, x3)
    y_max = max(y1, y2, y3)
    return x_min, y_min, x_max, y_max  # Return the coordinates

# Open a CSV file for writing annotation data
with open('annotations.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['filename', 'x_min', 'y_min', 'x_max', 'y_max', 'class_id'])

    # Generate 1000 images
    for i in range(1, 1001):
        image = Image.new('RGB', (width, height), 'white')  # Create a new white image
        draw = ImageDraw.Draw(image)  # Create a drawing context

        shape_count = random.randint(1, 3)  # Random number of shapes to draw
        for _ in range(shape_count):
            shape_type = random.choice(['circle', 'rectangle', 'triangle'])  # Randomly choose a shape
            if shape_type == 'circle':
                x_min, y_min, x_max, y_max = draw_random_circle(draw)  # Draw a circle
            elif shape_type == 'rectangle':
                x_min, y_min, x_max, y_max = draw_random_rectangle(draw)  # Draw a rectangle
            elif shape_type == 'triangle':
                x_min, y_min, x_max, y_max = draw_random_triangle(draw)  # Draw a triangle

            # Write the annotation data to the CSV file
            writer.writerow([generate_filename(i), x_min, y_min, x_max, y_max, shape_type])

        filename = generate_filename(i)  # Generate the filename for the image
        image.save(filename, 'PNG')  # Save the image

# Mapping of shape types to class IDs
shape_class_mapping = {
    'circle': 0,
    'rectangle': 1,
    'triangle': 2
}

# Open a CSV file for writing shape counts
with open('shape_counts.csv', 'w', newline='') as shape_counts_file:
    shape_counts_writer = csv.writer(shape_counts_file)
    # Write the header row
    shape_counts_writer.writerow(['image_filename', 'circle_count', 'rectangle_count', 'triangle_count'])
    for i in range(1, 1001):
        # Initialize shape counts
        circle_count = 0
        rectangle_count = 0
        triangle_count = 0
        with open('annotations.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == generate_filename(i):  # Check if the row corresponds to the current image
                    if row[5] == 'circle':
                        circle_count += 1  # Increment circle count
                    elif row[5] == 'rectangle':
                        rectangle_count += 1  # Increment rectangle count
                    elif row[5] == 'triangle':
                        triangle_count += 1  # Increment triangle count
        # Write the shape counts to the CSV file
        shape_counts_writer.writerow([generate_filename(i), circle_count, rectangle_count, triangle_count])
