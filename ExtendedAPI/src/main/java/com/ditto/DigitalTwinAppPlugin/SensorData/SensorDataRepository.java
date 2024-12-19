package com.ditto.DigitalTwinAppPlugin.SensorData;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface SensorDataRepository extends JpaRepository<SensorData, Long> {
//    List<SensorData> findByLocation(String location);
//
//    List<SensorData> findByVehicle(String vehicle);
//
//    List<SensorData> findByLocationAndVehicle(String location, String vehicle);
}
