# Global Health Data Analysis

This repository contains simple Python scripts for analyzing global health data from sources like DHIS2 and DHS. It serves as a learning environment for Git collaboration.

## Repository Structure

- `maternal_health.py`: Analyzes maternal health indicators from sample DHS data
- `vaccination_coverage.py`: Calculates vaccination coverage rates using DHIS2 data
- `nutrition_analysis.py`: Processes child nutrition statistics across regions
- `docs.md`: Documentation on how to use these scripts and data sources

## Git Collaboration Exercise

This repository is designed for 5 people to practice Git collaboration:

1. **Person 1**: `maternal_health.py` Include median in printed statistics (see end of file for instructions)
2. **Person 2**: `vaccination_coverage.py` Enhance vaccination coverage calculations with age group stratification (see end of file for instructions)
3. **Person 3**: `nutrition_analysis.py` Add a new nutrition indicator to the nutrition analysis (see end of file for instructions)
5. **Person 4**: `docs.md` Add links to DHS and DHIS2 websites (see file content for instructions)

## Collaboration Workflow

For each person:

1. Create a new branch from main
   ```
   git checkout -b <your-feature-branch>
   ```

2. Make your assigned changes to one file only

3. Commit your changes
   ```
   git add [filename]
   git commit -m "Description of your changes"
   ```

4. Push your branch to GitHub
   ```
   git push origin <your-feature-branch>
   ```

5. Create a Pull Request on GitHub

6. Request a review from another team member

7. After approval, merge the PR

## Data Sources

The sample data used in these scripts is based on:
- Demographic and Health Surveys (DHS)
- District Health Information System 2 (DHIS2)

Note: The data in this repository is synthetic and for educational purposes only.
