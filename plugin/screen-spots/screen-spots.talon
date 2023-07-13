mode: command
-
# save a mouse position to a spot name
spot save <user.text>: user.save_spot(user.text)

# click a saved spot then return the cursor to its prior position
spot [(click|touch)] {user.saved_spots}: user.click_spot(user.saved_spots)

# move the cursor to a saved spot
spot move {user.saved_spots}: user.move_to_spot(user.saved_spots)

# hold left click then move the cursor to a saved spot
spot drag {user.saved_spots}: user.drag_spot(user.saved_spots)

spot swipe {user.saved_spots}: user.drag_spot(user.saved_spots, 1)

# deletes all current spots (does not alter the cached dictionary of spots)
spot clear all: user.clear_spot_dictionary()

# delete a specific spot (does not alter the cached dictionary of spots)
spot clear {user.saved_spots}: user.clear_spot(user.saved_spots)

# display a list of all active spot names
spot list [all]: user.list_spot()

# Close the list of active spot names. including 'clothes' because that's commonly misheard by talon
spot (close|clothes)$: user.close_spot_list()

# displays a small colored circle at the location of each saved spot
spot [toggle] heatmap: user.toggle_spot_heatmap()
 