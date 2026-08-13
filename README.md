# Attendance Marker System

## Project Description

The Attendance Marker System is a simple web application built using Flask that allows users to mark their attendance in a secure and efficient manner. This system is designed to prevent duplicate entries from the same user on the same day by checking their IP address. All attendance records are stored in a `attendance.csv` file.

## Features

-   **User-Friendly Interface:** A clean and intuitive web form for entering a roll number and name.
-   **Secure Attendance:** Prevents multiple entries for the same user on the same day by checking the user's IP address.
-   **Real-Time Validation:** Displays error messages for duplicate entries and success messages for valid entries.
-   **Attendance Records:** Displays a table of all attendance records and stores data persistently in a CSV file.

## How It Works

The application is built with Flask. When a user submits the attendance form, the application checks the `attendance.csv` file to see if an entry with the same IP address already exists for the current day.

-   If an entry exists, the application displays an error message.
-   If no entry exists, the application adds a new row to the `attendance.csv` file with the user's roll number, name, the current date and time, and their IP address.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/RUSHAB3979/Secure-Attendance.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Secure-Attendance
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Flask application:**
    ```bash
    python Backend.py
    ```
2.  **Open your web browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```
    Or, if accessing from another device on the same network, use the host machine's local IP address: `http://<your-ip-address>:5000`.

    **Note:** The application runs on HTTP. Using HTTPS might cause issues.

3.  **Enter your Roll Number and Name into the form.**

4.  **Click "Mark Attendance".**

    -   If your attendance is marked successfully, you will see a success message.
    -   If you have already marked your attendance for the day, you will see an error message.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
