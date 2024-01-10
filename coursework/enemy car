self.position = position = Vector2(x, y)
    self.velocity = Vector2(0.0, 0.0)
    self.slip_angle = slip_angle
    self.length = length
    self.max_velocity = 20
    self.brake_deceleration = 10
    self.free_deceleration = 2
    self.initial_velocity = 0

    self.long_acceleration = 0.0
    self.lat_acceleration = 0.0
    self.acceleration = 0.0
    self.steering = 0.0


def update(self, dt):
  self.velocity += (self.acceleration * dt, 0)
  self.velocity.x = max(-self.max_velocity, min(self.velocity.x,          self.max_velocity))
  
  if self.steering:
                  turning_radius = self.length / sin(radians(self.steering))
                  angular_velocity = self.velocity.x / turning_radius
  else:
      angular_velocity = 0

  self.position += self.velocity.rotate(-self.angle) * dt
  self.slip_angle += degrees(angular_velocity) * dt 
