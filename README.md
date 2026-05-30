# Astrodynamics Simulator

A modular Python-based aerospace simulation framework built from first principles to study orbital mechanics, rocket launches, and flight dynamics.

The project focuses on understanding the physics behind aerospace systems by implementing numerical integration, guidance logic, environmental models, and mission simulations from scratch without relying on external physics engines.

---

## 🚀 Features

### Numerical Integrators

* Forward Euler
* Runge-Kutta 4th Order (RK4)
* Leapfrog (Symplectic)

### Satellite Module

* Earth-centered orbital propagation
* Earth-Moon three-body simulations
* Single and multiple orbital maneuvers
* Thruster control logic
* Energy and angular momentum tracking
* Orbit animation

### Rocket Module

* Variable-mass rocket dynamics
* Atmospheric drag modeling
* Gravity turn simulation
* PID-based pitch control
* Mission phase management
* Launch telemetry and crash detection

### Solar System Module

* Heliocentric trajectory propagation
* Earth Sphere of Influence (SOI) exit detection
* Automatic Earth-to-Solar handoff

### Telemetry & Visualization

* Real-time mission logging
* Trajectory visualization
* Velocity, altitude, mass, and orbital parameter plots
* Energy and angular momentum diagnostics

---

## 📂 Project Structure

### `/Core/`

Shared simulation infrastructure:

* Numerical integrators
* Gravity models
* Common utilities

### `/Environment_Module/`

Environmental models:

* Atmospheric density
* Aerodynamic drag calculations

### `/Satellite_Module/`

Orbital mechanics simulations:

* Earth-only missions
* Earth-Moon missions
* Orbital maneuvering

### `/Rocket_Module/`

Launch vehicle simulations:

* Variable-mass dynamics
* Guidance and control
* Atmospheric flight

### `/Solar_System_Module/`

Interplanetary mission simulations:

* Solar-centric propagation
* Sphere of Influence transitions

---

## 🛠️ Dependencies

```bash
pip install numpy matplotlib
```

---

## 💻 Usage

### Satellite Simulation

```bash
cd Satellite_Module
python main.py
```

Options:

* Integrator selection
* Earth-only simulation
* Earth-Moon simulation
* Orbital maneuvers

---

### Rocket Simulation

```bash
cd Rocket_Module
python main.py
```

Simulates:

* Launch
* Gravity turn
* Fuel depletion
* Atmospheric ascent
* Guidance and control

---

### Solar System Simulation

```bash
cd Solar_System_Module
python main.py
```

Simulates:

* Earth departure
* SOI transition
* Heliocentric trajectory propagation

---

## 📈 Outputs

The simulator can generate:

* X-Y trajectory plots
* Orbital radius history
* Velocity history
* Mass depletion history
* Energy conservation plots
* Angular momentum conservation plots
* Animated trajectories

---

## 🚧 Current Status

This project is actively under development. Planned future additions include:

* Attitude dynamics
* Advanced guidance algorithms
* Navigation and state estimation
* Autonomous landing systems
* Multi-stage launch vehicles
* Interplanetary mission planning
