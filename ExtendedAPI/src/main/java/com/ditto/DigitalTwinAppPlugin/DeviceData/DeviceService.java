package com.ditto.DigitalTwinAppPlugin.DeviceData;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class DeviceService {

    @Autowired
    private DeviceRepository deviceRepository;

    public List<Device> getAllDevices() {
        return deviceRepository.findAll();
    }

    public Optional<Device> getDeviceById(Long id) {
        return deviceRepository.findById(id);
    }

    public Device addDevice(Device device) {
        return deviceRepository.save(device);
    }

    public Device updateDevice(Long id, Device newDevice) {
        return deviceRepository.findById(id)
                .map(device -> {
                    device.setName(newDevice.getName());
                    device.setStatus(newDevice.getStatus());
                    device.setLocation(newDevice.getLocation());
                    return deviceRepository.save(device);
                })
                .orElseGet(() -> {
                    return deviceRepository.save(newDevice);
                });
    }

    public void deleteDevice(Long id) {
        deviceRepository.deleteById(id);
    }
}
