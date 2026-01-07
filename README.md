# 📡 Visualizing Data Flow Through the OSI Model

A Python-based mini project that simulates and visualizes how data flows through all 7 layers of the OSI model, including encapsulation and decapsulation on both sender and receiver sides.

This project is built for educational purposes to help understand networking concepts in a practical and visual manner.

---

## 🧑‍🎓 Student Information

- **Name:** Hemant Kumar 
- **Subject:** IT Platform  
- **Project Type:** Mini Project  

---

## 🧠 Project Objective

The objective of this project is to:
- Demonstrate data encapsulation through OSI layers (Layer 7 → Layer 1)
- Simulate data transmission
- Demonstrate decapsulation on the receiver side (Layer 1 → Layer 7)
- Help students visualize OSI model concepts clearly

---

## 🏗️ OSI Model Layers Implemented

| Layer | Name | Description |
|------|------|-------------|
| 7 | Application | Adds HTTP-like headers and message |
| 6 | Presentation | Encrypts and encodes data (Base64) |
| 5 | Session | Creates and attaches a session ID |
| 4 | Transport | Splits data into segments with sequence numbers |
| 3 | Network | Adds source and destination IP addresses |
| 2 | Data Link | Frames data using MAC addresses |
| 1 | Physical | Converts frames into binary data |

---

## 🔄 Project Workflow

### Sender Side (Encapsulation)
1. User inputs a message
2. Data passes through all OSI layers
3. Each layer adds its own headers/trailers
4. Final output is converted to binary for transmission

### Receiver Side (Decapsulation)
1. Binary data is received as frames
2. Headers are removed layer by layer
3. Data is reassembled
4. Original message is retrieved

---

## 🛠️ Technologies Used

- **Python 3**
- Standard libraries:
  - `random`
  - `base64`

No external dependencies required.

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/osi-model-visualization.git
