# This is a text-based password guessing game.
from uagame import Window
from time import sleep
#   create window

window = Window("Hacking", 600, 500)
window.set_font_name("couriernew")
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')


#   display header
line_x = 0
line_y = 0
string_height = window.get_font_height()
pause_time = 0.3
attempt_count = 4
header = ["DEBUG MODE", str(attempt_count)+" ATTEMPT(S) LEFT", ""]

#display header with for loop
for headerLine in header:
   #display header line
    window.draw_string(headerLine, line_x, line_y)
    window.update()
    sleep(pause_time)
    line_y = line_y + string_height


#   display passwords
passwordList = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE',
             'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']
for password in passwordList:
    #   display password line
    window.draw_string(password, line_x, line_y)
    window.update()
    sleep(pause_time)
    line_y = line_y + string_height

#   choose password
pw = passwordList[7]

#   get guesses
#   prompt for guess
prompt = 'ENTER PASSWORD >'
guess = window.input_string(prompt, line_x, line_y)
line_y = line_y + string_height
#   decrement attempts left
attempt_count = attempt_count - 1
while guess != pw and attempt_count != 0: # while guess is not password and attempts left is not zero
    window.draw_string(str(attempt_count), 0, string_height)
    # check warning
    if attempt_count == 1: # if attempts left is one, display warning
        warning = '*** LOCKOUT WARNING ***'
        warning_length = window.get_string_width(warning)
        window.draw_string(warning, 600-warning_length, 500-string_height)
    guess = window.input_string(prompt, line_x, line_y)
    line_y = line_y + string_height
    attempt_count = attempt_count - 1


#   end game
#   clear window
window.clear()

# create outcome

if guess == pw:
    # create success
    outcome = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
    prompt = 'PRESS ENTER TO CONTINUE'
else:
    # create failure
    outcome = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '', 'PLEASE CONTACT AN ADMINISTRATOR', '']
    prompt = 'PRESS ENTER TO EXIT'

    #   display outcome
    #      compute y coordinate
outcome_height = (len(outcome) + 1) * string_height
y_space = window.get_height() - outcome_height
line_y = y_space // 2

for outcome_line in outcome:
    # display centered outcome line
    #    compute x coordinate
    x_space = window.get_width() - window.get_string_width(outcome_line)
    line_x = x_space // 2

    window.draw_string(outcome_line, line_x, line_y)
    window.update()
    sleep(pause_time)
    line_y = line_y + string_height

#   prompt for end
x_space = window.get_width() - window.get_string_width(prompt)
line_x = x_space // 2
window.input_string(prompt, line_x, line_y)

#   close window
window.close()
