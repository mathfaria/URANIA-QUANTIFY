import math
def weatherBalloonData(balloonType, payloadMass, extraHelium,parachuteRadius):
    balloonMassList = [200, 300, 350, 450, 500, 600, 700, 800, 1000, 1200, 1500, 2000, 3000]  # gr (Kayamont Data)
    burstDiameterList = [300, 378, 412, 472, 499, 602, 653, 700, 786, 863, 944, 1054, 1300]  # cm (Kayamont Data)
    airDensity = 1.225 #Sea level
    Gravity = 9.807 #!!
    sphereDrag = 0.47 #!!
    parachuteDrag = 1.75 #!!
    balloonMass = balloonMassList[balloonType-1] # grams.
    bustDiameter = (burstDiameterList[balloonType-1]) / 100 # meters.
    burstVolume = (4*math.pi*(bustDiameter/2)**3)/3 # cubic meters.
    requiredHelium = (balloonMass + payloadMass + extraHelium) / 1000 # cubic meters.
    totalMass = (balloonMass + payloadMass) / 1000 # kilogram
    initialRadius = math.pow(((3 * requiredHelium) / (4 * math.pi)), 1/3) # meters. (considering a perfect sphere)
    sphereArea = 2*math.pi*(initialRadius**2) # squared meters.
    parachuteArea = 2*math.pi*(parachuteRadius**2) # squared meters.
    ascentSpeed = math.sqrt(2*(airDensity*requiredHelium*Gravity)-(totalMass*Gravity))/(airDensity*sphereArea*sphereDrag) # m/s
    descentSpeed = math.sqrt((2*(payloadMass/1000)*Gravity)/(airDensity*parachuteArea*parachuteDrag)) # m/s
    bustAltitude = -(7238.3*math.log(1/((burstVolume/(requiredHelium))))) #meters 
    return(balloonMass,requiredHelium,ascentSpeed,descentSpeed,bustAltitude)

#exmaple:
Data = weatherBalloonData(6,1200,200,0.5)
print("Balloon mass:", Data[0], "g.")
print("Required Helium:", Data[1], "m³.")
print("Ascent speed:", Data[2], "m/s.")
print("Descent speed:", Data[3], "m/s.")
print("Burst altitude:", Data[4], "m.")