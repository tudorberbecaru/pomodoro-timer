from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

# Define color constants for the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Define time constants for the Pomodoro timer
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECONDS_IN_A_MINUTE = 60

# Variables to keep track of repetitions and timer
reps = 0
timer = ""


# Function to reset the timer
def reset_timer():
    global reps
    reps = 0

    # Cancel the ongoing timer and reset UI components
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", font=(FONT_NAME, 42, "bold"), fg=GREEN, bg=YELLOW)
    checkmarks.config(text="")


# Function to start the timer
def start_timer():
    global reps
    reps += 1

    # Calculate time for work, short break, and long break
    work_time = WORK_MIN * SECONDS_IN_A_MINUTE
    short_break_time = SHORT_BREAK_MIN * SECONDS_IN_A_MINUTE
    long_break_time = LONG_BREAK_MIN * SECONDS_IN_A_MINUTE

    # Determine the type of interval based on repetitions
    if reps % 8 == 0:
        countdown(long_break_time)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_time)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_time)
        title_label.config(text="Work", fg=GREEN)


# Function for the countdown
def countdown(count):

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    # Update the timer text on the canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # If countdown is not complete, continue updating
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        # Start the next interval and update checkmarks if it's a break
        start_timer()
        if reps % 2 == 0:
            checkmarks["text"] += "✔"


# GUI setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_bg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_bg)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 42, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

checkmarks = Label(font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

window.mainloop()
