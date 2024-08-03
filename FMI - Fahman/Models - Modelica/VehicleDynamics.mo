model VehicleDynamics
  // Parameters
  parameter Real mass = 500; // mass of the vehicle in kg
  parameter Real wheelRadius = 0.3; // radius of wheels in meters
  parameter Real kFriction = 0.1; // friction coefficient

  // Variables
  Real velocity; // velocity of the vehicle
  Real position; // position of the vehicle
  Real appliedForce; // force applied to the vehicle
  Real frictionForce; // frictional force experienced by the vehicle

  // Control input (force applied to the vehicle)
  input Real inputForce;

  // Outputs
  output Real currentPosition;

  // Define equations for dynamics
  equation
    // Newton's second law for linear motion
    mass * der(velocity) = appliedForce - frictionForce;
    velocity = der(position);
    appliedForce = inputForce;
    frictionForce = kFriction * velocity;

    // Define the output as the current position
    currentPosition = position;
end VehicleDynamics;
