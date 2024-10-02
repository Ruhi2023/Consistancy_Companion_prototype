# Consistancy_Companion_prototype
Here's the updated `README.md` with GitHub-style markdown, including the mention of the `.bat` file:

---

# Consistency Companion Prototype

A companion to help you test what you’ve learned, improve through suggestions, and track your progress. It also includes a simulated friend chat feature for mental peace during your journey.

## Requirements

To run this project successfully, please ensure the following dependencies are installed:

### 1. MySQL Workbench
- Install MySQL and MySQL Workbench to handle the database for tracking progress and storing ideas.
- **Installation Guide:**
  - Visit [MySQL Workbench Download](https://dev.mysql.com/downloads/workbench/) and download the installer suitable for your OS.
  - Follow the installation steps provided by the installer.
  - Once installed, configure your MySQL Workbench connection by setting up a new MySQL server instance.
- **Adjustments:**
  After setting up MySQL, make necessary adjustments in the `Consistency_tables.py` file to ensure it connects to your MySQL database (e.g., database name, user credentials).

### 2. Python & Required Libraries
Ensure Python is installed on your machine along with the following libraries:

- **MySQL Connector Python 9.0.0**
  Install via:
  ```bash
  pip install mysql-connector-python==9.0.0
  ```

- **Streamlit**
  Install via:
  ```bash
  pip install streamlit
  ```

### 3. Gemini API Key
To fully leverage all the features, including AI-driven procedures and suggestions, you’ll need a Gemini API key. You can obtain one by signing up on the official Gemini platform.

### 4. `.bat` File for Easy Execution
For convenience, a `.bat` file is included in the repository. Running this file will set up the necessary environment and launch the Streamlit app. Simply double-click the `.bat` file, and the app will start without needing to run commands manually.

---

## Features

### 1. Testing Interface for Learning
The app provides an interface for you to test your knowledge on topics you’ve recently learned or projects you’ve created. It helps you reflect on what you've achieved and offers continuous improvement suggestions.

### 2. Improvement Suggestions
Tracks your learning progress and provides actionable improvement suggestions based on your test results. Past suggestions are logged and tailored to your performance.

### 3. Motivational Tracking
The app tracks your accomplishments over the past 20 days to keep you motivated and reminds you of your progress.

### 4. Virtual Friend Chat
You can create a virtual friend by describing their characteristics, or use an existing one. The chat simulates friendly conversation and remembers up to 4 previous conversations for continuity. This feature is designed to provide mental peace and personalized encouragement.

### 5. Idea Tracking System
The built-in idea tracking system lets you log your ideas into the database. You can manage, update, and track these ideas as they evolve.

### 6. Data Persistence
Your data is persisted across sessions. Even if you close the program or shut down your computer, your friend descriptions will remain stored and accessible upon relaunch.

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Consistency_Companion_prototype.git
   ```

2. **Set Up the Environment**
   - Ensure that MySQL is installed and running.
   - Install the required Python libraries using:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the `.bat` File**
   - Simply double-click the included `.bat` file for quick startup, or run the app manually using:
     ```bash
     streamlit run app.py
     ```

---

## Usage Instructions

1. **Start MySQL**
   - Make sure your MySQL server is running. If it’s not, launch it via MySQL Workbench or the command line.

2. **Run the Application**
   - Use the `.bat` file or the command:
     ```bash
     streamlit run app.py
     ```
   - Ensure your database credentials and connection are correctly set in the `Consistency_tables.py` file.

3. **Interacting with the Companion**
   - Take tests to reflect on your learning.
   - Receive tailored improvement suggestions.
   - Chat with your virtual friend.
   - Track your ideas and motivation over time.

---

## Contributing

Contributions are welcome! If you'd like to help improve this project, please fork the repository, create a new branch, and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

This version includes the GitHub markdown style for headings, lists, and code blocks. It also adds the `.bat` file for easier execution.
