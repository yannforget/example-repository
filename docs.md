# Documentation for Global Health Data Analysis

This document provides guidance on using the Python scripts in this repository for analyzing global health data.

## Data Sources

### DHS Data
The Demographic and Health Surveys (DHS) Program collects nationally representative data on population, health, and nutrition in over 90 countries. Our sample data mimics the structure of standard DHS datasets.

TODO: Add links to DHS website.

### DHIS2 Data
The District Health Information System 2 (DHIS2) is an open-source health management information system used by multiple organizations and governments. Our sample DHIS2 data follows standard indicator formats.

TODO: Add links to DHIS2 website.

## Using the Scripts

### Prerequisites
- Python 3.7+
- pandas
- matplotlib
- numpy

### maternal_health.py
This script analyzes maternal health indicators from sample DHS data.

```python
python maternal_health.py
```

The script generates basic statistics on:
- Antenatal care coverage
- Skilled birth attendance
- Maternal mortality ratios

### vaccination_coverage.py
This script calculates vaccination coverage rates using sample DHIS2 data.

```python
python vaccination_coverage.py
```

The script analyzes:
- Immunization coverage by antigen
- Dropout rates between vaccine doses
- Geographic variations in coverage

### nutrition_analysis.py
This script processes child nutrition statistics across regions.

```python
python nutrition_analysis.py
```

The script calculates:
- Stunting and wasting prevalence
- Underweight rates
- Nutrition intervention coverage

## Data Dictionary

The sample data files reference these common indicators:

| Indicator | Description | Source |
|-----------|-------------|--------|
| ANC4+ | % of women with 4+ antenatal care visits | DHS |
| SBA | % of births attended by skilled health personnel | DHS |
| Penta3 | % of children who received 3 doses of pentavalent vaccine | DHIS2 |
| Stunting | % of children under 5 with height-for-age < -2 SD | DHS |
| Wasting | % of children under 5 with weight-for-height < -2 SD | DHS |

## Potential Improvements

These scripts are simplified examples. Possible enhancements include:
- Adding statistical significance testing
- Creating more advanced visualizations
- Adding time trend analysis
- Implementing demographic disaggregation