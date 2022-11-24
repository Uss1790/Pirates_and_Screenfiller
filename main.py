counter = 0

point = []

def on_button_pressed_a():
    music.set_tempo(45)
    music.play_tone(294, music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.EIGHTH))
    music.play_tone(466, music.beat(BeatFraction.QUARTER))
    music.play_tone(466, music.beat(BeatFraction.QUARTER))
    music.play_tone(466, music.beat(BeatFraction.EIGHTH))
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.EIGHTH))
    music.play_tone(466, music.beat(BeatFraction.QUARTER))
    music.play_tone(466, music.beat(BeatFraction.QUARTER))
    music.play_tone(466, music.beat(BeatFraction.EIGHTH))
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.play_tone(466, music.beat(BeatFraction.EIGHTH))
    music.play_tone(523, music.beat(BeatFraction.QUARTER))
    music.play_tone(523, music.beat(BeatFraction.QUARTER))
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
    music.play_tone(587, music.beat(BeatFraction.EIGHTH))
    music.play_tone(622, music.beat(BeatFraction.QUARTER))
    music.play_tone(622, music.beat(BeatFraction.QUARTER))
    music.play_tone(587, music.beat(BeatFraction.EIGHTH))
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
    music.play_tone(587, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.EIGHTH))
    music.play_tone(466, music.beat(BeatFraction.QUARTER))
    music.play_tone(466, music.beat(BeatFraction.QUARTER))
    music.play_tone(523, music.beat(BeatFraction.QUARTER))
    music.play_tone(587, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.play_tone(466, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global counter
    point = []
    while True:
        counter += 1
        x = int(Math.random() * 5)
        y = int(Math.random() * 5)
        if (x + y / 10) not in point:
            basic.pause(100)
            led.plot(x, y)
            point.append(x + y / 10)
        if len(point) == 25:
            basic.show_number(counter)
            break
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
