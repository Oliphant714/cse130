import random

# Test varying image sizes
image_sizes = [4, 8, 16, 32, 64, 128, 256, 512]

loop_count = 0

# Check each image size for rows with signficant number of white pixels
for image_size in image_sizes:
    white_pixels = 0
    number_of_rows_with_significant_white_pixels = 0

    # Check the entire image
    for x in range(image_size):

        # Reset count at the start of each row
        white_pixels = 0
        for y in range(image_size):
            loop_count += 1
            # Pick a random pixel value
            pixel_value = random.randint(0, 255)

            # Pixel value > 210 is mostly white
            if pixel_value > 210:
                white_pixels += 1

            # A row with 15% or more white pixels is considered significantly white row
            if white_pixels > image_size * 0.15:
                number_of_rows_with_significant_white_pixels += 1
                break

    # Print out the number of rows in this image.
    print(f'image size: {image_size}, number of white rows: {number_of_rows_with_significant_white_pixels}')
    print(loop_count)