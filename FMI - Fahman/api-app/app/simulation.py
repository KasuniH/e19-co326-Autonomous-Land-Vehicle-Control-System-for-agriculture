from fmpy import simulate_fmu
import threading
import matplotlib.pyplot as plt
import os

current_simulation = None
simulation_thread = None
simulation_result = None

def start_fmu_simulation(fmu_file, start_time, stop_time):
    global current_simulation, simulation_thread, simulation_result

    def run_simulation():
        global current_simulation, simulation_result

        try:
            current_simulation = simulate_fmu(fmu_file, start_time=start_time, stop_time=stop_time)
            simulation_result = current_simulation

            # Plot the results after simulation
            if simulation_result:
                plot_simulation_results(simulation_result)
        except Exception as e:
            print(f"Error during simulation: {e}")

    simulation_thread = threading.Thread(target=run_simulation)
    simulation_thread.start()
    return {"fmu_file": fmu_file, "start_time": start_time, "stop_time": stop_time}

def stop_fmu_simulation():
    global simulation_thread
    if simulation_thread and simulation_thread.is_alive():
        # Note: Actual stopping of simulation depends on FMU capabilities
        simulation_thread.join(timeout=1)
    return {"status": "stopped"}

def get_simulation_status():
    if current_simulation:
        return {"running": True, "result": current_simulation}
    return {"running": False}

def plot_simulation_results(result):
    # Example: Plot the first variable in the result
    time = result['time']
    for variable in result.dtype.names:
        if variable != 'time':
            plt.plot(time, result[variable], label=variable)

    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title('FMU Simulation Results')
    plt.legend()
    plt.show()

# usage:
if __name__ == '__main__':
    fmu_file = r'C:/Users/MOHAMED FAHMAN/AppData/Local/Temp/OpenModelica/OMEdit/Agriculture_System/Agriculture_System.fmu'
    start_time = 0
    stop_time = 10

    # Start the simulation
    start_fmu_simulation(fmu_file, start_time, stop_time)
