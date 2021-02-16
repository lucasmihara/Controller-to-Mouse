from __future__ import division
import XInput as xin
import pyautogui as gui

is_turbo = False
is_left_clicked = False
is_right_clicked = False
is_middle_clicked = False

mouse_speed = 50.0
scroll_speed = 90.0
turbo_speed = 3.0

left_mouse = 'A'
right_mouse = 'X'
middle_mouse = 'LEFT_THUMB'
left_arrow = 'DPAD_LEFT'
right_arrow = 'DPAD_RIGHT'
up_arrow = 'DPAD_UP'
down_arrow = 'DPAD_DOWN'
back = 'LEFT_SHOULDER'
forward = 'RIGHT_SHOULDER'
f5 = 'BACK'
turbo = 'B'


def switch_turbo(press):
    global is_turbo
    if not is_turbo and press:
        is_turbo = True
    elif is_turbo and not press:
        is_turbo = False


def move_cursor(x, y):
    curr_pos_x, curr_pos_y = gui.position()
    size = gui.size()

    if is_turbo:
        new_pos_x = curr_pos_x + x * mouse_speed * turbo_speed
        new_pos_y = curr_pos_y - y * mouse_speed * turbo_speed
    else:
        new_pos_x = curr_pos_x + x * mouse_speed
        new_pos_y = curr_pos_y - y * mouse_speed

    if new_pos_x >= size[0] - 1:
        new_pos_x = size[0] - 2
    if new_pos_y >= size[1] - 1:
        new_pos_y = size[1] - 2
    if new_pos_x <= 0:
        new_pos_x = 1
    if new_pos_y <= 0:
        new_pos_y = 1

    gui.moveTo(new_pos_x, new_pos_y, 0.1)


def move_scroll(x, y):
    if is_turbo:
        gui.scroll(int(scroll_speed * y * turbo_speed))
    else:
        gui.scroll(int(scroll_speed*y))


def left_click(press):
    global is_left_clicked
    if not is_left_clicked and press:
        gui.mouseDown()
        is_left_clicked = True
    elif is_left_clicked and not press:
        gui.mouseUp()
        is_left_clicked = False


def right_click(press):
    global is_right_clicked
    if not is_right_clicked and press:
        gui.mouseDown(button='right')
        is_right_clicked = True
    elif is_right_clicked and not press:
        gui.mouseUp(button='right')
        is_right_clicked = False


def middle_click(press):
    global is_middle_clicked
    if not is_middle_clicked and press:
        gui.mouseDown(button='middle')
        is_middle_clicked = True
    elif is_middle_clicked and not press:
        gui.mouseUp(button='middle')
        is_middle_clicked = False


def other_buttons(buttons):
    if buttons[f5]:
        gui.press('f5')
    if buttons[back]:
        gui.press('browserback')
    if buttons[forward]:
        gui.press('browserforward')

    if buttons[left_arrow]:
        gui.press('left')
    if buttons[right_arrow]:
        gui.press('right')
    if buttons[up_arrow]:
        gui.press('up')
    if buttons[down_arrow]:
        gui.press('down')


if __name__ == '__main__':
    while True:

        state = xin.get_state(0)
        stick = xin.get_thumb_values(state)
        if stick[0][0] != 0 or stick[0][1] != 0:
            move_cursor(stick[0][0], stick[0][1])
        if stick[1][0] != 0 or stick[1][1] != 0:
            move_scroll(stick[1][0], stick[1][1])

        buttons = xin.get_button_values(state)

        left_click(buttons[left_mouse])
        right_click(buttons[right_mouse])
        middle_click(buttons[middle_mouse])
        switch_turbo(buttons[turbo])
        other_buttons(buttons)

