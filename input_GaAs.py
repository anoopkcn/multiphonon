T = 300  # Temperature in K
a_0 = 5.6  # lattice constant in Angstrome
Eg = 1.43  # bandgap in eV
epsilon_l = 13.18  # relative permittivity at low frequency;
epsilon_h = 10.9  # relative permittivity at high frequency
M_eff = 0.067  # effective mass
Mr = 36.11  # reduced mass im amu
Eph = 30E-3  # phonon energy in eV
Dij = 5e8  # deformation potential constant in eV/cm
Nt = 1e15  # trap density in cm^-3
v_th = 1e7  # thermal velocity in cm/s
trap_state = 'don'  # trap state. 'don' for donar, 'acc' for acceptor
sign = 1e-16  # electron capture cross section in cm2 for simple SRH
sigp = 1e-16  # hole capture cross section in cm2 for simple SRH
V_start = 0  # starting bias voltage
V_stop = 1  # last bias voltage
dV = 0.1  # step size of the bias voltage
dE = 1e-3  # energy mesh step size
dir = 'dp'  # 'dp' for deformation potential coupling, 'pc' for polar optical coupling, 'com' for combined coupling
