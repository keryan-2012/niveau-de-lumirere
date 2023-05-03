basic.forever(function () {
    if (input.lightLevel() > 100) {
        basic.showString("Frigo Ouvert!")
        basic.showLeds(`
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            `)
        music.playMelody("F B D A A C5 E C ", 40)
        basic.pause(100)
        music.stopAllSounds()
    }
    if (input.lightLevel() < 100) {
        basic.showString("Frigo fermée")
        basic.showLeds(`
            . # . # .
            # . . . #
            . . . . .
            # . . . #
            . # . # .
            `)
    }
    basic.clearScreen()
})
