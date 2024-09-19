# r"\Prozessorinformationen(_Total)\% Prozessorleistung"
# r"\Prozessor(_Total)\Prozessorzeit (%)"
import Cpu_frequency
import psutil
"""
# Create Dictionary for Monitoring Values:
CPU_Monitor = {"Frequency": int(Cpu_frequency.get_cpu_frequency()),
               "Usage" : psutil.cpu_percent()}
print(CPU_Monitor)

# Insert something to read the CPU Temperature:

from wmi import WMI


wmi = WMI()
for index, probe in enumerate(wmi.Win32_TemperatureProbe()):
    print(index, probe.CurrentReading)
"""
import clr

openhardwaremonitor_hwtypes = ['Mainboard', 'SuperIO', 'CPU', 'RAM', 'GpuNvidia', 'GpuAti', 'TBalancer', 'Heatmaster', 'HDD']
openhardwaremonitor_sensortypes = ['Voltage', 'Clock', 'Temperature', 'Load', 'Fan', 'Flow', 'Control', 'Level', 'Factor', 'Power', 'Data', 'SmallData']

def initialize_openhardwaremonitor():
    file = "OpenHardwareMonitorLib"

    clr.AddReference(file)

    from OpenHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.MainboardEnabled = True
    handle.CPUEnabled = True
    handle.RAMEnabled = True
    handle.GPUEnabled = True
    handle.HDDEnabled = True

    handle.Open()

    return handle

def fetch_stats(handle):
    for i in handle.Hardware:
        i.Update()
        for sensor in i.Sensors:
            parse_sensor(sensor)

            for j in i.SubHardware:
                j.Update()
                for subsensor in j.Sensors:
                    parse_sensor(subsensor)

def parse_sensor(sensor):
    hardwaretypes = openhardwaremonitor_hwtypes

    if sensor.Value is not None:
        # if str(sensor.SensorType) == "Temperature":
        print(u"%s: '%s'   Sensor: #%i %s - %s "
              % (
                  hardwaretypes[sensor.Hardware.HardwareType],
                  sensor.Hardware.Name,
                  sensor.Index,
                  sensor.Name,
                  sensor.Value,
              )
              )


print("OpenHardwareMonitor: ", end='\n\n')
HardwareHandle = initialize_openhardwaremonitor()
fetch_stats(HardwareHandle)