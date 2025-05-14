import socket
import sys
import time # For demonstration delay

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# --- Assume this part gets the audio data ---
# Example: audio_data = robot_interface.get_audio_chunk()
# For demonstration, let's create some dummy byte data (like audio)
# In Python 2, 'str' is already bytes
audio_data = b'\x01\x02\x03\x04' * 1000 # 4000 bytes of dummy data
audio_data += b'\xEE\xFF' # Add end marker perhaps
# ---

print "Python 2.7 Client: Starting..."

sock = None # Initialize sock to None
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