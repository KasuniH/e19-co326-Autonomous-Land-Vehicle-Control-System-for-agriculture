model SoilMoistureSensor
  output Real soilMoisture;
  Modelica.Blocks.Sources.Sine sineSource(
    amplitude=50, f=0.1, offset=50);
equation
  soilMoisture = sineSource.y;
end SoilMoistureSensor;
