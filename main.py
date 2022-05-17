from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    # reset timer to "00:00"
    canvas.itemconfig(timer_text, text="00:00")
    # reset checkmark
    cb_text_label.config(text="")
    # reset timer text
    text_label.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th rep:
    


    # If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        text_label.config(text="Long Break", fg=RED)
    # If it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        text_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        text_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    print(count)
    canvas.itemconfig(timer_text, text=f"{count_min}: {count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        cb_text_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# window.after(1000,say_something, 2, 4,6)

canvas = Canvas(width=200, height=222, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 110, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

text_label = Label(text="Timer", font=("Italic", 30, "bold"), fg=GREEN, bg=YELLOW)
text_label.grid(row=0, column=1)



start_btn = Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(row=2, column=0)

end_btn = Button(text="End", highlightthickness=0, command=reset)
end_btn.grid(row=2, column=2)

cb_text_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
cb_text_label.grid(row=3, column=1)


# count_down(5)

window.mainloop()