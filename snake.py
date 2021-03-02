import curses
from curses import textpad
import random

def board(stdscr):

  # turn off the cursor1
  curses.curs_set(0)
  # turn on nodelay to make the snake moving by itself.
  stdscr.nodelay(1)
  # set the timeout to 0.1 second
  stdscr.timeout(150)

  sh, sw = stdscr.getmaxyx()

  # define the game board.
  box = [
    [3, 3],
    [sh - 3, sw - 3]
  ]
  # draw the game board.
  textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

  food = [
    # the y axis
    random.randint(box[0][0] + 1, box[1][0] - 1),
    # the x axis
    random.randint(box[0][1] + 1, box[1][1] - 1)
    ]
  stdscr.addstr(food[0], food[1], "*")
  # define the snake body.
  snake = [
    # head is always be the first item.
    [sh // 2, sw // 2 + 1],
    # body,
    [sh // 2, sw // 2],
    # tail
    [sh // 2, sw // 2 - 1]
    ]
  snake_ch = chr(9608)

  # draw the snake body.
  for point in snake:
    stdscr.addstr(point[0], point[1], snake_ch)

  # set the default direction for the snake.
  direction = curses.KEY_RIGHT

  while True:
    # in nodelay model the -1 will return after timeout.
    key = stdscr.getch()
    if key == 27:
      break;

    if key == curses.KEY_UP:
      direction = curses.KEY_UP
    elif key == curses.KEY_RIGHT:
      direction = curses.KEY_RIGHT
    elif key == curses.KEY_DOWN:
      direction = key
    elif key == curses.KEY_LEFT:
      direction = key

    # here is how we move the snake one cell to right
    # Step 1, figure out the new head.
    head = snake[0]
    # decide the direction based on user's input key:
    if direction == curses.KEY_UP:
      new_head = [head[0] - 1, head[1]]
    elif direction == curses.KEY_RIGHT:
      new_head = [head[0], head[1] + 1]
    elif direction == curses.KEY_DOWN:
      new_head = [head[0] + 1, head[1]]
    elif direction == curses.KEY_LEFT:
      new_head = [head[0], head[1] -1]
    # step 2, draw the new head on game board.
    stdscr.addstr(new_head[0], new_head[1], snake_ch)
    # add new head to snake
    snake.insert(0, new_head)
    if new_head != food:
      # step 3, erase the tail from game board.
      stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
      # remove the tail cell from snake.
      snake.pop()
    else:
      food = [
      # the y axis
      random.randint(box[0][0] + 1, box[1][0] - 1),
      # the x axis
        random.randint(box[0][1] + 1, box[1][1] - 1)
      ]
      stdscr.addstr(food[0], food[1], "*")

    if new_head[0] == box [0][0]:
      break;
    if new_head[0] == box [1][0]:
      break;
    if new_head[1] == box [0][1]:
      break;
    if new_head[1] == box [1][1]:
      break;
  stdscr.addstr(sh // 2, sw // 2, "GAME OVER")
  stdscr.nodelay(0)
  stdscr.getch()
curses.wrapper(board)