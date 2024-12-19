package com.ditto.DigitalTwinAppPlugin.SensorData;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/extended/sensors")
public class SensorDataController {

    @Autowired
    private SensorDataService sensorDataService;

    // Get all sensor data
    @GetMapping("/{location}/{vehicle}")
    public List<SensorData> listAllSensorData(@PathVariable(required = false) String location, @PathVariable(required = false) String vehicle) {
        if (location != null && vehicle != null) {
            return sensorDataService.getSensorDataByLocationAndVehicle(location, vehicle);
        } else if (location != null) {
            return sensorDataService.getSensorDataByLocation(location);
        } else if (vehicle != null) {
            return sensorDataService.getSensorDataByVehicle(vehicle);
        } else {
            return sensorDataService.getAllSensorData();
        }
    }

    // Get sensor data by ID
    @GetMapping("/{id}")
    public ResponseEntity<SensorData> getSensorDataById(@PathVariable Long id) {
        Optional<SensorData> sensorData = sensorDataService.getSensorDataById(id);
        return sensorData.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    // Create new sensor data
    @PostMapping
    public ResponseEntity<SensorData> createSensorData(@RequestBody SensorData sensorData) {
        SensorData createdSensorData = sensorDataService.saveSensorData(sensorData);
        return ResponseEntity.ok(createdSensorData);
    }

    // Update existing sensor data
    @PutMapping("/{id}")
    public ResponseEntity<SensorData> updateSensorData(@PathVariable Long id, @RequestBody SensorData sensorData) {
        Optional<SensorData> existingSensorData = sensorDataService.getSensorDataById(id);
        if (existingSensorData.isPresent()) {
            // Update the existing sensorData object with the new data
            SensorData updatedSensorData = existingSensorData.get();
            // Update fields based on the request body (sensorData)
            updatedSensorData.setVehicleId(sensorData.getVehicleId());
            updatedSensorData.setVehicleType(sensorData.getVehicleType());
            updatedSensorData.setVehicleLocation(sensorData.getVehicleLocation());
            updatedSensorData.setSensor1Reading(sensorData.getSensor1Reading());
            updatedSensorData.setSensor2Reading(sensorData.getSensor2Reading());
            updatedSensorData.setSensor3Reading(sensorData.getSensor3Reading());

            sensorDataService.saveSensorData(updatedSensorData);
            return ResponseEntity.ok(updatedSensorData);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    // Delete sensor data by ID
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteSensorData(@PathVariable Long id) {
        sensorDataService.deleteSensorData(id);
        return ResponseEntity.noContent().build();
    }
}