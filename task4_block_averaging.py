# ---------------------------------------------------------
#   Name : Poornima K.N
#   Reg No: EG/2020/4115
#   Take Home Assignment 1
#   Task 4 : Block Averaging for Resolution Reduction
# ---------------------------------------------------------

import cv2
import numpy as np
import os

def block_averaging(image_path, block_size):
    """Apply block averaging to reduce image resolution"""
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not read the image file")
        return False
    
    # Get and adjust image dimensions
    h, w = img.shape[:2]
    new_h = h - h % block_size
    new_w = w - w % block_size
    img = img[:new_h, :new_w]
    
    # Process blocks
    blocks = img.reshape(new_h//block_size, block_size, 
                        new_w//block_size, block_size, -1)
    averaged = blocks.mean(axis=(1, 3)).astype(np.uint8)
    result = cv2.resize(averaged, (new_w, new_h), 
                      interpolation=cv2.INTER_NEAREST)
    
    # Display result
    cv2.imshow(f'{block_size}x{block_size} Block Averaging', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save result
    os.makedirs('output_images', exist_ok=True)
    filename = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f'output_images/block_avg_{filename}_{block_size}x{block_size}.png'
    cv2.imwrite(output_path, result)
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

def get_block_size():
    """Get block size choice from user"""
    print("\nAvailable block sizes:")
    print("1. 3x3 blocks")
    print("2. 5x5 blocks")
    print("3. 7x7 blocks")
    print("4. Custom block size")
    print("5. Back to image selection")
    print("6. Exit program")
    
    while True:
        choice = input("Select option (1-6): ").strip()
        if choice in ['1', '2', '3']:
            return [3, 5, 7][int(choice)-1]
        elif choice == '4':
            while True:
                try:
                    size = int(input("Enter block size (odd number ≥3): "))
                    if size >= 3 and size % 2 == 1:
                        return size
                    print("Please enter an odd number ≥3")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '5':
            return None
        elif choice == '6':
            return 'exit'
        else:
            print("Invalid choice. Please enter 1-6")

def main():
    print("\n=== Block Averaging Processor ===")
    print("Reduces image resolution using block averaging")
    print("Instructions:")
    print("- Enter 'q' at any time to go back")
    print("- Select option 6 to exit the program")
    
    while True:
        image_path = get_image_path()
        if not image_path:
            break
            
        while True:
            block_size = get_block_size()
            if block_size == 'exit':
                print("\nProgram exited. Thank you!")
                return
            if not block_size:
                break
                
            success = block_averaging(image_path, block_size)
            if not success:
                break
                
            again = input(f"\nProcess {os.path.basename(image_path)} with another block size? (y/n): ").lower()
            if again != 'y':
                break
    
    print("\nProgram exited. Thank you!")

if __name__ == '__main__':
    main()