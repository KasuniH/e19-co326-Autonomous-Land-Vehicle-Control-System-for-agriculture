model AirTemperatureSensor
  output Real airTemperature;
  Modelica.Blocks.Sources.Sine sineSource(
    amplitude=15, f=0.1, offset=25);
equation
  airTemperature = sineSource.y;
end AirTemperatureSensor;
