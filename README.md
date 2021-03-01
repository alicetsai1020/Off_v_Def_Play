# NBA Winning Stats

### Background

Introduced to the sport and game of basketball at a young age, my curiosity follows in determining whether offensive or defensive play is equivalently integral to game wins. In the exploration of this question, we look through the prism of some of the NBA's advanced statistics.  

### Question and Hypotheses

Question: Does offensive and defensive game play differ between winning and losing teams?

Null hypothesis: There is no difference between offensive and defensive game play stats for winning and losing teams.

Alternative hypothesis: There is a difference between offensive and defensive game play stats for winning and losing teams.

### Data

Data consisted of NBA 2018-19 regular season game statistics from NBA.com APIs via the client package at [nba-api](https://pypi.org/project/nba-api/). From the season data, I select the following statistics to compare winning and losing teams as proxies to measure offensive and defensive play:

1. Effective field goal percentage
1. Turnover rate
1. Offensive rebounding percentage
1. Free throw attempt rate 

These are commonly known as the four factors, which are box score derived metrics and are presumed by many to correlate most closely with winning basketball games.

### Methods

The statistical test applied is a t-test for the difference of means between the winning and losing team samples because the standard deviations of the winning and losing team populations are unknown. Because the sample sizes are sufficiently large, we can additionally assume that the distribution for the difference of means approximates the normal distribution by the central limit theorem.

### Results

For each of the statistics above, the null hypothesis is rejected - there is statistical evidence to infer that there is a difference between offensive and defensive game play stats for winning and losing teams.

### Acknowledgements

Thanks to Juliana Duncan, Dan Rupp & Kiara Hearn for their help and guidance during this project.

### References
API client package: [nba-api](https://pypi.org/project/nba-api/)
