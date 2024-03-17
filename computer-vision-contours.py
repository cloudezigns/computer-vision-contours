import cv2
import numpy as np

try:
    # Load the image
    image = cv2.imread('/Users/ktamobile/Python/First-Python-Scripts/shapes.jpg')

    # Check if the image was successfully loaded
    if image is None:
        print("Error: Unable to load image.")
        exit(1)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find Canny edges
    edged = cv2.Canny(gray, 30, 200)

    # Finding Contours
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Display the Canny edges image
    cv2.imshow('Canny Edges After Contouring', edged)
    cv2.waitKey(0)

    print("Number of Contours found = " + str(len(contours)))

    # Draw all contours
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    # Display the image with contours
    cv2.imshow('Contours', image)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()

except Exception as e:
    print("An error occurred:", e)

