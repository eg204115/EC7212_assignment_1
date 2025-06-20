# ---------------------------------------------------------
#   Name : Poornima K.N
#   Reg No: EG/2020/4115
#   Take Home Assignment 1
#   Task 3 : Image Rotation (45° and 90°)
# ---------------------------------------------------------

import cv2
import numpy as np
import os

def rotate_image(image_path, angle):
    """Rotate image by specified angle and save result"""
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not read the image file")
        return False
    
    # Get image dimensions and center
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    
    # Perform rotation
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    
    # Display result
    cv2.imshow(f'Rotated {angle}°', rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save result
    os.makedirs('output_images', exist_ok=True)
    filename = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f'output_images/rotated_{filename}_{angle}deg.png'
    cv2.imwrite(output_path, rotated)
    print(f"Result saved to {output_path}")
    return True

def get_image_path():
    """Get valid image path from user with exit options"""
    while True:
        path = input("\nEnter image path (or 'q' to quit): ").strip()
        if path.lower() == 'q':
            return None
        if os.path.exists(path):
            return path
        print("Error: File not found. Please try again.")

def get_rotation_choice():
    """Get rotation angle choice from user"""
    print("\nAvailable rotation options:")
    print("1. 45° rotation")
    print("2. 90° rotation")
    print("3. Custom angle")
    print("4. Back to image selection")
    
    while True:
        choice = input("Select option (1-4): ").strip()
        if choice == '1':
            return 45
        elif choice == '2':
            return 90
        elif choice == '3':
            while True:
                try:
                    angle = float(input("Enter custom rotation angle (0-360°): "))
                    if 0 <= angle <= 360:
                        return angle
                    print("Please enter an angle between 0 and 360")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '4':
            return None
        else:
            print("Invalid choice. Please enter 1-4")

def main():
    print("\n=== Image Rotation Processor ===")
    print("Rotates images by specified angles")
    
    while True:
        image_path = get_image_path()
        if not image_path:
            break
            
        while True:
            angle = get_rotation_choice()
            if angle is None:
                break
                
            success = rotate_image(image_path, angle)
            if not success:
                break
                
            again = input(f"\nRotate {os.path.basename(image_path)} again? (y/n): ").lower()
            if again != 'y':
                break
    
    print("\nProgram exited. Thank you!")

if __name__ == '__main__':
    main()