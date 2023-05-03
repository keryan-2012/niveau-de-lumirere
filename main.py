def on_forever():
    if input.light_level() > 100:
        basic.show_string("Frigo Ouvert!")
        basic.show_leds("""
            # . # . #
                        . # # # .
                        # # # # #
                        . # # # .
                        # . # . #
        """)
        music.play_melody("F B D A A C5 E C ", 40)
        basic.pause(100)
        music.stop_all_sounds()
    if input.light_level() < 100:
        basic.show_string("Frigo fermée")
        basic.show_leds("""
            . # . # .
                        # . . . #
                        . . . . .
                        # . . . #
                        . # . # .
        """)
    basic.clear_screen()
basic.forever(on_forever)
