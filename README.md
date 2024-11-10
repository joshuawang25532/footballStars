# footballStars

### Statistics and Probability Final Project: Identify Football Stars

## Project Overview

This project is part of my Statistics and Probability Final Report, and its goal is to identify top-performing football players based on lifetime statistical data. By analyzing historical football data, we can evaluate and determine which players truly qualify as "football stars."

## Data Conversion

This repository contains the code used to convert publicly available football data from its original format into a format better suited to player analysis.

The original data format recorded statistics on a "per goal" basis, where each entry provided details about a specific goal scored by a player. 

This format is inconvenient because all data is indexed on a "per goal" basis, making it hard to draw conclusions about any given player because information is spread out through multiple data entries.

To gain a clearer view of each player's performance and career impact, the data was restructured to provide cumulative, **lifetime statistics** for each player across their entire career.

This new format is better for data analysis, as it makes it easier to:
- Track lifetime goals, matches played, and other relevant statistics for each player.
- Identify consistent, high-performing players based on their career data.
- Apply statistical analysis to draw comparisons and insights on player performance.

## Project Goals

1. **Data Aggregation**: Convert "per goal" data into lifetime summaries for each player.
2. **Statistical Analysis**: Use statistical methods to identify key performance indicators that make certain players stand out.
3. **Insights on Football Stars**: Determine which players can be identified as stars based on their lifetime performance metrics.

## Data Source

The football data used in this project is publicly available and contains information on goals, matches, teams, and other match-specific details. This data has been restructured and analyzed to provide a lifetime summary for each player.

## Technologies Used

- **Python**: Data processing and analysis
- **Pandas**: Data manipulation and conversion
- **Git**: Version control for project management

## Future Work / TODO

- Add goals/match, first_goals to the converted data
- Define evaluation metrics
- Assign ratings to each player via a weighted sum of the evaluation metrics
