# Entry point
label start:

    # ID of this playtrhoguh
    $ anticheat = persistent.anticheat

    # keep track of chapter
    $ chapter = 0

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # girl names
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ mi_name = "Mio"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    call default_boot_screen
    if persistent.playthrough == 0:
        #Call example script
        #call alice_poem_demos
        call setup
        call pre_ch0
        call ch0_main
        call ch0_end
        call ch0_blackbox_puzzle

        $ chapter = 1
        call pre_ch1
        call ch1_main
        call ch1_end
        call ch1_blackbox_puzzle

        ## Extra Content
        # This probably won't be finished, so I am commenting it out.
        $ chapter = 2
        # No script for any prologue; Alice has been already introduced. For now.
        # call ch2_main
        # call ch2_end

        ## Disable this segment if it isn't the demo.
        call demo_end
        call ch2_main
        call demo_end_2

    if persistent.playthrough == 1:
        #Stuff here would only play after you increased the playthrough count

        ## Disable this line if this isn't the demo.
        call demo_end_loop
        pass

    return
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
