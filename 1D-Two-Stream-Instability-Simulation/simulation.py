import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve

"""
Create Your Own Plasma PIC Simulation (With Python)
Philip Mocz (2020) Princeton Univeristy, @PMocz

Simulate the 1D Two-Stream Instability
Code calculates the motions of electron under the Poisson-Maxwell equation
using the Particle-In-Cell (PIC) method

"""


def getAcc( pos, Nx, boxsize, n0, Gmtx, Lmtx ):
    """
    Calculate the acceleration on each particle due to electric field
    pos      is an Nx1 matrix of particle positions
    Nx       is the number of mesh cells
    boxsize  is the domain [0,boxsize]
    n0       is the electron number density
    Gmtx     is an Nx x Nx matrix for calculating the gradient on the grid
    Lmtx     is an Nx x Nx matrix for calculating the laplacian on the grid
    a        is an Nx1 matrix of accelerations
    """
    # Calculate Electron Number Density on the Mesh by 
    # placing particles into the 2 nearest bins (j & j+1, with proper weights)
    # and normalizing
    N          = pos.shape[0]
    dx         = boxsize / Nx
    j          = np.floor(pos/dx).astype(int)
    jp1        = j+1
    weight_j   = ( jp1*dx - pos  )/dx
    weight_jp1 = ( pos    - j*dx )/dx
    jp1        = np.mod(jp1, Nx)   # periodic BC
    n  = np.bincount(j[:,0],   weights=weight_j[:,0],   minlength=Nx);
    n += np.bincount(jp1[:,0], weights=weight_jp1[:,0], minlength=Nx);
    n *= n0 * boxsize / N / dx 
    
    # Solve Poisson's Equation: laplacian(phi) = n-n0
    phi_grid = spsolve(Lmtx, n-n0, permc_spec="MMD_AT_PLUS_A")
    
    # Apply Derivative to get the Electric field
    E_grid = - Gmtx @ phi_grid
    
    # Interpolate grid value onto particle locations
    E = weight_j * E_grid[j] + weight_jp1 * E_grid[jp1]
    
    a = -E

    return a
    

def main():
    """ Plasma PIC simulation """
    
    # Simulation parameters
    N         = 40000   # Number of particles
    Nx        = 400     # Number of mesh cells
    t         = 0       # current time of the simulation
    tEnd      = 50      # time at which simulation ends
    dt        = 1       # timestep
    boxsize   = 50      # periodic domain [0,boxsize]
    n0        = 1       # electron number density
    vb        = 3       # beam velocity
    vth       = 1       # beam width
    A         = 0.1     # perturbation
    plotRealTime = True # switch on for plotting as the simulation goes along
    
    # Generate Initial Conditions
    np.random.seed(42)            # set the random number generator seed
    # construct 2 opposite-moving Guassian beams
    pos  = np.random.rand(N,1) * boxsize  
    vel  = vth * np.random.randn(N,1) + vb
    # Create Gmtx and Lmtx matrices
    Gmtx, Lmtx = create_matrices(Nx, boxsize)

    # Run the simulation
    while t < tEnd:
        # Calculate accelerations
        a = getAcc(pos, Nx, boxsize, n0, Gmtx, Lmtx)
        
        # Update positions and velocities using the calculated accelerations
        pos += dt * vel
        vel += dt * a
        
        # Periodic boundary conditions for positions
        pos = np.mod(pos, boxsize)
        
        # Increment the time
        t += dt

        # Plot or save the data at desired intervals
        if plotRealTime:
            plot_data(pos, vel, t, boxsize, Nx)

    # Plot or save the final state of the system
    if not plotRealTime:
        plot_data(pos, vel, t, boxsize, Nx)

def create_matrices(Nx, boxsize):
    # Create Gmtx and Lmtx matrices
    dx = boxsize / Nx
    Gmtx = sp.diags([-1, 1], [0, 1], shape=(Nx, Nx)) / dx
    Lmtx = sp.diags([1, -2, 1], [-1, 0, 1], shape=(Nx, Nx)) / (dx ** 2)
    Lmtx = Lmtx + sp.diags([1, 1], [-Nx + 1, Nx - 1], shape=(Nx, Nx)) / (dx ** 2)

    # Convert Gmtx and Lmtx to CSR format
    Gmtx = Gmtx.tocsr()
    Lmtx = Lmtx.tocsr()

    return Gmtx, Lmtx


def plot_data(pos, vel, t, boxsize, Nx):
    plt.figure(figsize=(12, 6))

    plt.subplot(121)
    plt.hist(pos, bins=Nx, range=(0, boxsize), color='b', alpha=0.5, label='Particle positions')
    plt.xlabel('x')
    plt.ylabel('Particle count')
    plt.title(f'Time: {t:.2f}')

    plt.subplot(122)
    plt.scatter(pos, vel, s=1, color='r', alpha=0.5, label='Particle velocities')
    plt.xlabel('x')
    plt.ylabel('v')
    plt.title(f'Time: {t:.2f}')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
