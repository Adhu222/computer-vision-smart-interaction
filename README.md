# 🎥 Computer Vision for Smart Interaction (YOLOv8 + Flask + React)

This project is an **AI-powered object detection system** that allows users to upload images and detect objects in real-time. It uses **YOLOv8 for object detection**, **Flask for backend processing**, and **React for the frontend UI**.

---

## 📌 **Project Features**
✅ Detects objects in images using **YOLOv8 (pretrained model)**  
✅ Provides a **web-based UI** for uploading images (React)  
✅ Processes images in **real-time using Flask**  
✅ Displays detected objects with bounding boxes  
✅ No dataset required (uses a pretrained YOLOv8 model)  

---

## 📂 **Project Folder Structure**
```
📦 computer-vision-smart-interaction
├── backend/                     # Flask Backend (Object Detection API)
│   ├── main.py                  # Flask API for image processing
│   ├── object_detection.py       # YOLOv8 model for detecting objects
│   ├── requirements.txt          # Backend dependencies
│   ├── static/                   # Stores processed images/videos (Auto-filled)
│   ├── models/                   # Stores YOLOv8 pre-trained model (Manually add)
│   ├── uploads/                  # Stores uploaded images/videos (Auto-filled)
│
├── frontend/                     # React Frontend (User Interface)
│   ├── src/
│   │   ├── App.js                # React UI logic
│   │   ├── index.js              # React entry point
│   │   ├── styles.css            # Styling for UI
│   ├── public/
│   │   ├── index.html            # Base HTML file
│   ├── package.json              # React dependencies
│   ├── node_modules/             # Auto-generated after npm install (Do NOT upload to GitHub)
│
├── README.md                     # Project Documentation
```

---

## 🛠 **Libraries & Technologies Used**

### **Backend (Flask & YOLOv8)**
| Library | Purpose |
|---------|---------|
| `Flask` | Backend server for handling API requests |
| `ultralytics` | YOLOv8 object detection model |
| `opencv-python` | Image processing |
| `numpy` | Mathematical operations |
| `requests` | HTTP requests |

### **Frontend (React)**
| Library | Purpose |
|---------|---------|
| `React` | Web UI framework |
| `Axios` | Sends API requests to Flask |

---

##  **Installation & Setup**

### **1️⃣ Install Backend Dependencies**
📌 Open a terminal inside `backend/` and run:
```bash
cd backend
pip install -r requirements.txt
```

### **2️⃣ Start the Flask Backend**
```bash
python main.py
```
✅ The Flask server should start at **http://localhost:5000**

---

### **3️⃣ Install Frontend Dependencies**
📌 Open another terminal inside `frontend/` and run:
```bash
cd frontend
npm install
```

### **4️⃣ Start the React Frontend**
```bash
npm start
```
✅ The React app should open at **http://localhost:3000**

---

##  **How to Use the Application**

1️⃣ Open **http://localhost:3000/** in your browser.  
2️⃣ Click **"Choose File"**, select an image, and click **Upload**.  
3️⃣ The processed image with detected objects will be displayed.  

---

## 📌 **Troubleshooting Errors**

### ❌ `ModuleNotFoundError: No module named 'requests'`
✅ Run:
```bash
pip install requests
```

### ❌ `npm: command not found`
✅ Install **Node.js** and verify:
```bash
node -v
npm -v
```

### ❌ `Flask server not running`
✅ Ensure Flask is installed and run:
```bash
python main.py
```

---

## 📜 **License**
This project is open-source. Feel free to use and modify it! 🚀
