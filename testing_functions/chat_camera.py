# Import necessary libraries
import sys
import numpy as np
from naoqi import ALProxy
from PIL import Image

# NAO Robot IP and Port
NAO_IP = "172.18.16.54"  # Change to your NAO's IP
PORT = 9559

# Connect to ALVideoDevice
video_proxy = ALProxy("ALVideoDevice", NAO_IP, PORT)

# Subscribe to the camera
camera_name = "python_camera"
resolution = 2  # 640x480
color_space = 11  # RGB
fps = 10  # Frames per second
camera_id = 0  # 0 for Top Camera, 1 for Bottom Camera

# Subscribe to a video feed
capture_device = video_proxy.subscribeCamera(camera_name, camera_id, resolution, color_space, fps)

# Display the video feed
try:
    while True:
        # Get Image
        nao_image = video_proxy.getImageRemote(capture_device)

        # Extract Image Data
        width = nao_image[0]
        height = nao_image[1]
        array = nao_image[6]

        # Convert byte array to numpy array
        img = np.frombuffer(array, dtype=np.uint8).reshape((height, width, 3))
        pil_image = Image.fromarray(img)
        print(img)
        pil_image.save('out.jpg')
        # # Display Image using OpenCV
        # cv2.imshow("NAO Camera", img)

        # # Exit on 'q' key
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

finally:
    # Unsubscribe from the camera
    video_proxy.unsubscribe(capture_device)
    # cv2.destroyAllWindows()
