# ---------------------------------------------------------
#   Name : Poornima K.N
#   Reg No: EG/2020/4115
#   Take Home Assignment 1
#   Task 1 : Reducing intensity levels from 256 to powers of 2 
# ---------------------------------------------------------

import cv2
import numpy as np
import os

def reduce_intensity_levels(image_path, levels):
    """Reduce image intensity levels and save the result"""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Error: Could not read the image file")
        return
    
    scale = 256 / levels
    reduced = (img // scale) * scale

    # Display the result
    cv2.imshow(f'Reduced to {levels} levels', reduced)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the result
    os.makedirs('output_images', exist_ok=True)
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f'output_images/intensity_reduced_{image_name}_{levels}.png'
    cv2.imwrite(output_path, reduced)
    print(f"Image saved as {output_path}")

def get_image_path():
    """Get valid image path from user"""
    while True:
        path = input("\nEnter image path (or 'q' to quit): ").strip()
        if path.lower() == 'q':
            return None
        try:
            with open(path, 'rb') as f:
                return path
        except FileNotFoundError:
            print("Error: File not found. Please try again.")

def get_intensity_levels():
    """Get valid intensity levels from user"""
    while True:
        level_input = input("Enter intensity levels (2,4,8,16... or 'b' to go back): ").strip()
        
        if level_input.lower() == 'b':
            return None
            
        try:
            levels = int(level_input)
            if levels > 1 and (levels & (levels - 1)) == 0:  # Check if power of 2
                return levels
            print("Please enter a power of 2 (2, 4, 8, 16, etc.)")
        except ValueError:
            print("Invalid input. Please enter a number or 'b' to go back.")

def process_single_image(image_path):
    """Process one image with multiple intensity levels"""
    while True:
        print(f"\nCurrent image: {os.path.basename(image_path)}")
        print("1. Process with new intensity level")
        print("2. Choose different image")
        print("3. Exit program")
        
        choice = input("Select option (1-3): ").strip()
        
        if choice == '1':
            levels = get_intensity_levels()
            if levels:
                reduce_intensity_levels(image_path, levels)
        elif choice == '2':
            return True  # Signal to choose new image
        elif choice == '3':
            return False  # Signal to exit
        else:
            print("Invalid choice. Please enter 1, 2, or 3")

def main():
    print("\n=== Image Intensity Reduction Program ===")
    print("Reduces grayscale images to specified intensity levels")
    
    while True:
        image_path = get_image_path()
        if not image_path:  # User entered 'q' to quit
            break
            
        continue_processing = process_single_image(image_path)
        if not continue_processing:
            break
            
    print("\nProgram exited. Goodbye!")

if __name__ == '__main__':
    main()