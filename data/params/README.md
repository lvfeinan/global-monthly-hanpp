# Accounting parameter tables

These files contain compact accounting parameters used by the monthly HANPP reconstruction. Parameters are assigned by the ten PNAS regions of Haberl et al. (2007), crop class, or livestock class, as applicable.

## Files read by the notebooks

| File | Contents | Consumer |
|---|---|---|
| `crop_coefficients.xlsx` | Above-ground crop-residue harvest factors by class and region. | B2, B3 |
| `grazing_coefficients.xlsx` | Daily dry-matter intake for 11 functional livestock groups by region. | B2, B4 |
| `FBS_feed_items.xlsx` | Mapping from Food Balance Sheet commodity items to feed categories. | B2 |
| `crop_moisture.csv` | Moisture fractions used to convert crop fresh mass to dry mass. | B2, B3 |
| `forest_factors.csv` | Forest recovery fractions and wood-volume-to-dry-matter factors. | B2 |
| `crop_classification.csv` | Mapping from crop items to harvest-factor and recovery classes. | B2, B3 |
| `crop_uesd_in_FAO.csv` | FAO crop-code list included in the accounting. | B2, B3 |
| `FAO-CROPGRIDS-GGCMI.csv` | Crop-name mapping and temporal-allocation method across FAO, CROPGRIDS, and GGCMI. | B3 |

## Reference exports

`country_region_mapping.csv` and `region_definition.csv` document the country and region mappings used in the analysis. The notebooks derive the operational mapping from the aligned administrative-boundary table produced by A3.

The manuscript and Supplementary Information are the authoritative sources for parameter definitions and literature citations.

These author-compiled tables are supplied to document and reproduce the accounting workflow. Cite the associated article when reusing them; rights in underlying third-party source information remain with the original providers. The repository's MIT License applies to code, not to third-party data.
