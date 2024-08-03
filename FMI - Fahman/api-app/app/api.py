from flask import Blueprint, jsonify, request
from .simulation import start_fmu_simulation, stop_fmu_simulation, get_simulation_status

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def index():
    return "Welcome to the FMU Simulation API!"

@api_bp.route('/start_simulation', methods=['POST'])
def start_simulation():
    data = request.json
    fmu_file = data.get('fmu_file')
    start_time = data.get('start_time', 0)
    stop_time = data.get('stop_time', 10)

    # Call the function to start the simulation
    result = start_fmu_simulation(fmu_file, start_time, stop_time)
    return jsonify({"message": "Simulation started", "result": result})

@api_bp.route('/stop_simulation', methods=['POST'])
def stop_simulation():
    # Call the function to stop the simulation
    result = stop_fmu_simulation()
    return jsonify({"message": "Simulation stopped", "result": result})

@api_bp.route('/simulation_status', methods=['GET'])
def simulation_status():
    # Call the function to get simulation status
    status = get_simulation_status()
    return jsonify(status)
