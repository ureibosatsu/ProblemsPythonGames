# This is a graphical password guessing game that displays a
# list of potential computer passwords. The player is allowed
# up to 4 attempts to guess the password. Each time the user
# guesses incorrectly, the user is prompted to make a new guess.
# The game indicates whether the player successfully guessed
# the password or not.

from uagame import Window
from time import sleep


def main():
    location = [0, 0]
    attempts_left = 4
    window = create_window()
    display_header(window, location, attempts_left)
    password = display_password_list(window, location)
    guess = get_guesses(window, password, location, attempts_left)
    end_game(window, guess, password)


#   create window for game, open it and return it
def create_window():
    window = Window("Hacking", 600, 500)
    window.set_font_name("couriernew")
    window.set_font_size(18)
    window.set_font_color('green')
    window.set_bg_color('black')
    return window


# display the header line by line
def display_header(window, location, attempts):
    header = ["DEBUG MODE", str(attempts) + " ATTEMPT(S) LEFT", ""]
    for headerLine in header:
        display_line(window, headerLine, location)


# display a string in the window at location
def display_line(window, string, location):
    string_height = window.get_font_height()
    pause_time = 0.3
    window.draw_string(string, location[0], location[1])
    window.update()
    sleep(pause_time)
    location[1] = location[1] + string_height


# display the password list line by line starting at location, set the password
def display_password_list(window, location):
    password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE',
                     'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']
    for password in password_list:
        display_line(window, password, location)
    pw = password_list[7]
    return pw


# prompt user for guesses until she guesses correctly or runs out of the 4 guesses, return final guess
def get_guesses(window, password, location, attempts_left):
    prompt = 'ENTER PASSWORD >'
    guess = prompt_user(window, prompt, location)
    string_height = window.get_font_height()
    location[1] += string_height
    attempts_left -= 1
    while guess != password and attempts_left != 0:  # while guess is not password and attempts left is not zero
        window.draw_string(str(attempts_left), 0, window.get_font_height())
        check_warning(window, attempts_left)
        guess = window.input_string(prompt, location[0], location[1])
        location[1] += string_height
        attempts_left -= 1
    return guess


# prompt user for input
def prompt_user(window, prompt, location):
    user_input = window.input_string(prompt, location[0], location[1])
    return user_input


# check if one guess is left, and if so display warning message
def check_warning(window, attempts_left):
    warning = '*** LOCKOUT WARNING ***'
    if attempts_left == 1:
        warning_length = window.get_string_width(warning)
        string_height = window.get_font_height()
        window.draw_string(warning, 600 - warning_length, 500 - string_height)


# end the game by displaying the outcome,
# eliciting an enter, and closing the window
def end_game(window, guess, password):
    window.clear()
    if guess == password:
        outcome = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
        prompt = 'PRESS ENTER TO CONTINUE'
    else:
        outcome = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '', 'PLEASE CONTACT AN ADMINISTRATOR', '']
        prompt = 'PRESS ENTER TO EXIT'
    location = display_outcome(window, outcome)
    location[0] = (window.get_width() - window.get_string_width(prompt))//2
    prompt_user(window, prompt, location)
    window.close()


# display each line in the outcome line by line
def display_outcome(window, outcome):
    location = [0, 0]
    string_height = window.get_font_height()
    outcome_height = (len(outcome) + 1) * string_height
    y_space = window.get_height() - outcome_height
    location[1] = y_space // 2
    for outcome_line in outcome:
        x_space = window.get_width() - window.get_string_width(outcome_line)
        location[0] = x_space // 2
        display_line(window, outcome_line, location)
    return location


main()
