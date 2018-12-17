# Quantify (for weather balloons)
## [+] About:
#### Hello! I created this Python function to help scientists and hobbyist to calculate useful data about weather balloons!
#### We used a lot of math and physics formulas to calculate those values, but some of them doesn't work so well, like "ascent speed", if you want to get a precise value, I recommend this site: http://tools.highaltitudescience.com/#. This program is _open-source_, so feel free to edit something if you think that it could improve the performance!
## [+] Math formulas:
#### _Required helium_: We know that Helium can lift 1 gram per liter. It means that the minimum Helium amount could be calculated if you sum the mass of the Payload and the Balloon. If you just do it, the balloon won't move, you have to add some extra-Helium, that's called "Positive Lift", so:
##### > Required Helium = PayloadMass + BalloonMass + PositiveLift.
#### _Ascent speed_: In physics, we can explain a balloon floating by "buoyancy force", so we can calculate balancing the _Buoyancy force_ and the _Weight force_, but we also have the air resistance, so i think we can calculate this way:
##### > Ascent speed = ![](https://i.imgur.com/6KpKbI4.png) 
#### _Descent speed_: That's simple, you just have to consider weight and air resistance!
##### > Descent speed = ![](https://i.imgur.com/54TKmCq.png) 
#### _Burst altitude_: You can know more about it in this site: [Click here!](https://www.launchwithus.org/lwu-blog/2016/6/26/near-space-balloon-burst-altitude-calculator-sceience)


Where: _d_ = Air density. _V_ = Helium volume. _G_ = Gravity. _A_ = Contact area. _Cx_ = Drag.
