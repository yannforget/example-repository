"""
Maternal Health Analysis Script
Analyzes maternal health indicators from sample DHS data
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample DHS maternal health data (synthetic)
data = {
    "region": ["North", "South", "East", "West", "Central"],
    "anc_coverage": [76.2, 64.8, 82.3, 59.7, 71.5],  # % women with 4+ ANC visits
    "skilled_birth_attendance": [
        82.7,
        58.9,
        88.4,
        62.3,
        75.8,
    ],  # % births with skilled attendant
    "maternal_mortality_ratio": [267, 412, 198, 376, 285],  # per 100,000 live births
    "postnatal_care": [
        59.8,
        42.3,
        67.1,
        48.9,
        52.6,
    ],  # % women with postnatal check within 2 days
}


def analyze_maternal_indicators():
    """Analyze key maternal health indicators from sample DHS data"""

    # Create DataFrame from sample data
    df = pd.DataFrame(data)

    print("Maternal Health Indicators Analysis")
    print("===================================")

    # Calculate basic statistics
    print("\nSummary Statistics:")
    for indicator in [
        "anc_coverage",
        "skilled_birth_attendance",
        "maternal_mortality_ratio",
        "postnatal_care",
    ]:
        mean_val = df[indicator].mean()
        median_val = df[indicator].median()
        min_val = df[indicator].min()
        max_val = df[indicator].max()
        print(f"{indicator.replace('_', ' ').title()}:")
        print(f"  Mean: {mean_val:.1f}")
        print(f"  Median: {median_val:.1f}")
        print(
            f"  Min: {min_val:.1f} (Region: {df.loc[df[indicator] == min_val, 'region'].iloc[0]})"
        )
        print(
            f"  Max: {max_val:.1f} (Region: {df.loc[df[indicator] == max_val, 'region'].iloc[0]})"
        )
        print()

    # Calculate correlation between indicators
    print("Correlation between Skilled Birth Attendance and Maternal Mortality:")
    correlation = np.corrcoef(
        df["skilled_birth_attendance"], df["maternal_mortality_ratio"]
    )[0, 1]
    print(f"  Correlation coefficient: {correlation:.2f}")

    return df


if __name__ == "__main__":
    # Analyze the maternal health data
    maternal_data = analyze_maternal_indicators()
