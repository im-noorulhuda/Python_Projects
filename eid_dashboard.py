from tkinter import *
import random
import winsound  # works on Windows only

# ---------------- WINDOW ----------------
root = Tk()
root.title("Eid Wish For You") # title
root.geometry("550x450") # dashborad size
root.config(bg="#FFD1DC") #background color


# ---------------- TITLE ----------------
title = Label(
    root,
    text="🌙 Eid Ul Adha Mubarak 🐐",
    font=("Ink Free", 22, "bold"),
    bg="#FFD1DC",
    fg="white"
)
title.pack(pady=15)

# ---------------- NAME INPUT ----------------
name_entry = Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
name_entry.pack(pady=10)
name_entry.insert(0, "Enter your name")

# ---------------- WISH LABEL ----------------
wish_label = Label(
    root,
    text="Your wish will appear here ✨",
    font=("Arial", 14),
    bg="#FFD1DC",
    fg="#C71585"
)
wish_label.pack(pady=20)

# ---------------- WISHES ----------------
wishes = [
    "May your Eid be filled with happiness ✨",
    "May Allah bless you and your family 🌙",
    "Eid brings peace and joy 🐐",
    "Stay grateful and blessed 💖",
    "Wishing you love and success 🌸"
]

# ---------------- SOUND ----------------
def play_sound():
    try:
        winsound.Beep(1000, 150)  # simple beep sound
    except:
        pass

# ---------------- ANIMATION TEXT ----------------
def animate_text(text, i=0):
    if i <= len(text):
        wish_label.config(text=text[:i])
        root.after(40, animate_text, text, i+1)

# ---------------- BUTTON FUNCTION ----------------
def generate_wish():
    name = name_entry.get()

    if name == "" or name == "Enter your name":
        name = "Dear User"

    wish = random.choice(wishes)
    final_text = f"{name}, {wish}"

    play_sound()
    animate_text(final_text)

# ---------------- BUTTON ----------------
btn = Button(
    root,
    text="✨ Get Eid Wish ✨",
    font=("Segoe Print", 12, "bold"),
    bg="#FF1493",
    fg="white",
    activebackground="#FF69B4",
    activeforeground="white",
    padx=15,
    pady=5,
    bd=0,
    command=generate_wish
)
btn.pack(pady=20)

# ---------------- RUN ----------------
root.mainloop()