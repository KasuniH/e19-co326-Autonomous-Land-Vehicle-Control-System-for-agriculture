package com.ditto.DigitalTwinAppPlugin.SensorData;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "sensor_data")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode
public class SensorData {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;


    private String vehicleId;
    private String vehicleType;


    private String vehicleLocation;
    private double sensor1Reading;
    private double sensor2Reading;
    private double sensor3Reading;
}
