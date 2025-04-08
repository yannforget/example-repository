"""
Nutrition Analysis Script
Processes child nutrition statistics across regions
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample nutrition data from DHS (synthetic)
data = {
    "province": ["Province 1", "Province 2", "Province 3", "Province 4", "Province 5"],
    "stunting": [
        32.4,
        41.7,
        28.9,
        36.2,
        30.5,
    ],  # % children under 5 with height-for-age < -2 SD
    "wasting": [
        8.7,
        12.3,
        6.9,
        10.8,
        7.6,
    ],  # % children under 5 with weight-for-height < -2 SD
    "underweight": [
        19.8,
        27.5,
        15.3,
        22.9,
        18.4,
    ],  # % children under 5 with weight-for-age < -2 SD
    "exclusive_bf": [
        52.4,
        38.9,
        61.7,
        43.5,
        56.2,
    ],  # % infants exclusively breastfed for first 6 months
    "sample_size": [876, 945, 782, 814, 903],  # Number of children measured
}


def analyze_nutrition_data():
    """Analyze child nutrition indicators from sample DHS data"""

    # Create DataFrame from sample data
    df = pd.DataFrame(data)

    print("Child Nutrition Status Analysis")
    print("===============================")

    # Calculate weighted national averages
    national_indicators = {}
    for indicator in ["stunting", "wasting", "underweight", "exclusive_bf"]:
        weighted_avg = sum(df[indicator] * df["sample_size"]) / sum(df["sample_size"])
        national_indicators[indicator] = weighted_avg

    print("\nNational Prevalence Estimates:")
    print(f"  Stunting: {national_indicators['stunting']:.1f}%")
    print(f"  Wasting: {national_indicators['wasting']:.1f}%")
    print(f"  Underweight: {national_indicators['underweight']:.1f}%")
    print(f"  Exclusive breastfeeding: {national_indicators['exclusive_bf']:.1f}%")

    # Classify provinces by stunting severity (WHO classification)
    print("\nStunting Severity Classification by Province:")
    for _, row in df.iterrows():
        if row["stunting"] < 20:
            severity = "Low severity"
        elif 20 <= row["stunting"] < 30:
            severity = "Medium severity"
        elif 30 <= row["stunting"] < 40:
            severity = "High severity"
        else:
            severity = "Very high severity"

        print(f"  {row['province']}: {row['stunting']:.1f}% ({severity})")

    # Calculate correlation between breastfeeding and malnutrition
    print("\nCorrelation between exclusive breastfeeding and malnutrition indicators:")
    for indicator in ["stunting", "wasting", "underweight"]:
        corr = np.corrcoef(df["exclusive_bf"], df[indicator])[0, 1]
        print(f"  {indicator.title()}: {corr:.2f}")

    return df


if __name__ == "__main__":
    # Analyze nutrition data
    nutrition_data = analyze_nutrition_data()

    # TODO: Change thresholds for stunting severity:
    # Low severity: < 10%
    # Medium severity: 10% - 20%
    # High severity: 20% - 30%
    # Very high severity: > 30%
