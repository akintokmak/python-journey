# Day 20: Snake Game - Part 1 (Movement & Body) 🐍

This is the first stage of the legendary Snake Game project. The focus of this part was building the core engine and the complex movement logic of the snake.

## 🚀 Features Implemented
- **Body Construction:** Created a segmented snake body using a list of Turtle objects.
- **Animation Control:** Used `screen.tracer(0)` and `screen.update()` to ensure smooth, flicker-free movement.
- **Movement Logic:** Implemented a "linked-movement" system where each segment follows the position of the one ahead of it.
- **Controls:** Integrated event listeners for `Up`, `Down`, `Left`, and `Right` arrow keys, preventing illegal 180-degree turns.

## 🏗️ Technical Highlight: The Movement Engine
The most challenging part was ensuring the tail followed the head correctly. Instead of moving each segment forward, I moved each segment to the position of the previous segment in reverse order, starting from the tail.

```python
# Movement Logic Snippet
for seg_num in range(len(segments) - 1, 0, -1):
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()
    segments[seg_num].goto(new_x, new_y)
head.forward(20)