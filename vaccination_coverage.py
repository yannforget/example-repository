"""
Vaccination Coverage Analysis Script
Calculates vaccination coverage rates using sample DHIS2 data
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample DHIS2 vaccination data (synthetic)
data = {
    "district": ["District A", "District B", "District C", "District D", "District E"],
    "bcg_coverage": [92.1, 87.6, 94.3, 82.9, 89.7],  # BCG vaccination coverage (%)
    "penta1_coverage": [
        88.4,
        82.3,
        91.5,
        79.8,
        85.2,
    ],  # Pentavalent 1st dose coverage (%)
    "penta3_coverage": [
        76.2,
        68.9,
        82.7,
        64.5,
        72.3,
    ],  # Pentavalent 3rd dose coverage (%)
    "measles_coverage": [
        71.8,
        65.4,
        78.9,
        62.7,
        68.5,
    ],  # Measles vaccination coverage (%)
    "population_under1": [
        4521,
        6823,
        3928,
        5142,
        4789,
    ],  # Population of children under 1 year
    "population_under5": [
        2103,
        4521,
        8431,
        5743
    ], # Population of children under 5 years old (and over 1)
}


def calculate_vaccination_coverage():
    """Calculate vaccination coverage indicators from sample DHIS2 data"""

    # Create DataFrame from sample data
    df = pd.DataFrame(data)

    print("Vaccination Coverage Analysis")
    print("=============================")

    # Calculate national coverage (weighted by population)
    national_coverage1 = {}
    national_coverage5 = {}
    for vaccine in [
        "bcg_coverage",
        "penta1_coverage",
        "penta3_coverage",
        "measles_coverage",
    ]:
        weighted_coverage1 = sum(df[vaccine] * df["population_under1"]) / sum(
            df["population_under1"]
        )
        weighted_coverage5 = sum(df[vaccine] * df["population_under5"]) / sum(
            df["population_under5"]
        )
        national_coverage1[vaccine] = weighted_coverage1
        national_coverage5[vaccine] = weighted_coverage5

    print("\nNational Coverage Estimates:")
    for vaccine, coverage in national_coverage.items():
        print(f"  {vaccine.replace('_coverage', '').upper()}: {coverage:.1f}%")

    # Calculate dropout rates
    print("\nDropout Rates:")
    penta_dropout = (
        (national_coverage["penta1_coverage"] - national_coverage["penta3_coverage"])
        / national_coverage["penta1_coverage"]
        * 100
    )
    print(f"  Penta1 to Penta3 dropout rate: {penta_dropout:.1f}%")

    bcg_measles_dropout = (
        (national_coverage["bcg_coverage"] - national_coverage["measles_coverage"])
        / national_coverage["bcg_coverage"]
        * 100
    )
    print(f"  BCG to Measles dropout rate: {bcg_measles_dropout:.1f}%")

    # Identify districts with low coverage
    low_coverage_threshold = 70
    print("\nDistricts with low Penta3 coverage (<70%):")
    low_coverage_districts = df[df["penta3_coverage"] < low_coverage_threshold]

    if not low_coverage_districts.empty:
        for _, row in low_coverage_districts.iterrows():
            print(f"  {row['district']}: {row['penta3_coverage']:.1f}%")
    else:
        print("  None")

    return df


if __name__ == "__main__":
    # Analyze vaccination coverage
    vaccination_data = calculate_vaccination_coverage()
