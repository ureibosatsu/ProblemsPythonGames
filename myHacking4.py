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
header = ["DEBUG MODE", "1 ATTEMPT(S) LEFT", ""]

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
for pw in passwordList:
    #   display password line
    window.draw_string(pw, line_x, line_y)
    window.update()
    sleep(pause_time)
    line_y = line_y + string_height

#   choose password
password = passwordList[7]

#   prompt for guess
guess = window.input_string("ENTER PASSWORD >", line_x, line_y)

#   end game
#   clear window
window.clear()

# create outcome

if guess == password:
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
