import ephem
from datetime import datetime
 
# Define the observer's location
observer = ephem.Observer()
observer.lat = '41.57586044017277'
observer.long = '24.708720484928566'
 
# Define the date
observer.date = datetime.now()
 
# Define the moon
moon = ephem.Moon()
 
# Calculate the phase of the moon
moon.compute(observer)
 
# Print the phase of the moon
print(moon.moon_phase)
print(moon.moon_phase * 360)
