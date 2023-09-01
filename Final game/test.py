aTan = -math.tan(angle_ray)
if angle_ray < math.pi / 2 or angle_ray > math.pi * 3 / 2:  # looking right
    rayX = (self.playerX // Zoom) * Zoom + Zoom
    rayY = self.playerY + ((self.playerX - rayX) * aTan)
    offsetX = Zoom
    offsetY = -offsetX * aTan
elif angle_ray > math.pi / 2 and angle_ray < math.pi * 3 / 2:  # looking left
    rayX = (self.playerX // Zoom) * Zoom - 0.0001
    rayY = self.playerY + ((self.playerX - rayX) * aTan)
    offsetX = -Zoom
    offsetY = -offsetX * aTan
else:
    rayY = self.playerY
    rayX = self.playerX
    rendist = Render_dist

aTan = -math.tan(angle_ray)
if angle_ray < math.pi / 2 or angle_ray > math.pi * 3 / 2:  # looking right
    rayX = (self.playerX // Zoom) * Zoom - 0.0001
    rayY = self.playerY + ((self.playerX - rayX) * aTan)
    offsetX = -Zoom
    offsetY = -offsetX * aTan
elif angle_ray > math.pi / 2 and angle_ray < math.pi * 3 / 2:  # looking left
    rayX = (self.playerX // Zoom) * Zoom + Zoom
    rayY = self.playerY + ((self.playerX - rayX) * aTan)
    offsetX = Zoom
    offsetY = -offsetX * aTan
else:
    rayY = self.playerY
    rayX = self.playerX
    rendist = Render_dist