+++
title = "Coralign: Automated Coronagraph Alignment for Exoplanet Imaging"
date = 2023-11-20
summary = "Coralign is an open-source Python package for the automated alignment and calibration of coronagraphic instruments. It provides a suite of algorithms to precisely align optical components, such as deformable mirrors and masks, which is essential for high-contrast exoplanet imaging."
externalUrl = "https://github.com/nasa-jpl/coralign.git"
showToc = false
+++

![Coronagraph Layout](/assets/coralign_coro_layout.png)

![Center of Energy Method](/assets/coralign_center_of_energy.png)

### The Problem & Motivation:
Directly imaging exoplanets requires extremely high-contrast coronagraphs to suppress starlight, which can be billions of times brighter than the planet. This suppression demands sub-micron alignment precision of optical masks and deformable mirrors (DMs). Manual alignment is slow, error-prone, and lacks repeatability. This package was developed to automate these critical alignment and calibration procedures, ensuring the accuracy and repeatability required for instruments like NASA’s Nancy Grace Roman Space Telescope Coronagraph Instrument.

### Key Features:
**Deformable Mirror (DM) Registration:** Implements algorithms to precisely determine the position, clocking, and scaling of DM actuator grids relative to the optical beam using phase retrieval data.

**Automated Mask Alignment:** Provides routines for the sub-pixel alignment of various coronagraphic masks, including pupil masks (apodizers, Lyot stops) and focal plane masks (occulters).

**Wavefront Flattening:** Uses registered DM positions to correct wavefront errors, decomposing aberrations using Zernike polynomials and allocating corrections to the DMs to achieve a flat starting wavefront.

**Astrometry & Calibration:** Includes functions for astrometric calibration (`occastro`) and plate scale solving (`platesolv`) using DM-generated satellite spots.

### Tech Stack & Implementation:
The package is built in Python, leveraging **NumPy** and **SciPy** for numerical computation and **Astropy** for FITS file I/O. As a contributor, I helped establish a robust software development lifecycle by implementing a comprehensive **unit test suite with `pytest`** (following Test-Driven Development principles) and configuring the **Continuous Integration (CI) pipeline using GitHub Actions** to ensure code reliability.

My contributions to the utility library include implementing core alignment algorithms, such as the model-free **`center_of_energy` method** for focal plane alignment. I also integrated the **OpenCV (`cv2`)** library to provide fast, robust circle and ellipse fitting for mask detection. To improve the project's accessibility and demonstrate key features, I also developed a series of **interactive Jupyter Notebooks** runnable in Google Colab.

### Resources & Citation

[GitHub Repository](https://github.com/nasa-jpl/coralign)

A. J. Eldorado Riggs, **Michael Bertagna**, Garreth J. Ruane, Eric J. Cady, David S. Marx, Sam P. Halverson, Samuel Miller, Kevin J. Ludwick, "Coralign: a software package for coronagraphic alignment and calibration," in _Proc. SPIE 12680, Techniques and Instrumentation for Detection of Exoplanets XI_, 126802F (5 October 2023). [doi:10.1117/12.2677703](https://doi.org/10.1117/12.2677703)