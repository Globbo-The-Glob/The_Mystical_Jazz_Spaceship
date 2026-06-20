---
layout: payge
title:  "Dam Hydrostatics"
date:   2026-06-20 22:51:38 +0100
categories: jekyll update
permalink: /dam-hydrostatics
---

---
tags:
  - Physics
  - Tutoring
---

# Hydrostatics question on dam
Find hydrostatic thrust
![Pasted image 20241031135702](/images/Pasted image 20241031135702.png)

Forces on the wall are imposed by the vertical pressure of the water above.

This creates a _Pressure Gradient_ down the wall. This will be linear, due to the compounding weight of water above each new bit of depth.

![Pasted image 20241031145915](/images/Pasted image 20241031145915.png)

From pressure equations, the pressure is the force per unit area, so:
$$ F = PA $$ P in this case is caused purely by the water's weight. In fact we can do this as $\bar{P}$. This is the average pressure on the surface. 
Hydrostatic pressure is give by: 

$$ \bar{P} = \rho g \bar{h}$$

Where $\rho$ is the water's density, $g$ is the acceleration due to gravity and $\bar{h}$ is the average depth. 

$$ F = (\rho g (h_0 + h_x) / 2) A $$


It is also possible to do this with an integral: 

$$F = PA$$


$$ dF = PdA$$


$$F_y = \int P dA$$


$$dA = wdy $$


$$ F = w \int^y_0 \rho gydy$$


$$ F = w \rho g[\frac{y^2}{2} - 0]$$

This is essentially the same, but more interesting and demonstrates integral