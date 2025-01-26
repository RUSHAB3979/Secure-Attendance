from flask import Flask, request, render_template, session
import csv
from datetime import datetime
import os

app = Flask(__name__)

app.secret_key = 'Secret Key'  #if you want to manage session get your secret key
ATTENDANCE_FILE = "attendance.csv"

#check if the csv file exists
def init_files():
    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Date", "Time", "IP Address"])

#here attendance submissions display the form and handle 
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        #Get form data
        roll_number = request.form.get("roll_number")
        name = request.form.get("name")
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        ip_address = request.remote_addr  #Get the user's IP address

        #Check if the user has already marked attendance for today based on IP
        with open(ATTENDANCE_FILE, mode="r") as file:
            reader = csv.reader(file)
            records = list(reader)

        #Check if attendance already exists for this IP and Date
        for row in records:
            if len(row) >= 5 and row[4] == ip_address and row[2] == date:
                return render_template("index.html", error="Attendance already marked from this device for today.", records=records)

        #Save the attendance to the CSV file
        with open(ATTENDANCE_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([roll_number, name, date, time, ip_address])

        #Reloads the records after marking attendance
        with open(ATTENDANCE_FILE, mode="r") as file:
            reader = csv.reader(file)
            records = list(reader)

        #Confirmation message
        return render_template("index.html", success="Attendance marked successfully!", records=records)

    #check attendance records from the csv attendance file
    with open(ATTENDANCE_FILE, mode="r") as file:
        reader = csv.reader(file)
        records = list(reader)

    # Check if the file is empty or only contains headers
    if len(records) <= 1:
        records = []

    return render_template("index.html", records=records)
print("After taking all successfull attendance extract the file data and store it safely and remove the file content so that new attendance can be marked")
print("Please make sure that students are connecting to website by using http://-ip- because Flask doesnt supports https responses")


if __name__ == "__main__":
    init_files()
    app.run(host="0.0.0.0", port=5000)


