model SoilPhSensor
  output Real soilPH;
  Modelica.Blocks.Sources.Sine sineSource(
    amplitude=0.5, f=0.01, offset=7);
equation
  soilPH = sineSource.y;
end SoilPhSensor;
