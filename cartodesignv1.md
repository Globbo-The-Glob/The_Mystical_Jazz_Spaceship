---
layout: payge
title: Design Requirements V1
permalink: /carto/designv1
---

## Display
The display will be eink, due to its low power usage which maps the map more useful. 
The display will be a simple compass, with GPX route data stored. 
Some metrics may be counted using gpx data. 
A challenge is getting a nice local topographic map with contours etc. Ideally it should allow routes to be left and still see locals. 
Display could be 3D with local refresh but for now stick to route on 2D contour map. 

## Hardware
Device would have big battery, and a small amount of memory. The cpu need not be too powerful, but should display maps. 
A good thing about eink is that updating can be done locally, so the marker can be updated quickly with little power consumption. 
The GPS chip will be a key part. 
Buttons need to be minimal and intuitive. The software shouldn't be complicated, most should be handled on pc. 
Maybe 3 buttons, with one being a shift key. 
Rechargable battery
Solar powered!

## Software
Written in Rust
Simple splash
Menu of routes
Route is booted and map drawn, with option to start metric tracking or guidance. 
Way points are marked, and updates are small to save on eink
Ideally a full reshresh should take place every now and again
Line on map will go grey with way points hitto some degree
Routes can be arbitrarily long
A grid can be displayed, and used to select zoom regions
Holds of buttons may be useful. Should be some indication this is happening
A metric page is displayed when root is confirmed ended.
Metrics saved to some format, ideally something strava compatible or something. 

<br>
<a href="https://github.com/Globbo-The-Glob/Carto">GitHub Repo</a>
