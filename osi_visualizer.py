import random
import base64

# --- STEP 1: DISPLAY INFORMATION ---
def display_info():
    student_name = "HEMANT KUMAR"
    matriculation_number = "56010482" 
    
    print("-" * 50)
    print(f"Name: {student_name}")
    print(f"Matriculation Number: {matriculation_number}")
    print("Project Title: Visualizing Data Flow Through the OSI Model")
    print("Subject: IT Platform")
    print("Task: Mini project")
    print("-" * 50)
    print("\n")

# --- STEP 2: APPLICATION LAYER ---
def application_layer(message):
    print(f"\n--- LAYER 7: APPLICATION LAYER ---")
    print(f"Original Message: {message}")
    
    # Simulating a Chat Application using HTTP-like headers [cite: 35, 42]
    headers = (
        "POST /send-message HTTP/1.1\n"
        "Host: chat.example.com\n"
        "Content-Type: text/plain\n"
        f"Content-Length: {len(message)}"
    )
    
    # Combining headers and message
    app_data = f"{headers}\n\n{message}"
    print("Application Layer Output (Data + Headers):")
    print(app_data)
    return app_data

# --- STEP 3: PRESENTATION LAYER ---
def presentation_layer(app_data):
    print(f"\n--- LAYER 6: PRESENTATION LAYER ---")
    
    # 1. Encrypt: Simple reversal for demonstration 
    encrypted_msg = app_data[::-1] 
    
    # 2. Encode: Using UTF-8 (then to Base64 to make it readable printable) 
    # We use base64 here to simulate a distinct encoding format for visualization
    encoded_msg = base64.b64encode(encrypted_msg.encode("utf-8")).decode("utf-8")
    
    print("Presentation Layer Output (Encrypted & Encoded):")
    print(encoded_msg)
    return encoded_msg

# --- STEP 4: SESSION LAYER ---
def session_layer(pres_data):
    print(f"\n--- LAYER 5: SESSION LAYER ---")
    
    # Generate random Session ID
    session_id = str(random.randint(1000, 9999))
    
    # Concatenate Session ID with data 
    session_data = f"SessionID:{session_id};{pres_data}"
    
    print(f"Session ID Generated: {session_id}")
    print("Session Layer Output:")
    print(session_data)
    return session_data

# --- STEP 5: TRANSPORT LAYER ---
def transport_layer(session_data):
    print(f"\n--- LAYER 4: TRANSPORT LAYER ---")
    
    segments = []
    chunk_size = 10
    port = 8080
    
    # Split message into 10-character segments
    raw_segments = [session_data[i:i+chunk_size] for i in range(0, len(session_data), chunk_size)]
    
    print(f"Data split into {len(raw_segments)} segments.")
    
    for idx, segment in enumerate(raw_segments):
        seq_num = idx + 1 
        # Adding Header: Sequence Number + Port + Checksum placeholder [cite: 63, 64]
        transport_segment = f"[SEQ:{seq_num}|PORT:{port}]{segment}"
        segments.append(transport_segment)
        print(f"Segment {seq_num}: {transport_segment}")
        
    return segments

# --- STEP 6: NETWORK LAYER ---
def network_layer(segments):
    print(f"\n--- LAYER 3: NETWORK LAYER ---")
    
    packets = []
    source_ip = "192.168.1.2"  
    dest_ip = "192.168.1.10"  
    
    for segment in segments:
        # Attach IP addresses
        packet = f"[SIP:{source_ip}|DIP:{dest_ip}]{segment}"
        packets.append(packet)
        print(f"Packet: {packet}")
        
    return packets

# --- STEP 7: DATA LINK LAYER ---
def data_link_layer(packets):
    print(f"\n--- LAYER 2: DATA LINK LAYER ---")
    
    frames = []
    source_mac = "AA:BB:CC:DD:EE:01" 
    dest_mac = "FF:GG:HH:II:JJ:02"   
    
    for packet in packets:
        # Add MAC addresses
        frame = f"[SMAC:{source_mac}|DMAC:{dest_mac}]{packet}[trailer]"
        frames.append(frame)
        print(f"Frame: {frame}")
        
    return frames

# --- STEP 8: PHYSICAL LAYER ---
def physical_layer(frames):
    print(f"\n--- LAYER 1: PHYSICAL LAYER ---")
    
    bit_stream = ""
    for frame in frames:
        # Convert frame data to binary 
        binary_data = ' '.join(format(ord(char), '08b') for char in frame)
        bit_stream += binary_data + " " # Adding space between frames
    
    print("[Physical Layer output] Binary Transmission:")
    # Printing a substring to avoid flooding console, as per Example [cite: 82]
    print(bit_stream[:200] + "... (truncated for display)")
    return bit_stream

# --- REVERSE PROCESS (RECEIVER)  ---
def receiver_process(frames):
    print("\n" + "="*50)
    print("RECEIVER SIDE (DECAPSULATION)")
    print("="*50)
    
    # 1. Data Link Decapsulation
    print("\n--- DECAPSULATION: DATA LINK LAYER ---")
    packets = []
    for frame in frames:
        # Remove MACs and trailer
        # Content is between second ']' and last '[' approximately
        # A simpler way given our strict formatting:
        # Strip [SMAC...DMAC] (length 44 approx) and [trailer]
        start_marker = "]" # End of MAC header
        end_marker = "[trailer]"
        
        # Find the first closing bracket corresponding to MAC header
        header_end = frame.find("]") + 1
        # Find the trailer
        trailer_start = frame.find(end_marker)
        
        packet = frame[header_end:trailer_start]
        packets.append(packet)
        print(f"Extracted Packet: {packet}")

    # 2. Network Decapsulation
    print("\n--- DECAPSULATION: NETWORK LAYER ---")
    segments = []
    for packet in packets:
        # Remove IPs. Format: [SIP...DIP]segment
        header_end = packet.find("]") + 1
        segment = packet[header_end:]
        segments.append(segment)
        print(f"Extracted Segment: {segment}")

    # 3. Transport Decapsulation (Reassembly)
    print("\n--- DECAPSULATION: TRANSPORT LAYER ---")
    full_session_data = ""
    # Sort would happen here based on SEQ, but our list is ordered.
    for segment in segments:
        # Remove [SEQ...PORT]
        header_end = segment.find("]") + 1
        data_chunk = segment[header_end:]
        full_session_data += data_chunk
    
    print(f"Reassembled Data: {full_session_data}")

    # 4. Session Decapsulation
    print("\n--- DECAPSULATION: SESSION LAYER ---")
    # Format: SessionID:XXXX;pres_data
    split_point = full_session_data.find(";")
    session_id_info = full_session_data[:split_point]
    pres_data = full_session_data[split_point+1:]
    print(f"Session Info Verified: {session_id_info}")
    print(f"Extracted Presentation Data: {pres_data}")

    # 5. Presentation Decapsulation
    print("\n--- DECAPSULATION: PRESENTATION LAYER ---")
    # Decode Base64/UTF-8
    try:
        decoded_bytes = base64.b64decode(pres_data)
        decrypted_str = decoded_bytes.decode("utf-8")
        # Reverse string (Decryption)
        original_app_data = decrypted_str[::-1]
        print(f"Decoded Data: {original_app_data}")
    except:
        print("Error in decoding.")
        return

    # 6. Application Decapsulation
    print("\n--- DECAPSULATION: APPLICATION LAYER ---")
    # Separate headers from body (Double newline)
    header_end = original_app_data.find("\n\n")
    if header_end != -1:
        final_message = original_app_data[header_end+2:]
        print(f"Final Message Received: {final_message}")
    else:
        print(f"Final Message Received: {original_app_data}")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    display_info()
    
    # 1. User Input
    user_message = input("Enter your message: ")
    
    # --- SENDER SIDE (FORWARD) ---
    app_out = application_layer(user_message)
    pres_out = presentation_layer(app_out)
    sess_out = session_layer(pres_out)
    trans_out = transport_layer(sess_out)
    net_out = network_layer(trans_out)
    data_link_out = data_link_layer(net_out)
    phys_out = physical_layer(data_link_out)
    
    # --- RECEIVER SIDE (BACKWARD) ---
    # We pass the 'data_link_out' (frames) to the receiver to start decapsulation
    receiver_process(data_link_out)