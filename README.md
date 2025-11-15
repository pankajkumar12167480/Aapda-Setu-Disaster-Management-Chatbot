# Aapda-Setu-Disaster-Management-Chatbot



🌐 Aapda Setu – Disaster Management & Emergency Response Chatbot

Aapda Setu is an intelligent AI-powered disaster management chatbot designed to help people during emergencies like floods, earthquakes, cyclones, fires, and medical crises.
It provides real-time safety instructions, nearest emergency help, first-aid guidance, and Firebase-based live updates.

🔥 Features
🆘 Emergency Safety Guidance

Flood safety steps

Earthquake survival guide

Cyclone & storm alerts

Fire emergency actions

Landslide & road blockage support

🏥 Nearby Emergency Help

Nearest hospital

Nearest police station

Nearest relief camp

Google Maps location support

📍 Location Awareness

Detects user’s location

Matches with nearest relief center

Shows safe routes & map links

🩺 First-Aid Assistance

CPR

Burns

Bleeding

Fracture handling

Choking management

🔥 Firebase Integration

Stores user queries

Saves incident reports

Fetches hospital/relief center data

Real-time database updates

🤖 Smart AI Response

NLP-based understanding

Intent classification

Contextual replies

Calm, helpful tone

🏗️ Tech Stack

Flutter / React / HTML (Frontend)

Python / Node.js / Firebase Functions (Backend)

Firebase Realtime Database / Firestore

TensorFlow / Scikit-learn (ML Model)

Dialogflow / Custom NLP Model

Google Maps API (Location services)

📂 Project Structure
Aapda-Setu/
│
├── backend/
│   ├── model/
│   ├── intents.json
│   ├── app.py / index.js
│
├── app/
│   ├── lib/
│   ├── assets/
│   ├── screens/
│
├── firebase/
│   ├── database rules
│   ├── relief_centers.json
│
└── README.md

🧠 How It Works

User sends a message (e.g., “Flood water entering my home”).

NLP model detects the intent (Flood Safety).

Bot provides step-by-step safety instructions.

If location is shared → finds nearest relief center from Firebase.

Stores incident in Firebase for admin dashboard.

🧪 Sample Query & Response

User: “What should I do during an earthquake?”
Bot:

Drop, Cover, Hold

Stay away from windows

If outdoors, move to open space

If you need nearby shelters, share your location

🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/yourusername/aapda-setu.git
cd aapda-setu

2️⃣ Install Dependencies

For Python:

pip install -r requirements.txt


For Node.js:

npm install

3️⃣ Run Backend
python app.py


or

node index.js

4️⃣ Setup Firebase

Add your Firebase API keys

Upload relief_centers.json

Enable Real-Time Database

5️⃣ Run Frontend

Flutter:

flutter run

📦 Firebase Database Structure
/users/
/disasters/
/relief_centers/
/emergency_reports/

🛡️ Safety & Reliability

Aapda Setu follows:
✔ Real-time disaster guidelines
✔ Verified first-aid steps
✔ Accurate mapping & shelter suggestions

🤝 Contributing

Want to contribute? Great!

Fork the repo

Create a feature branch

Submit a pull request

📜 License

This project is licensed under the MIT License.

❤️ Support

If you like this project, don’t forget to ⭐ star the repository!

For queries:
📧 pankajkumargupta12167480@gmail.com
