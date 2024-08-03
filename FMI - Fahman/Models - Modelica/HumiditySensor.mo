model HumiditySensor
  output Real humidity;
  Modelica.Blocks.Sources.Sine sineSource(
    amplitude=30, f=0.2, offset=50);
equation
  humidity = sineSource.y;
end HumiditySensor;
