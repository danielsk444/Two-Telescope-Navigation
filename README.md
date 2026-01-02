Quick start

Clone the repository:

git clone https://github.com/danielsk444/Two-Telescope-Navigation


Install dependencies:

python -m pip install -r requirements.txt


Run the main simulation:

python main.py

Core dependencies

The code is written in Python (Python ≥ 3.x) and relies primarily on the following third-party packages:

numpy

scipy

pandas

matplotlib

healpy

cartopy

scikit-learn

seaborn

openpyxl

Additional standard Python libraries are used internally.

Data

Gravitational-wave strain data and related products used by this code are publicly available from the Gravitational Wave Open Science Center (GWOSC).
This repository contains the simulation and analysis code only; large data products are not stored in the repository.

Reproducibility

To ensure reproducibility, users are encouraged to cite the specific Git commit hash or GitHub release tag corresponding to the version of the code used to generate the results.

Data sources

The following publicly available datasets were used in this work:

Gravitational-wave sky maps

Sky localization FITS files (e.g. S230529ay.fits.gz, S230606d.fits.gz, etc.) were obtained from the LIGO/Virgo/KAGRA Gravitational-Wave Candidate Event Database (GraceDB):
https://gracedb.ligo.org/

SNR–credible area curves

Files used to construct the 90% credible area versus SNR relations (e.g. 29.csv, 32.csv, 38.csv, 49.csv, 56.csv, 1024.csv) were obtained from the GstLAL early-warning GW data release:
https://gstlal.docs.ligo.org/ewgw-data-release/data.html

Detector noise curves

Detector noise power spectral density curves (NoiseO3.txt, NoiseO4.txt, NoiseO5.txt) were obtained from the LIGO Document Control Center (DCC):
https://dcc.ligo.org/LIGO-T2000012/public

All datasets listed above are publicly available. Large data products are not stored directly in this repository.
