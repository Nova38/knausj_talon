not tag: user.screenshot_disabled
-

^grab screen$: user.screenshot()
^grab screen <number_small>$: user.screenshot(number_small)
^grab window$: user.screenshot_window()
^grab selection$: user.screenshot_selection()
^grab selection clip$: user.screenshot_selection_clip()
^grab settings$: user.screenshot_settings()
^grab screen clip$: user.screenshot_clipboard()
^grab screen <number_small> clip$: user.screenshot_clipboard(number_small)
^grab window clip$: user.screenshot_window_clipboard()
