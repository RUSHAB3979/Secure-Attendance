# Secure Attendance System

A simple, secure web-based attendance marking system built with Flask.

## Project Description

The Secure Attendance System provides a user-friendly interface for marking attendance while ensuring data integrity. It prevents users from marking attendance multiple times on the same day from the same device, making it suitable for small-scale academic or professional use. All attendance records are stored in a `attendance.csv` file for easy access and management.

## Features

- **User-Friendly Interface:** A clean and intuitive web form for entering roll number and name.
- **Secure Attendance:** Prevents multiple entries for the same user on the same day.
- **Device-Limited Access:** Associates attendance with a unique device (via IP address) to prevent proxy attendance.
- **Real-Time Validation:** Displays error messages for duplicate entries and success messages for valid entries.
- **Attendance Records:** Displays a table of all attendance records and stores data persistently in a CSV file.

## How It Works

The application identifies a user's device by its IP address. When a user tries to mark attendance, the system checks if an entry with the same IP address already exists for the current day. If it does, the new entry is blocked. This ensures that each user can only mark their attendance once per day from a single device.

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/RUSHAB3979/Secure-Attendance.git
    cd Secure-Attendance
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Flask application:**
    ```bash
    python Backend.py
    ```

2.  **Access the application:**
    Open your web browser and navigate to `http://<your-ip-address>:5000`.

3.  **Mark your attendance:**
    - Enter your Roll Number and Name in the form.
    - Click the "Mark Attendance" button.

A success message will be displayed if your attendance is marked successfully. An error message will appear if you have already marked your attendance for the day.

## Important Note

For the application to work correctly, please ensure you are accessing it using `http://` and not `https://`. The Flask development server does not support HTTPS by default.
