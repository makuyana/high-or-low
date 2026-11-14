
import customtkinter as ctk
from random import choice
from gameData import game_data

score = 0

current_celebrity = choice(game_data)

next_celebrity = choice(
    [person for person in game_data if person != current_celebrity]
)


def display_celebrity():

    # LEFT SIDE: Current celebrity
    left_name_label.configure(
        text=current_celebrity["name"]
    )

    left_followers_label.configure(
        text=f"👥 {current_celebrity['followers']:,}"
    )

    # RIGHT SIDE: Celebrity to compare
    right_name_label.configure(
        text=next_celebrity["name"]
    )

    right_followers_label.configure(
        text="??? followers"
    )


def play_round(guess):
    global score, current_celebrity, next_celebrity

    current_followers = current_celebrity["followers"]
    next_followers = next_celebrity["followers"]

    if (guess == "higher" and next_followers > current_followers) or \
       (guess == "lower" and next_followers < current_followers):

        score += 1

        result_label.configure(
            text=f"🎉 Correct! Score: {score}",
            text_color="#2ecc71"
        )

        # Move the next celebrity to the left
        current_celebrity = next_celebrity

        # Select a new celebrity
        next_celebrity = choice(
            [person for person in game_data
             if person != current_celebrity]
        )

        display_celebrity()

    else:

        result_label.configure(
            text=f"💥 Wrong! Final score: {score}",
            text_color="#e74c3c"
        )

        # Reveal the correct follower count
        right_followers_label.configure(
            text=f"👥 {next_followers:,} followers"
        )

        # Disable buttons
        higher_btn.configure(state="disabled")
        lower_btn.configure(state="disabled")


# --- UI Setup ---

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Higher or Lower Game")
app.geometry("750x650")
app.resizable(False, False)

app.grid_columnconfigure((0, 1), weight=1)
app.grid_rowconfigure(0, weight=0)
app.grid_rowconfigure(1, weight=1)


# Main heading
label = ctk.CTkLabel(
    app,
    text="High vs Low",
    text_color="yellow",
    font=("Arial", 30, "bold")
)
label.grid(row=0, column=0, columnspan=2, pady=30)


# Create frames
left_frame = ctk.CTkFrame(
    app,
    fg_color="#2E8B57"
)

right_frame = ctk.CTkFrame(
    app,
    fg_color="#263B55"
)

left_frame.grid(row=1, column=0, sticky="nsew")
right_frame.grid(row=1, column=1, sticky="nsew")


# VS circle
vs_frame = ctk.CTkFrame(
    app,
    width=70,
    height=70,
    fg_color="#993523",
    corner_radius=35
)

vs_frame.place(relx=0.5, rely=0.5, anchor="center")

vs_label = ctk.CTkLabel(
    vs_frame,
    text="VS",
    text_color="white",
    font=("Arial", 25, "bold")
)

vs_label.place(relx=0.5, rely=0.5, anchor="center")


# ==========================
# LEFT SIDE
# ==========================

left_name_label = ctk.CTkLabel(
    left_frame,
    text="",
    text_color="white",
    font=("Arial", 21, "bold")
)

left_name_label.place(
    relx=0.5, rely=0.35, anchor="center"
)


left_has_label = ctk.CTkLabel(
    left_frame,
    text="has",
    text_color="white",
    font=("Arial", 17)
)

left_has_label.place(
    relx=0.5, rely=0.48, anchor="center"
)


left_followers_label = ctk.CTkLabel(
    left_frame,
    text="",
    text_color="white",
    font=("Arial", 20, "bold")
)

left_followers_label.place(
    relx=0.5, rely=0.60, anchor="center"
)


# ==========================
# RIGHT SIDE
# ==========================

right_name_label = ctk.CTkLabel(
    right_frame,
    text="",
    text_color="white",
    font=("Arial", 21, "bold")
)

right_name_label.place(
    relx=0.5, rely=0.25, anchor="center"
)


right_has_label = ctk.CTkLabel(
    right_frame,
    text="has",
    text_color="white",
    font=("Arial", 17)
)

right_has_label.place(
    relx=0.5, rely=0.36, anchor="center"
)


right_followers_label = ctk.CTkLabel(
    right_frame,
    text="??? followers",
    text_color="white",
    font=("Arial", 20, "bold")
)

right_followers_label.place(
    relx=0.5, rely=0.47, anchor="center"
)


# Higher button
higher_btn = ctk.CTkButton(
    right_frame,
    text="📈 Higher",
    text_color="orange",
    width=130,
    height=45,
    command=lambda: play_round("higher")
)

higher_btn.place(
    relx=0.5, rely=0.62, anchor="center"
)


# Lower button
lower_btn = ctk.CTkButton(
    right_frame,
    text="📉 Lower",
    text_color="red",
    width=130,
    height=45,
    command=lambda: play_round("lower")
)

lower_btn.place(
    relx=0.5, rely=0.74, anchor="center"
)


# Result label
result_label = ctk.CTkLabel(
    right_frame,
    text="Make your guess!",
    text_color="white",
    font=("Arial", 16, "bold")
)

result_label.place(
    relx=0.5, rely=0.9, anchor="center"
)


# Display celebrities when game starts
display_celebrity()

app.mainloop()
