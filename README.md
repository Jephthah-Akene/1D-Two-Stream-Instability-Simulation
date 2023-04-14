# 1D-Two-Stream-Instability-Simulation

This project simulates the 1D Two-Stream Instability in a plasma using the Particle-In-Cell (PIC) method. The code calculates the motion of electrons under the Poisson-Maxwell equation.

## Table of Contents

- [1D-Two-Stream-Instability-Simulation](#1d-two-stream-instability-simulation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Dependencies](#dependencies)
  - [Usage](#usage)
  - [Simulation Parameters](#simulation-parameters)
  - [Results](#results)
  - [References](#references)

## Introduction

The Particle-In-Cell (PIC) method is a numerical technique for simulating plasmas. This project demonstrates a 1D simulation of the Two-Stream Instability, a well-known phenomenon in plasma physics. The instability arises when two oppositely directed beams of charged particles interact with each other.

## Dependencies

The project requires the following Python packages:

- NumPy
- Matplotlib
- SciPy

Install these dependencies using `pip`: `pip install numpy matplotlib scipy`


## Usage

To run the simulation, execute the Python script: `python plasma_pic_simulation.py`


The script will run the simulation and display real-time plots of the particle positions and velocities. At the end of the simulation, a figure will be saved to the working directory as 'pic.png'.

## Simulation Parameters

You can customize various simulation parameters by modifying the following variables in the `main()` function:

- `N`: Number of particles
- `Nx`: Number of mesh cells
- `t`: Current time of the simulation
- `tEnd`: Time at which simulation ends
- `dt`: Timestep
- `boxsize`: Periodic domain [0, boxsize]
- `opening_size`: Opening size in the wall at the center of the domain
- `n0`: Electron number density
- `vb`: Beam velocity
- `vth`: Beam width
- `A`: Perturbation
- `plotRealTime`: Toggle real-time plotting (True or False)

## Results

The simulation generates a real-time plot of the particle positions and velocities, with half of the particles colored blue and the other half colored red. After the simulation has completed, a final figure is saved as 'pic.png' in the working directory.

## References

This project builds upon the work done by Philip Mocz "Create Your Own Plasma PIC Simulation (With Python)". Looking forward to building more complex simulations


