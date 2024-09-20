---
layout: payge
title: Vectors - A Pointed Approach
permalink: /blog/maths/vectors/
categories: jekyll update
date:   2024-09-16 16:31:51 +0100
---
Harri, [20/09/2024 20:27]
Vectors are a powerful concept shrouded behind some tricky language. They play such a fundamental role in mathematics and science, but are also very beautiful and I think quite fun. 
I'd like to provide an introduction to a vector that gives a foundation for thinking and using vectors that will hopefully be useful for harder concepts. I will be working through the simple building blocks that form the foundation for so much awesome maths. I will also be mentioning the higher level stuff here and there, to give context and hopefully inspiration as to what these tools can do, as well as providing grounded examples where appropriate to illustrate the concepts.

We will start very simple and build our way up to what a vector is. Then, we can start to think about what we can do with them and that's where the fun begins.
I'll draw some hand drawn images to get my points across too.

A little note, in maths and physics, it's important for both work and communication to be precise in notation, and this can be tricky when the systems we are playing with get abstract. So as we go I will introduce some notation, hopefully in a way that allows you to get to grips with it before I use it a lot. I find it helpful to note these things down and try saying them aloud. Don't worry, we all start somewhere and it comes with practice, I was useless when I started. 

## 1. Spaces 

So to begin, a vector is an object in mathematics. It's something we can use to represent something, anything really, that fits the vector _vibe_. We will get to that, but I don't think you'd see any objects around without somewhere to put them. So we need a _space_ to place our objects in. Something interesting with maths is that the space we define puts restrictions of the nature of objects in them. Think of it like this: 
We can start with a space that's real. In math notation this looks like $$\mathbb{R}^{dim}$$ for $$\mathbb{R}$$eal spaces with a number of $$dim$$ensions.
All the $$\mathbb{R}$$eal part means is that numbers like 1, 2, ,-2, -4.35, 2.1345, $$\sqrt{2}$$, $$\pi$$ and so on, can all live here. 
We have seen a $$\mathbb{R}^1$$ space before, it's called a number line.  See how the 1 has replaced $$dim$$ in our notation? This means the space is 1 dimensional. You'll remember this is a nice way of looking at numbers and we can say that a number like 3 is made of other numbers, like three 1's added together (1+1+1=3).
A space also needs a point of reference, some origin in which we can say things come from, or are measured from. This is called the $$origin$$. In $$\mathbb{R}^1$$, this point is the number 0. 

You have also been using other spaces of higher dimension. First, $$\mathbb{R}^2$$ could be a sheet of paper, with two dimensions. We can draw all around the sheet of paper, but crucially we can't draw up out of a sheet of paper. This is because we live in a 3 dimensional world. It's up for debate whether this is $$\mathbb{R}^3$$ (it's definitely not), but for the sake of existing and doing day to day things, it might as well be with 3 ways you can move: forward/backward, left/right, up/down. .

So you can see that although we are using some funky shorthand to write our maths, we are talking about things that we use everyday. 
After that things get a little nuts, but no less important to how we think about the world. Spaces with 4 dimensions are used in physics for general relativity, which is how gravity works. Higher dimensions than that, we can have very large spaces that can represent how languages work in AI and machine learning and at the ultimate end, quantum mechanics deals with infinite dimensional dimension vector spaces, which is really wild right now but you could easily understand with a bit of practice! We can also have spaces containing different numbers, like complex numbers, which are fancy and a personal favourite of mine. We will talk about them in another writing.

For now, lets hang out in our piece of paper $$\mathbb{R}^2$$. Here we can draw a fair number of cool objects. You could draw a triangle, a square, a little person or a whole map! All of these things as we will see can be described by objects in the space, for example, vectors. For now, be aware that these drawings are not possible on the number line, where we are restricted to forward and backward motions! This is because $$\mathbb{R}^2$$ is where we first start to meet vectors properly\*.

So lets play in $$\mathbb{R}^2$$ for a while, but know that what we talk about here naturally extends up and away to higher dimensions, with some changes here and there. 

## 2.First Vectors
Now a vector, as you will probably hear said a thousand times, is an object with both a magnitude and a direction. This might sound strange, because most things have direction and magnitude, and this is why a lot of things can be described in the language of vectors! But not everything.  There are also _Scalars_, which have a size, but no real direction. They are useful for measuring, like counting the number of marbles in a bag, but not so good for drawing triangles. They do however form a key part of a vector as we will see.

A fantastic way to think of this definition is walking. In front of you is a pond, lets say its distance is 15 steps away. Now to the right of you, again 15 steps away, is a tree. You can walk 15 steps, but the direction you go will matter to whether or not you arrive at the tree or the pond. Both objects are the same distance away, but they have different directions. The scalar here is the number of steps. It is a measurement of the distance. The vector is both the distance and the direction together.  

So a good way to draw vectors at this stage is using an arrow, like this: 

( Vector Image)

And its like a distance in a direction. 

One final bit of our space to describe is also a set of vectors we call a _basis_. A basis is made of a number of vectors, in fact we have one for each of our dimensions.
These vectors are a basis because every single vector in the space can be built from them in combination, like the smallest possible Lego brick.
Each of these vectors has a size 1. You can think of these as sign posts that point out in the directions of each dimension. In our earlier example, one signpost might say "Tree" and the other "Pond".
(Draw)
Lets say each of these signposts is a single stride long so these basis vectors are similar to the number 1 on the number line. Just as we can make 3 by writing 1+1+1 = 3 or 6,503,329 by writing 1+1+1...(6,503,325 more)+1 =  6,503,329, any other vectors can be made up by combining these basis vectors.
These basis vectors are usually given names, depending on what it is the vectors describe. It might be familiar to you to call them $$\mathbf{x}$$ and $$\mathbf{y}$$. This is very standard, $$x$$ usually means across horizontally, and $$y$$ meaning up and down. A very important property of these basis vectors is that they form a very neat square when put together like this: 

basis vector image

This brings up another feature of $$\mathbb{R}^2$$, that our vectors have _angles_ between them. This is a result of having direction, we have a new way of talking about how two vectors compare. Normally, our basis vectors have a solid $$90^\circ$$ angle between them. This is all we will be working with here, although this can change in more complex maths and physics. This is exactly what happens in Einstein's General Relativity, which tells us how gravity works. Let's not worry about that right now, all our basis vectors are arranged so that they are $$90^\circ$$ from each other. 

*\*Note 1.1: We could say that the positive and negative numbers are like directions, in which case we have a 1dimensional vector space, but I think this can be confusing at first. For now, think of vectors as needing angles between them, which is where the distance part comes from. In 1D, this angle is either 0 or 180 deg.   

## 3. General Vectors

So, you might be wondering how a triangle with angles less or more than $$90^\circ$$ can be made from our basis. Further, what if we wanted a tringle with sides longer than 1?  
Well, like I said we can build any vector in $$\mathbb{R}^2$$ from the basis. Lets build a vector now, lets give it a name, like $$v$$ for vector. 
Our vector $$v$$ is going to be made of some bits of $$x$$ and some bits of $$y$$, like this:
$$$$ v = 3x + 4y $$$$ and $$v$$ lives in $$\mathbb{R}^2$$. We can say that mathematically by writing $$v \in \mathbb{R}^2$$ and we can draw it like this:

( Draw v)

Cool, notice how $$v$$ is the hypotenuse of a triangle built connecting the stack of $$x$$ basis vectors and the stack of $$y$$ basis vectors, so straight away we have a triangle.  This is just like lego or minecraft, where we build a path out of little bricks. In this case, our path takes us 3 steps in the direction of $$x$$ to the right, and then we step 4 steps forwards in the direction $$y$$. 
When we look back at the sign post, we see we are between the two sign posts, and if we walked back straight towards the signpost, we would have walked in a triangle.
Remember, $$x$$ and $$y$$ are both vectors themselves, basis vectors to be exact, so what we are doing here is _adding_ vectors. To add vectors, we place them tip to tail: 

(Draw vector adding)

and this is just like following map instructions. 

How about another vector, this time lets have our vector be $$u\in \mathbb{R}^2$$ , because it's next to $$v$$ in the alphabet:
$$$$ u = -3x-4y $$$$
and we can add it to our picture:

(Draw u)

Great. So what can we see with these two vectors. Well first, the numbers attached $$x$$ and $$y$$ tell us how many of each basis we need to build the vectors. We can see from our picture that $$u$$ is pointing the opposite way to $$v$$. This is also seen with the minus signs before the coefficients (those numbers before $$x$$ and $$y$$) when we wrote down $$u$$. However, if we take a ruler and measure both vectors, we see they have the same size.

What would happen if we added these vectors together? Lets do that. 
$$$$ v + u = 3x + 4y - 3x -4y $$$$ group like terms:
$$$$ v + u = 3x -3x +4y - 4y = 0 $$$$ Interesting. Lets draw this out and see what it looks like.
(Draw u + v)
Right, so when we add these two , we think of it like walking along $$v$$ and then along $$u$$, but because $$u$$ is the same size as $$v$$, just pointing the other way. We end up back at the start. 
This is again showing that vectors have direction and magnitude.

We can also scale our vectors. Say we wanted a vector to be twice as long, we could write 
$$$$ 2v = 2(3x + 4y) = 6x + 8y$$$$
(Draw this.)
Nice and easy. The 2 is distributed to each coefficient. What happens if we write:
$$$$ u + 2v ?$$$$
Try drawing a picture and doing the calculation.

Lets introduce another vector, lets call it $$w$$ and write it like: 
$$$$ w = 0.5x + 6y \in \mathbb{R}^2$$$$
$$w$$ also lives in $$\mathbb{R}^2$$, so we can draw it. 
(Draw)
This time, $$w$$ points in a similar direction to $$v$$, which is nice. It also lets us do another neat trick with vectors. What if I wanted to know about the vector $$\vec{vw}$$ ? 
What is that? Well it's just the vector between $$v$$ and $$w$$:
(Draw)
So $$\vec{vw}$$ points from the tip of $$v$$ to the tip of $$w$$. If we think of vectors as paths again, how would we get this path? Well what if we went the long way? We could go back down $$v$$ and up to $$w$$, and we'd be at the tip of $$w$$, same as travelling $$vw$$.
$$$$ \vec{vw} = w - v = 0.5x + 6y - (3x + 4y) $$$$
$$$$              = 0.5x - 3x + 6y - 4y = -2.5x + 2y $$$$ (Draw)
Try this yourself with the vector $$\vec{uw}$$, use the picture to help!  

## 4. Rulers made of math

Its important to measure the direction and magnitude of vectors and we will want ways to do this in maths, because it won't always be possible to get a ruler out and measure them. Luckily, we have nice ways to calculate both!

First, lets start with a vector's size. You hopefully will have encountered the Pythagorean Formula: 
$$$$ c^2 = a^2 + b^2 $$$$
This is an amazing tool, because it gives us a very clean and simple way of calculating the size of a vector. Remember that the Pythagorean Formula tells us the length of a side of a right angle triangle, given the other two. This is exactly what we have in our picture of $$v$$.
Because both our basis vectors $$x$$ and $$y$$ are size 1, the description $$v = 3x + 4y$$ tells us that we have two sides defined, a length 3 side and a length 4 side. In general, a vector's magnitude is written $$|v|$$ which reads like "the magnitude of $$v$$". The triangle looks like this, with $$a$$ being the number before $$x$$, and $$b$$ the number before $$y$$:
(Draw triangle)
All we have to do is calculate: 
$$$$ |v| = \sqrt{a^2 + b^2} $$$$
$$$$ |v| = \sqrt{3^2 + 4^2} = \sqrt{25} = 5 $$$$
You can do this on a calculator, but try it on paper first by calculating $$|u|$$ yourself. 

Notice that $$|u| = |v|$$. The vectors have the same magnitude. 
Can you prove to yourself using this that the basis vectors are magnitude 1 as well? 
As a hint, think of $$x = 1x + 0y$$.

Awesome, we have a way of getting the size of vectors without worrying about pulling out a ruler. This formula is so powerful that it actually works for any higher dimensional space too. Its the same in $$\mathbb{R}^3$$: 
$$$$ vector = ax + by + cz \in \mathbb{R}^3
$$$$ $$$$ |vector| = \sqrt{a^2 + b^2 + c^2}$$$$ and so on into higher dimensions.  

Now all we need to get is the angle between the vectors. This tool is a little more complicated, but very important and equally as powerful, so I am going to take the time to work up to it so that you can understand it well. 

 I want to focus on $$v$$ and $$w$$ for the moment, so lets zoom in to the top right:
(Draw top right)
It's easy to see that an angle, $$\theta$$,  lives between these arrows, and we are going to learn how to measure that angle very soon.
First calculate $$|w|$$, because it's good practice and we will need it later. You'll notice this time it's a different magnitude to $$v$$ and $$u$$.