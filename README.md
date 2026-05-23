# Astrodynamics Simulator

A modular, Python-based astrodynamics and physics engine built to simulate orbital mechanics, satellite trajectories, and variable-mass rocket launches. 

This simulator is written entirely from scratch using fundamental physics and numerical methods, completely avoiding black-box physics engines. It features custom numerical integrators, environmental models, and multi-body gravitational systems.

## 🚀 Features

* **Custom Numerical Integrators:** * Runge-Kutta 4th Order (RK4)
  * Leapfrog Integration (Symplectic)
  * Forward Euler
* **Orbital Mechanics (Satellite Module):**
  * 2-Body Problem (Earth-only system)
  * 3-Body Problem (Earth-Moon system)
  * Active orbital maneuvering and thruster control logic.
  * Conservation tracking (Energy and Angular Momentum).
* **Launch Dynamics (Rocket Module):**
  * Variable mass kinematics (Tsiolkovsky rocket equation principles).
  * Programmatic pitch/guidance control.
  * Atmospheric drag modeling with exponential air density calculations.
* **Data Visualization:** Built-in Matplotlib plotting for 2D spatial trajectories, mass depletion, velocity, and orbital radii over time.

## 📂 Project Structure

* `/Core/` - Base physics calculations, gravity models, and shared numerical integrators.
* `/Environment_Module/` - Atmospheric physics, including surface density and exponential drop-off functions for drag calculations.
* `/Rocket_Module/` - Simulates a rocket launch from Earth. Handles variable mass, continuous thrust profiles, atmospheric drag, and automated guidance algorithms.
* `/Satelite_Module/` - Simulates orbital trajectories. Allows switching between Earth-only and Earth-Moon gravitational models, complete with orbital maneuver controllers.

## 🛠️ Dependencies

This project relies on standard scientific Python libraries. 

```bash
pip install numpy matplotlib
```

## 💻 Usage

To run a simulation, navigate to the desired module and execute its `main.py` file.

**For the Satellite/Orbital Simulation:**
```bash
cd Satelite_Module
python main.py
```
*The command line interface will prompt you to select your desired numerical integrator (Euler, RK4, or Leapfrog) and your gravitational model (Earth-only or Earth-Moon).*

**For the Rocket Launch Simulation:**
```bash
cd Rocket_Module
python main.py
```
*You will be prompted to select an integrator before the engine propagates the launch sequence, thrust depletion, and gravity turn.*

## 📈 Visual Outputs

The simulator automatically generates dashboard-style plots upon completion of a run, providing analytical insights into:
* **X-Y Trajectory** (scaled to Earth/Moon positions)
* **Orbital Energy & Angular Momentum** (to verify integrator stability)
* **Velocity & Mass vs. Time** (for launch profiles)

## 🚧 Development Status
This project is still evolving! Suggestions for improvement, code contributions, and feedback on the physical models are highly encouraged.
