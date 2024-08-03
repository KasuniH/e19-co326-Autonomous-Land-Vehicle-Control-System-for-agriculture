model SoilTemperatureSensor
  output Real soilTemperature;
  Modelica.Blocks.Sources.Sine sineSource(
    amplitude=10, f=0.05, offset=20);
equation
  soilTemperature = sineSource.y;
end SoilTemperatureSensor;
