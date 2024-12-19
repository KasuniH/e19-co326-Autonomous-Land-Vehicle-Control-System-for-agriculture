package com.ditto.DigitalTwinAppPlugin.SensorData;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.List;
import java.util.Optional;

@Service
public class SensorDataService {

    @Autowired
    private SensorDataRepository sensorDataRepository;

    public List<SensorData> getAllSensorData() {
        return sensorDataRepository.findAll();
    }

    public Optional<SensorData> getSensorDataById(Long vehicleId) {
        return sensorDataRepository.findById(vehicleId);
    }

    public SensorData saveSensorData(SensorData sensorData) {
        return sensorDataRepository.save(sensorData);
    }

    public void deleteSensorData(Long vehicleId) {
        sensorDataRepository.deleteById(vehicleId);
    }

    public List<SensorData> getSensorDataByLocation(String location) {
        return Collections.emptyList();
    }

    public List<SensorData> getSensorDataByVehicle(String vehicle) {
        return Collections.emptyList();
    }

    public List<SensorData> getSensorDataByLocationAndVehicle(String location, String vehicle) {
        return Collections.emptyList();
    }
}
