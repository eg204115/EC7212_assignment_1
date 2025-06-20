# ---------------------------------------------------------
#   Name : Poornima K.N
#   Reg No: EG/2020/4115
#   Take Home Assignment 1
#   Task 2 : Spatial averaging with 3x3, 10x10, and 20x20 kernels 
# ---------------------------------------------------------

import cv2
import numpy as np
import os

def spatial_averaging(image_path, kernel_size):
    """Apply spatial averaging with given kernel size"""
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not read the image file")
        return False
    
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    averaged = cv2.filter2D(img, -1, kernel)
    
    # Display result
    cv2.imshow(f'{kernel_size}x{kernel_size} Averaging', averaged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save result
    os.makedirs('output_images', exist_ok=True)
    filename = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f'output_images/avg_{filename}_{kernel_size}x{kernel_size}.png'
    cv2.imwrite(output_path, averaged)
    print(f"Result saved to {output_path}")
    return True

def get_image_path():
    """Get valid image path from user"""
    while True:
        path = input("\nEnter image path (or 'q' to quit): ").strip()
        if path.lower() == 'q':
            return None
        if os.path.exists(path):
            return path
        print("Error: File not found. Please try again.")

def get_kernel_choice():
    """Get kernel size choice from user"""
    print("\nAvailable kernel sizes:")
    print("1. 3x3 (Light blur)")
    print("2. 10x10 (Medium blur)")
    print("3. 20x20 (Heavy blur)")
    print("4. Custom kernel size")
    print("5. Back to image selection")
    
    while True:
        choice = input("Select option (1-5): ").strip()
        if choice in ['1', '2', '3']:
            return [3, 10, 20][int(choice)-1]
        elif choice == '4':
            while True:
                try:
                    size = int(input("Enter custom kernel size (odd number): "))
                    if size > 0 and size % 2 == 1:
                        return size
                    print("Please enter a positive odd number")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '5':
            return None
        else:
            print("Invalid choice. Please enter 1-5")

def main():
    print("\n=== Spatial Averaging Processor ===")
    print("Applies averaging filters to images")
    
    while True:
        image_path = get_image_path()
        if not image_path:
            break
            
        while True:
            kernel_size = get_kernel_choice()
            if not kernel_size:
                break
                
            success = spatial_averaging(image_path, kernel_size)
            if not success:
                break
                
            again = input(f"\nProcess {os.path.basename(image_path)} with another kernel? (y/n): ").lower()
            if again != 'y':
                break
    
    print("\nProgram exited. Thank you!")

if __name__ == '__main__':
    main()