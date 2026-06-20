---
layout: payge
title:  "Integration"
date:   2026-06-20 22:57:42 +0100
categories: jekyll update
permalink: /integration
---

---
tags:
  - Tutoring
  - Maths
---
# 1. Area Under Curves

Often it is desirable to find the area under a function. This can apply in physics, for example in work. 
Work is given by:
$$
W = Fx
$$
which involves a product between the force and displacement which looks like an area in a $F,x$ graph. 
What if our Force was to vary as a function of x:

$$F = F(x) \to W=?$$

This can be achieved by integrating, as we will see. 
Integration is essentially a sum of infinitesimal areas.
We will see how this takes shape, but first lets consider the first example with constant force.

If we had a constant force, our graph might look something like this:

![constantgraph](/images/constantgraph.png)

Between any $a,b$ pair we could simply use$$ W = F(b-a)$$as work. This is just the area under the graph.
We could call $(a-b) = \Delta x$ to demonstrate an arbitrary interval.
$$
W=F\Delta x
$$
If we wanted to find the are under a linear function, we might try something like the below example:

![lineararea](/images/lineararea.png)

If we call the base of each rectangle $\Delta x = (x_{2}=x_{1})$ we can say that the area under our function would look like this: $$
W = \sum^b_{a} F\left( \frac{x_{2}-x_{1}}{2} \right)\Delta x 
$$
This essentially says that we take the area of each rectangle and add them up between our interval $a \to b$. The height of each rectangle is then the height of the Force function at the midpoint of the interval. 
This works well in the linear case, as every part which overshoots the function is compensated for by a part missed (Look closely at the rectangles around the line, the triangles are congruent).
When taking about arbitrarily curvy (but still smooth) functions like any $F(x)$ we need to deal with calculus to find the result.
In calculus we imagine taking these intervals like $\Delta x$ and shrinking them down to the tiniest possible interval. We call this $dx$ which means a tiny step in x. 
The areas become like very thin sticks, with height $F(x)$ at each value of $x$. We can say this because our interval is so small. 
Our work function now looks fairly similar to before, but now we are in the world of calculus. 
$$
\int_{a}^b F(x) dx = W
$$
Here the integral means "infinite sum". The $dx$, our infinitesimal interval, is multiplied by the value $F(x)$ to give our extremely thin areas. When we sum them up, we get the area under a curve, which is our work $W$.

Below is a nice example of this happening:

![riemannsums](/images/riemannsums.gif)

Imagine this process occurring until the rectangles are so thin they look like a solid shading under the graph. 

# 2. Antiderivatives and the Fundamental Theorem 
---
The anti derivative is the inverse operation of differentiation. The question:
``What function when differentiated gives the function?
Integration gives this result.

For example:
$$
 4t^2 - \frac{1}{3}t^3 + C  = \int 8t - t^2 dt
$$
As 
$$
\frac{d}{dt}\left( 4t^2 - \frac{1}{3}t^3 +C \right) = 8t - t^2
$$
The derivative of a constant, $C$ is always 0:
$$
\frac{d}{dx}C = 0
$$
In general, every constant is valid for $C$ as the constant simply shifts the curve up, and does not affect the curvature.
If given bounds, say $0 \to T$, we can find $C$ using the lower bound $0$.
At the lower bound, the integral should equal $0$ as no area has been calculated in a interval of $0$ width. In this case: 
$$
\int^0_{0} 8t-t^2 = 0

$$
In general, the area of a bounded function is equal to the antiderivative plus this constant. To find the constant we subtract from the antiderivative the value of the lower bound:
$$
\int^T_{0} t(8-t) = \left( 4T^2 - \frac{1}{3}T^3 \right) - \left(4(0)^2 - \frac{1}{3}(0)^3 \right) 
$$

This first term on the RHS is the antiderivative. The second term means that when $T=0$, the area calculated by the integral is $0$. It may be worth convincing yourself this is true both algebraically and graphically. Set $T=0$ and see what value the RHS takes. 

### The Fundamental Theorem of Calculus
In general, if 

$$ \frac{dF}{dx}(x) = f(x)$$


For an arbitrary function $f(x)$ and its antiderivative $F(x)$, the integral only needs to be defined by the bounds of the integral such that
$$
\int ^b_{a}f(x) = F(b) - F(a)
$$

This is the fundamental theorem of calculus and underpins much of modern mathematical science. 

# 3.  Inverse Chain Rule and Substitution
The chain rule in derivatives allows for the integration of multiple functions, especially nested functions.
$$
y = f(g(x))
$$
$$

\frac{dy}{dx} = f'(g(x)) \cdot g'(x)
$$
The chain rule can be seen as an extension of the simple statement:
$$
\frac{dy}{dx} = \frac{df}{dg} \frac{dg}{dx}
$$
This allows us to solve may problems.
When doing integration, we are interested in unpicking the chain rule to find a functions antiderivative.
This requires some intuition but can be clearly seen via substitution:
Integrate a function that takes the form of the chain rule:
$$
\int f(g(x))g'(x) dx
$$
substitute u = g into the equation and change the subject of the integral:
$$
\frac{du}{dx} = g'(x) \to du = \frac{g'(x)}{dx}  
$$
Which we can substitute into our original integral to get 
$$
\int f(u)du
$$
This is now a standard integral which can be easily solved to give $f$ in terms of $u$. Upon finding the antiderivative, we simply substitute $u = g(x)$ back into the equation. 

# 4. By Parts
Integration by parts is essentially the inverse of the product rule. 
$$
(fg)' = fg'+gf'
$$
When we integrate this we first write:
$$
\int(fg)' = \int fg' + \int gf'
$$
Then the LHS has the integral and derivative cancel.
$$
fg = \int fg' + \int gf'
$$
This can then be rearranged to give:
$$
\int fg' = fg - \int gf' 
$$Integration by parts allows for the solving of products in integration that can't otherwise be solved via substitution. 

# Numerical Integration

We can do integration _analytically_, as we have above, or we can do it _numerically_. Computers will use numerical integration techniques to approximate integration results. We will see how we can get adequate accuracy from these techiques.

## Common Numerical Methods

### 1. Trapezoidal Rule
- **Concept**: Approximates the area under the curve as a series of trapezoids.
- **Formula**:  
  $$
  \int_a^b f(x) \, dx \approx \frac{h}{2} \left[ f(x_0) + 2f(x_1) + 2f(x_2) + \dots + 2f(x_{n-1}) + f(x_n) \right]
  $$  
  where $h = \frac{b - a}{n}$ is the step size, and $x_0, x_1, \dots, x_n$ are equally spaced points.
- **Use Case**: Simple to implement but less accurate for highly oscillatory functions.

---

### 2. Simpson's Rule
- **Concept**: Uses parabolic arcs instead of straight lines to approximate the area.
- **Formula**:  
  $$
  \int_a^b f(x) \, dx \approx \frac{h}{3} \left[ f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \dots + 2f(x_{n-2}) + 4f(x_{n-1}) + f(x_n) \right]
  $$  
  where $h = \frac{b - a}{n}$ is the step size, and $n$ must be even.
- **Use Case**: Generally more accurate than the Trapezoidal Rule for smooth functions.

---

### 3. Monte Carlo Integration
- **Concept**: Utilizes random sampling to estimate the integral.
- **Formula**:  
  $$
  \int_a^b f(x) \, dx \approx (b - a) \cdot \frac{1}{N} \sum_{i=1}^N f(x_i)
  $$  
  where $x_i$ are random points uniformly distributed in $[a, b]$, and $N$ is the number of samples.
- **Use Case**: Particularly useful for high-dimensional integrals where traditional methods become computationally expensive.

---
# Q.  Combination Exercises

`` Soultions below!

### **Question 1**
Evaluate the following integral:
$$
\int (3x^2 + 4x - 5) \, dx
$$

---

### **Question 2**
Use integration by substitution to evaluate:
$$
\int x \sqrt{2x^2 + 3} \, dx
$$

---

### **Question 3**
Evaluate the following integral using integration by parts:
$$
\int x^2 \ln x \, dx
$$

---

### **Question 4**
Evaluate the following integral using partial fractions:
$$
\int \frac{3x + 5}{(x + 1)(x^2 + 4)} \, dx
$$

---

### **Question 5**
Evaluate the following integral using trigonometric identities and substitution:
$$
\int \sin^3 x \cos^2 x \, dx
$$

---
# A. Solutions

**Question 1**:
   $$
   \int (3x^2 + 4x - 5) \, dx = x^3 + 2x^2 - 5x + C
   $$

**Question 2**:
   Let $u = 2x^2 + 3$, then $du = 4x \, dx$. The integral becomes:
   $$
   \frac{1}{4} \int \sqrt{u} \, du = \frac{1}{6} (2x^2 + 3)^{3/2} + C
   $$

**Question 3**:
   Use integration by parts with $u = \ln x$ and $dv = x^2 \, dx$. The result is:
   $$
   \frac{x^3}{3} \ln x - \frac{x^3}{9} + C
   $$

**Question 4**:
   Decompose into partial fractions:
   $$
   \frac{3x + 5}{(x + 1)(x^2 + 4)} = \frac{A}{x + 1} + \frac{Bx + C}{x^2 + 4}
   $$
   Solve for $A, B, C$, then integrate term by term.

**Question 5**:
   Rewrite $\sin^3 x$ as $\sin x (1 - \cos^2 x)$, then use substitution $u = \cos x$. The integral becomes:
   $$
   \int \sin x (1 - \cos^2 x) \cos^2 x \, dx = -\int (1 - u^2) u^2 \, du
   $$
   Integrate and substitute back. 