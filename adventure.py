
def start():
  # give some prompts.
  print("You are standing in a dark room.")
  print("There is a door to your left and right, which one do you take? (l or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead him to bear_room()
    bear_room()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to monster_room()
    monster_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type something properly?")


# start the game
start()