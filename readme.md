# About The Project
This project was created with assistance while I was watching a lesson from Teacher Lira on the Hashtag Programação YouTube channel.

I don’t think there is any merit of my own in this; I personally didn’t create anything here, just copied.

I believe that the learning process is like the description by Kirby Ferguson in his video called "Everything is a Remix," where he explains that to create anything new, the journey involves copying, combining, and transforming.

Based on this, I'm taking my first step.

## Project Explanation
The project consists of two parts: creating the Flappy Bird game and developing the Machine Learning Model that will enable the birds to learn how to pass the game. In this README, I will explain my journey building the project ("if I just copy, maybe I will not learn so much").

## The Flappy Bird Game
We will use three libraries for the game: `pygame`, `random`, and `os`.

If you want to see this project in your computer, you will nedd install the `pygame`:

'''
pip install pygame
'''
The first thing we did was set the screen size to 500x800 pixels.

Next, we created the pattern images for all the objects that we have (the bird, the pipe, the background, and the floor).

We initialized the font and set it to the Arial family with a size of 50px.

### The Bird
Our first object is the bird, which is the hardest object in the code because it has many functions and uses a physics formula to calculate the jump and fall.

In that moment of the code we are defining what the Bird wil do, basically jump and move and draw the bird on the screen.

One very important thing here is defining the bird mask, for the collision don't be based on a square, but in the pixel range of the bird.

### The Pipe
The pipe is more simple than the bird, here we are creating the pipes that will be apear while the bird pass, here has a aditional comment, while i'm creating that game, i realize that the bird does not move forward, only up and down, what really moves forward are the pipes and nothing else, neither the bottom nor the ground, it seemed obvious, but it is very interesting to think about how optics help us in this way. 

The pipe has a random height and base on your height of top pipe, the height of bottom pip is defined.

Like i said, the pipe is the only element who moves, so we need to define that to.

Like the bird, we will draw the pipe on the screen.

At least, we will create the bird collision logic, the more intersting part of a game is that we can lose cause of something, that who make a game fun, the feeling of don't lose or the feeling of win.

### The Floor