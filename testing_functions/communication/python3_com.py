import socket
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

print("Python 3 Server: Starting...")

# Use 'with' statement for automatic socket closing
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Python 3 Server: Listening on {}:{}".format(HOST, PORT))

        conn, addr = s.accept() # Blocks until a client connects
        with conn:
            print('Python 3 Server: Connected by', addr)
            total_data = b'' # Use bytes object to accumulate data
            while True:
                try:
                    # Receive data (returns bytes)
                    data = conn.recv(1024) # Receive up to 1024 bytes
                    if not data:
                        # If recv returns empty bytes object, client closed connection
                        print("Python 3 Server: Client closed connection.")
                        break
                    print("Python 3 Server: Received {} bytes.".format(len(data)))
                    # In a real app, process or save the 'data' bytes here
                    # For audio, you'd append 'data' to a buffer or file
                    total_data += data

                    # Example: Send an acknowledgement back (must be bytes)
                    ack_message = "Data received".encode('utf-8') # Encode string to bytes
                    conn.sendall(ack_message)

                except socket.error as e:
                    print("Python 3 Server: Socket error during recv/send: {}".format(e))
                    break
                except Exception as e:
                     print("Python 3 Server: Error receiving data: {}".format(e))
                     break

            print("Python 3 Server: Total data received: {} bytes".format(len(total_data)))
            # Process total_data here (e.g., give to vLLM/STT library)
            print("Python 3 Server: Processing received data...")
            # result = your_processing_function(total_data)
            # print("Python 3 Server: Processing result:", result)

except socket.error as e:
    print("Python 3 Server: Socket error during setup: {}".format(e))
    sys.exit(1)
except KeyboardInterrupt:
     print("\nPython 3 Server: Shutting down.")
finally:
    print("Python 3 Server: Finished.")