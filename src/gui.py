import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sqlite3
import pandas as pd
import sys
DB_PATH = "../database/attendance.db"


# =====================================================
# START ATTENDANCE
# =====================================================

def start_attendance():

    try:

        subprocess.Popen(
            [
                sys.executable,
                "realtime_attendance.py"
            ]
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

print(sys.executable)


# =====================================================
# EXPORT CSV
# =====================================================

def export_csv():

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT
        student_name,
        date,
        entry_time,
        exit_time,
        duration_seconds
    FROM attendance_sessions
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    df.to_csv(
        "../reports/attendance_report.csv",
        index=False
    )

    messagebox.showinfo(
        "Success",
        "CSV Exported Successfully!"
    )


# =====================================================
# VIEW DATABASE
# =====================================================

def view_database():

    window = tk.Toplevel(root)

    window.title(
        "Attendance Records"
    )

    window.geometry(
        "900x500"
    )

    tree = ttk.Treeview(

        window,

        columns=(

            "Name",
            "Date",
            "Entry",
            "Exit",
            "Duration"

        ),

        show="headings"

    )

    tree.heading(
        "Name",
        text="Student"
    )

    tree.heading(
        "Date",
        text="Date"
    )

    tree.heading(
        "Entry",
        text="Arrival"
    )

    tree.heading(
        "Exit",
        text="Leaving"
    )

    tree.heading(
        "Duration",
        text="Duration(sec)"
    )

    tree.pack(
        fill=tk.BOTH,
        expand=True
    )

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            student_name,

            date,

            entry_time,

            exit_time,

            duration_seconds

        FROM attendance_sessions

        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    for row in rows:

        tree.insert(
            "",
            tk.END,
            values=row
        )


# =====================================================
# VIEW DAILY REPORT
# =====================================================

def view_report():

    window = tk.Toplevel(root)

    window.title(
        "Daily Attendance Report"
    )

    window.geometry(
        "700x400"
    )

    text = tk.Text(
        window,
        font=("Consolas", 11)
    )

    text.pack(
        fill=tk.BOTH,
        expand=True
    )

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            student_name,

            MIN(entry_time),

            MAX(exit_time),

            SUM(duration_seconds)

        FROM attendance_sessions

        GROUP BY student_name
        """
    )

    rows = cursor.fetchall()

    conn.close()

    text.insert(
        tk.END,
        "\nDAILY ATTENDANCE SUMMARY\n\n"
    )

    text.insert(
        tk.END,
        f"{'Name':<15}"
        f"{'Arrival':<15}"
        f"{'Leaving':<15}"
        f"{'Duration(sec)':<15}\n"
    )

    text.insert(
        tk.END,
        "-" * 60 + "\n"
    )

    for row in rows:

        text.insert(
            tk.END,
            f"{row[0]:<15}"
            f"{row[1]:<15}"
            f"{row[2]:<15}"
            f"{row[3]:<15}\n"
        )


# =====================================================
# MAIN WINDOW
# =====================================================

root = tk.Tk()
root.title("Face Attendance Management System")
root.geometry("500x550")
root.resizable(False, False)

# Modern Dark Theme Colors
BG_COLOR = "#1e1e2e"
TEXT_COLOR = "#cdd6f4"
BTN_BG = "#89b4fa"
BTN_FG = "#11111b"
BTN_ACTIVE_BG = "#f38ba8"
BTN_ACTIVE_FG = "#11111b"
FONT = ("Segoe UI", 12, "bold")

root.configure(bg=BG_COLOR)

title = tk.Label(
    root,
    text="FACE ATTENDANCE\nMANAGEMENT SYSTEM",
    font=("Segoe UI", 20, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
title.pack(pady=30)

def create_btn(text, command, bg_color=BTN_BG):
    return tk.Button(
        root,
        text=text,
        font=FONT,
        width=25,
        height=2,
        bg=bg_color,
        fg=BTN_FG,
        activebackground=BTN_ACTIVE_BG,
        activeforeground=BTN_ACTIVE_FG,
        relief=tk.FLAT,
        cursor="hand2",
        command=command
    )

btn1 = create_btn("Start Attendance", start_attendance, bg_color="#a6e3a1") # Green
btn1.pack(pady=10)

btn2 = create_btn("View Report", view_report)
btn2.pack(pady=10)

btn3 = create_btn("View Database", view_database)
btn3.pack(pady=10)

btn4 = create_btn("Export CSV", export_csv, bg_color="#f9e2af") # Yellow
btn4.pack(pady=10)

btn5 = create_btn("Exit", root.destroy, bg_color="#f38ba8") # Red
btn5.pack(pady=10)

root.mainloop()