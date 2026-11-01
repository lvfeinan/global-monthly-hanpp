# Global Monthly HANPP Reconstruction (2010-2024)

Public code and main-text figure inputs for *Seasonal energy bottlenecks reveal constraints on vertebrate biodiversity*.

The analysis reconstructs monthly human appropriation of net primary production (HANPP), actual net primary production (NPPact), and residual ecological production (NPPeco) on a global 0.1-degree grid.

## What this repository provides

- The core A-C notebooks used for grid alignment, carbon accounting, monthly harvest allocation, NPP reconstruction, and rolling-window metrics.
- The shared grid utilities used by those notebooks.
- Condensed Ultraplot notebooks adapted to the included plot-ready data for reproducing the Python-generated panels in Figures 1-4.
- Compact, plot-ready values for the main-text figures.

The A-C notebooks document the core analysis but require external source data and intermediate raster exports. The D-stage notebooks reproduce the Python-generated main-text panels from the compact files included in `data/main_figures/`.

## External data and Google Earth Engine exports

Google Earth Engine acquisition and export code is not included. Follow the manuscript Methods and source-provider documentation to obtain the required inputs and configure an appropriate export workflow. Earth Engine is not required for the main-text plotting notebooks because their compact inputs are included in `data/main_figures/`.

## Reproduce the main-text figures

Python 3.10 or newer is recommended. A Conda environment is the easiest way to install the geospatial stack.

```bash
pip install -r requirements.txt
cd notebooks
jupyter lab
```

Run the following notebooks:

- `D4_main_figures.ipynb`: Figures 1 and 3.
- `D2_sem_plots.ipynb`: Figure 2 panels A-D.
- `D3_richness_risk.ipynb`: Figure 4 from the final baseline-risk and monthly NPPeco-anomaly arrays.

The notebooks read `../data/main_figures/` and write generated panels to `../outputs/main_figures/`.

Figure 2 panels E-H are the manually checked SEM path diagrams used in the manuscript and were finalized in PowerPoint. They are not redrawn in Python. The table `data/main_figures/figure2/sem_paths.csv` records the path and interaction coefficients, significance values, and R-squared values used to check those panels.

## Analysis record

For the A-C notebooks, copy `config.yaml.template` to `config.yaml` and replace the placeholders with local paths. These stages will run only when the required external inputs and intermediate products are available.

| Stage | File | Role |
|---|---|---|
| External preparation | Not included | Prepare the external inputs described in the manuscript Methods, including any required Earth Engine exports. |
| A | `A3_admin_align.ipynb` | Align administrative boundaries and FAOSTAT country identifiers. |
| B | `B1_grid_alignment.ipynb` | Resample exported MODIS rasters to the common 0.1-degree grid. |
| B | `B2_fao_carbon_accounting.ipynb` | Convert FAOSTAT crop, livestock, and forestry statistics to carbon. |
| B | `B3_crop_harvest.ipynb` | Spatialize monthly crop harvest. |
| B | `B4_grassland_harvest.ipynb` | Spatialize monthly grazing harvest. |
| B | `B5_forest_harvest.ipynb` | Spatialize monthly forest harvest. |
| B | `B6_hanppharv_combine.ipynb` | Combine crop, grazing, and forest HANPPharv. |
| C | `C1_nppact_reconstruct.ipynb` | Reconstruct monthly NPPact. |
| C | `C2_nppeco_npppot.ipynb` | Derive NPPeco, NPPpot, and HANPP. |
| C | `C3_rolling_metrics.ipynb` | Calculate 1-, 3-, 6-, and 12-month rolling metrics. |
| D | `D2_sem_plots.ipynb` | Plot Figure 2 panels A-D. |
| D | `D3_richness_risk.ipynb` | Plot Figure 4. |
| D | `D4_main_figures.ipynb` | Plot Figures 1 and 3. |

## Repository layout

```text
config.yaml.template   Local path template for the A-C analysis record
data/params/           Accounting parameter tables used by the notebooks
data/main_figures/     Compact inputs for the main-text plotting notebooks
notebooks/             Core analysis record and main-text plotting notebooks
src/                   Shared grid utilities
requirements.txt       Python dependencies
LICENSE                MIT license for the code
```

## Data availability and citation

Third-party inputs are not included; see the manuscript Methods, references, and Data Availability statement for their sources and citations.

Code is released under the MIT License.

## AI-assisted repository preparation

ChatGPT (OpenAI) assisted with public-repository organization, English-language documentation, and consistency checks. The authors reviewed and validated all repository content and take full responsibility for it.
