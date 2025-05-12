# The Land Carbon Sink

This repository contains the data and code for the paper:  
**_“Contributions of country-level net land carbon sinks to inclusive wealth”_** 
<!-- The paper is published in [journal] and is available [here](link). -->

## Authors

- Lotta Siebert¹\*  
- Ignacio Saldivia Gonzatti²  
- Anthony Harding³  
- Clemens Schwingshackl⁴  
- Michael O'Sullivan⁵  
- Julia Pongratz⁴ ⁶  
- Wilfried Rickels¹ ⁷

<details>
<summary>Affiliations (click to expand)</summary>

- **\*** Corresponding author: [lotta.siebert@ifw-kiel.de](mailto:lotta.siebert@ifw-kiel.de)  
- ¹ Global Commons and Climate Policy, Kiel Institute for the World Economy, Germany  
- ² Earth Systems and Global Change Group, Wageningen University & Research, Netherlands  
- ³ School of Public Policy, Georgia Institute of Technology, USA  
- ⁴ Department of Geography, Ludwig Maximilian University Munich, Germany  
- ⁵ Faculty of Environment, Science and Economy, University of Exeter, UK  
- ⁶ Max Planck Institute for Meteorology, Hamburg, Germany  
- ⁷ Department of Economics, Kiel University, Germany  
</details>


## Abstract


## Requirements

This project uses **Python 3.12.7** and requires the following Python packages:


```
numpy
pandas
xarray
matplotlib
geopandas
scipy
pysankey

```


## Data

All data used in this analysis are stored in the `data/raw/` directory.

| Dataset | File Name | Source |
|---------|-----------|--------|
| Country Social Cost of Carbon (CSCC) | `raw_scc_SSP2_rcp60_constant_bootstrap_climensemble_hmqrs.csv` | Provided by Anthony Harding |
| Net Land-use Change Flux | `National_LandUseChange_Carbon_Emissions_2024v1.0.xlsx` | [Global Carbon Project](https://globalcarbonbudgetdata.org/latest-data.html) |
| Natural Land Sink | `GCB2023_SLAND_country_mask.nc` | Provided by Michael O'Sullivan |
| Fossil and Industry CO₂ Emissions | `National_Fossil_Carbon_Emissions_2024v1.0.xlsx` | [Global Carbon Project](https://globalcarbonbudgetdata.org/latest-data.html) |
| GDP Deflator Values | `Worldbank_Deflator.csv` | [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators/Series/NY.GDP.DEFL.ZS) |


The dataset `raw_scc_SSP2_rcp60_constant_bootstrap_climensemble_hmqrs.csv` (~2.6 GB) is required but excluded from version control due to its size.

You can either:
- Run the script below to automatically download the file:

```bash
python code/download_data.py
```

- Or manually download it via [this Dropbox link](https://www.dropbox.com/scl/fi/qlxnntf3kelfeocmt0te2/raw_scc_SSP2_rcp60_constant_bootstrap_climensemble_hmqrs.csv?rlkey=53y8xoysiksq35xlzocrlepvr&st=h4ss2dd7&dl=1) and place it in `data/raw/`


## Repository Structure

```
├── code/             
│   └── download_data.py             
│   └── main.ipynb         
├── data/                 
│   ├── raw/
│   ├── interim/
│   └── processed/
├── img/    
└── README.md
```
## Processed Data Naming Convention

Files in the `data/processed/` directory follow a consistent naming convention to reflect the **type of variable**, **geographic aggregation**, and **calculation method**. Below is a breakdown of how to interpret the filenames:

### Format:  
`[Variable]_[Region/Scope]_[Method].csv`

### Components:

- **Variable**  
  - `CSCC`: Country Social Cost of Carbon  
  - `EFOS`: Fossil and industrial CO₂ emissions  
  - `ELUC`: CO₂ emissions from land-use change  
  - `SLAND`: Natural land carbon sink
    - `tf`: Total forest — calculated using all forested land area based on forest cover mask
    - `mf`: Managed forest — calculated using only forest areas classified as "managed"
  - `Fab`, `Fabc`, `Fbc`: Aggregate carbon fluxes  
  - `Wdom`, `Wglob`, `Win`, `Wout`, `Wnet`: Wealth flows (domestic, global, inbound, outbound, net)

- **Region/Scope**  
  - `sovereign`: Aggregated to sovereign country level (e.g., merging overseas territories) 
  

- **Method**  
  - `stats`: Summary statistics (mean, median, percentiles, etc.)
  - `boot_stats`: Bootstrapped statistics used for uncertainty analysis
  - `final`: Final merged outputs for replication or figure generation


## License

<!-- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. -->

