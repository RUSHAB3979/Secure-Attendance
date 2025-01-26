Attendance Marker System

Project Description

The Attendance Marker System is a simple web application built using Flask that allows users to mark attendance in a secure and efficient manner. This system ensures that a user can only mark attendance from one device and prevents multiple entries for the same user. The application also maintains a record of all attendance entries in a CSV file for easy reference.

Features

User-Friendly Interface: A clean and intuitive web form for entering roll number and name.

Secure Attendance: Prevents multiple entries for the same roll number on the same day.

Device-Limited Access: Associates attendance with a unique device to prevent proxy attendance.

Real-Time Validation: Displays error messages for duplicate entries and success messages for valid entries.

Attendance Records: Displays a table of all attendance records and stores data persistently in a CSV file.

Installation

Clone this repository:
git clone https://github.com/RUSHAB3979/Secure-Attendance.git

Install the required dependencies:
pip install -r requirements.txt

Launch the application and navigate to the provided URL.

Enter your Roll Number and Name into the form.

Click Mark Attendance.

If attendance is successfully marked, a success message will appear. If the roll number has already marked attendance for the day, an error message will be displayed.

CAUTION - Dont use https://your ip use http://your ip for non error execution.
