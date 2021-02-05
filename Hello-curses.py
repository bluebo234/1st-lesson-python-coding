import curses

def window(stdscr):

  #calculate the center of the window
  #get the heigh and the width of the screen
  sh, sw = stdscr.getmaxyx()

  #y-axis and x-axis are start from 0 (0, 1)
  stdscr.addstr(sh - 5, 0, chr(120))

  while True:
    #waiting user's input
    #getch will get the ascii code
    userkey = stdscr.getch()
    stdscr.addstr(sh // 2, sw // 2 - len(str(userkey)) // 2, (str(userkey)))
    
    if userkey == 27:
      break

curses.wrapper(window)