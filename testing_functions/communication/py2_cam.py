# Import necessary libraries
import sys
import cv2
import socket
import numpy as np
from naoqi import ALProxy

# NAO Robot IP and Port
NAO_IP = "172.18.16.27"  # Change to your NAO's IP
NAO_PORT = 9559

PC_HOST = '127.0.0.1'  # The server's hostname or IP address
PC_PORT = 65432        # The port used by the server

sock = None # Initialize sock to None

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

def sock_send_data(audio_data):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Python 2.7 Client: Connecting to {}:{}".format(HOST, PORT)
        sock.connect((HOST, PORT))
        print "Python 2.7 Client: Connected."

        # Send the audio data (already bytes in Py2 'str')
        print "Python 2.7 Client: Sending {} bytes of data...".format(len(audio_data))
        sock.sendall(audio_data)
        print "Python 2.7 Client: Data sent."

        # Optional: Wait for an acknowledgement
        # Give server a moment to process and send back
        sock.settimeout(5.0) # Set a timeout for receiving
        try:
            ack_data = sock.recv(1024) # Returns str (bytes)
            if ack_data:
                # If you expect text, decode it
                print "Python 2.7 Client: Received acknowledgement: '{}'".format(ack_data.decode('utf-8'))
            else:
                print "Python 2.7 Client: Received empty ack (server likely closed connection)."
        except socket.timeout:
            print "Python 2.7 Client: Timeout waiting for acknowledgement."
        except socket.error as e:
            print "Python 2.7 Client: Socket error receiving ack: {}".format(e)


    except socket.error as e:
        print "Python 2.7 Client: Socket error: {}".format(e)
        sys.exit(1)
    except KeyboardInterrupt:
        print "\nPython 2.7 Client: Aborted."
    finally:
        if sock:
            print "Python 2.7 Client: Closing socket."
            sock.close()
        print "Python 2.7 Client: Finished."

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
        # print(img)
        # # Display Image using OpenCV
        # cv2.imshow("NAO Camera", img)

        sock_send_data(img)

        # # Exit on 'q' key
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

finally:
    # Unsubscribe from the camera
    video_proxy.unsubscribe(capture_device)
    # cv2.destroyAllWindows()

