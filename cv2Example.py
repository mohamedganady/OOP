import cv2
import numpy as np

class PolylineManager:
    def __init__(self):
        self.points = []  # List to store polyline points

    def add_point(self, point):
        """Add a point to the current polyline."""
        self.points.append(point)
        print(f"Point added: {point}")

    def draw_polyline(self, image):
        """Draw the polyline on the image."""
        if len(self.points) > 1:
            for i in range(1, len(self.points)):
                cv2.line(image, self.points[i-1], self.points[i], (0, 255, 0), 2)
        for point in self.points:
            cv2.circle(image, point, 5, (0, 0, 255), -1)  #cv2.circle(image, center, radius, color, thickness)

# Instantiate the PolylineManager
polyline_manager = PolylineManager()

# Mouse callback function to capture points on left mouse click
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Add point on left mouse click
        polyline_manager.add_point((x, y))

# Set up OpenCV window and register the mouse callback
cv2.namedWindow("Polyline Drawer")
cv2.setMouseCallback("Polyline Drawer", RGB)

# Main loop to display the image and draw polyline
image = 255 * np.ones((500, 500, 3), dtype=np.uint8)  # Create a white image

while True:
    display_image = image.copy()  # Copy image to avoid modifying the original
    polyline_manager.draw_polyline(display_image)  # Draw the polyline on the copied image

    cv2.imshow("Polyline Drawer", display_image)  # Show the image with polyline

    # Exit loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
