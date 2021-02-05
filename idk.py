import curses
import random


def window(stdscr):

  sh, sw = stdscr.getmaxyx()

  #stdscr.nodelay(True)
  #stdscr.timeout(100)
  
  
  
  curses.start_color()
  curses.use_default_colors()

  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)

  
  while True:
    letter = chr(random.randint(33, 126))
    color = random.randint(1, curses.COLORS + 1)

    y = random.randint(0, sh-1)
    x = random.randint(0, sw-1)

    stdscr.addstr(y, x, letter, curses.color_pair(color))
    stdscr.getch()

curses.wrapper(window)
