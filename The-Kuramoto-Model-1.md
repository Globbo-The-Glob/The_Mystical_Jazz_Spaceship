---
layout: payge
title:  "Kuramoto Model 1"
date:   2026-03-14 10:31:00 +0100
categories: jekyll update
permalink: /blog/maths/kuro1/
---
Objectives: 
- Understand the motivation for synchronisation models
- Develop the model and show how it is solvable with complex numbers
- Extensions (continuum) and applications
- Coding the model

# Intro
In the 1600s, Christopher Huygens was in the business of sorting out ship clocks. Time keeping had become an important navigational tool, but pendulum clocks often drifted away from accurate time due to the motion of ships. Huygens found that clocks, suspended from the same beam, would begin to _synchronise_ and tick at the same rate. These pendulum clocks were _coupled_, resulting in the rhythmic exchange of energy between them.

Throughout the following centuries, the phenomenon of synchronisation was further developed. All over physics, biology and engineering, synchronisation became a key phenomena of interest.

Despite efforts from researchers, particularly Poincare and Arthur Winfree, the coupled oscillator phenomenon remained out of reach. This was until in 1975 Yoshiki Kuramoto presented a solvable model for coupled oscillators, called the Kuramoto model.

This model has been applied in many different scenarios, including firefly populations, heart cells, neural dynamics, power generators in the national grid, and even quantum computers.

# Model
We will now seek to develop the Kuramoto model, before solving it.

To start, we must first define our oscillators. 
Our oscillators will be _phase oscillators_. The phase $$\theta$$ refers to the angle of a unit vector with the x-axis, and is measured in radians such that $$0 \leq \theta \leq 2\pi$$. 

We can express a population of these oscillators as a number of phases labelled by $$i$$ like $$\theta_i$$ where $$1 \leq i \leq N$$ where $$N$$ is the number of oscillators.

The rate at which the oscillator moves we can call

$$\frac{d\theta_i}{dt}$$

This is the small change in phase of an oscillator $$d\theta_i$$ with a small change in time $dt$.
Each oscillator will have a _natural frequency_ $$\omega_i$$ which will push it around the circle at some speed. We will also add a term that quantifies the degree to which oscillators are apart and a term $K$ which couples them together. Overall, our model has a phase rate of:

$$ \frac{d\theta_i}{dt} = \omega_i + \frac{K}{N}\sum^N_j \sin(\theta_j-\theta_i) $$

This is the Kuramoto model. 
It describes the interactions between oscillators as a term contributing to the change in phase of each oscillator. 
The sin term means that if an oscillator lags another, it will speed up, and if it leads another, it will slow down. 
This is akin to two people running on a track attempting to run at the same speed. 
The coupling term $$K$$ is averaged over the population to normalise the coupling in large $N$ cases. 

# Complex Numbers in the Kuramoto Model
To solve this model, we need to express it in a new way. 
When there is a large degree of synchrony in the population, there is a large coherence between the oscillators and they group up. When they are desynchronised, the population is spread out. We measure this using a complex number, expressed in exponential form:
$$z(t) = r(t)e^{i\psi(t)} = \frac{1}{N}\sum^N_ie^{i\theta_i(t)}$$
What is the benefit of this? Well it allows a new understanding of the oscillator population. The dynamics of the underlying oscillators can be expressed using two numbers: $$r,\psi$$.
We call $$0 \leq r \leq 1$$ the order parameter. If the oscillators are all grouped up, the sum on the right tends to $N$ and when normalised tends to 1.
$$\psi$$ is the group phase, which is the average of the phases. 

Further exploration of this gives the equation:

$$\frac{d\theta_i}{dt} = \omega_i + Kr\sin(\psi-\theta_i)$$

this equation shows an interesting phenomena from physics, which is called _mean field coupling_. In this view of the model, the synchronisation phenomena is driven by an oscillators coupling to the mean field. The order parameter $$r$$ strengthens the mean field's contribution, and the difference of the oscillator is now from the group phase.
This shows that, in the case of the fully connected population, the population dynamics and the individual interactions are the same thing.
