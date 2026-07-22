# Main-text figure inputs

This directory contains compact final values read by the public main-text plotting notebooks. It does not include or replace the third-party raw data used by the full analysis.

## Contents

- `figure1/`: final NPPeco maps, a global monthly series, and a trailing 12-month global series (`global_annual.csv`).
- `figure2/`: model-comparison values for panels A-D and the numeric path values used to check the manually assembled PowerPoint panels E-H.
- `figure3/`: reference deficit frequency, the non-Antarctic analysis land mask used for area statistics, four seasonal NPPeco maps, and eight regional time series.
- `figure4/`: three baseline-risk maps and twelve monthly NPPeco anomaly maps.
- `world_simplified.geojson`: simplified Natural Earth country outlines used for offline plotting. Natural Earth data are in the public domain.
- `manifest.json`: file sizes, SHA-256 checksums, and common grid information.

Spatial arrays use EPSG:4326 on the manuscript 0.1-degree grid from 60 degrees south to 80 degrees north. Variable-specific packing metadata, when used, are stored in each NetCDF file's encoding. Figure 3 deficit frequency is retained as float32 so threshold statistics remain reproducible. Using geodetic cell-area weights and `land_mask` as the denominator, `Dfreq >= 1/12` covers 43.9% and `Dfreq > 1/6` covers 34.1% of non-Antarctic land.

Start Jupyter in `notebooks/` and run `D2_sem_plots.ipynb`, `D3_richness_risk.ipynb`, and `D4_main_figures.ipynb`.

The repository's MIT License applies to code. The compact numerical outputs and author-compiled parameter tables are supplied to reproduce the reported figures and should be cited through the associated article. Rights in any underlying third-party sources remain with their respective providers.
