---
layout: payge
title: Carto Home
permalink: /carto/
---

Carto is a EInk based mapping system. I am building it right now from basic breakout boards, but will eventually build a custom PCB for the hardware.
The low level embedded programming is done in Rust. 

The heart of Carto is a Raspberry Pi Zero 2W, which interfaces with a GPS breakout from Adafruit. 

The software is barebones and designed for simple use and ease of access, with the main focus on reliability and battery life.
The main feature is the eink display, with a custom graphics driver to do partial refresh on the screen. Eink holds images for next to no power, so it is idea for a mapping system where the image needs updating only periodically.

This project will be fully open sourced when complete.

<br>
<a href="https://github.com/Globbo-The-Glob/Carto">GitHub Repo</a>

<br>
## Articles

<br>
## Work Logs 

<br>
## Thinking
<a href="/carto/designv1">Design Requirments v1</a>