input.is_gesture(Gesture.SHAKE)
def on_logo_event_pressed():
    pass
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)
led.unplot(1, 0)
def onEvery_interval():
    pass
loops.every_interval(200, onEvery_interval)
input.button_is_pressed(Button.A)
basic.show_string("Hello!")
music.play_melody("", 120)