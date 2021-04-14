![](images/NBA-Goat.jpg)

# Basketball on Paper

### Background

Introduced to the sport and game of basketball at a young age, my curiosity follows in determining whether offensive or defensive play is equivalently integral to game wins. In the exploration of this question, we look through the prism of some of the NBA's advanced statistics.  

### Question and Hypotheses

Question: Does offensive and defensive game play differ between winning and losing teams?

Null hypothesis: There is no difference between offensive and defensive game play stats for winning and losing teams.

Alternative hypothesis: There is a difference between offensive and defensive game play stats for winning and losing teams.

### Data

Data consisted of NBA 2018-19 regular season game statistics from NBA.com APIs via the client package at [nba-api](https://pypi.org/project/nba-api/). Data drawn is comprised of a game log, league stats, and play stats by team. From the season data, I select the following statistics to compare winning and losing teams as proxies to measure offensive and defensive play:

1. Effective field goal percentage (EFG%) - shooting the ball
1. Turnover rate (TO rate) - taking care of the ball
1. Offensive rebounding percentage (OREB%) - ball recovery by the offensive team
1. Free throw attempt rate (FTA rate) - getting to the foul line

These are commonly known as the four factors, which are box score derived metrics and are presumed by many to correlate most closely with winning basketball games.

### Methods

The statistical test applied is a Welch’s t-test on the difference of means between the winning and losing team samples (without knowing the standard deviations of the winning and losing team populations, the student’s t-test is not well suited here). Because the sample sizes are sufficiently large, we can additionally consider that the central limit theorem applies and therefore we can reasonably assert that the distribution for the difference of means approximates the normal distribution.

### Results

For each of the play statistics by NBA team below, the null hypothesis is rejected - there is statistical evidence to infer that there is a difference between offensive and defensive game play stats for winning and losing teams.

With a significance level selected at 5% and a conservative Bonferroni correction application which further sets the significance level at 1.25% for each t-test, the Welch’s t-tests results of infinitesimally small p-values provide suitable statistical evidence. 

![](images/EFG.png)

p-value: 3.029870529831025e-129

![](images/TO.png)

p-value: 7.22946836638982e-07

![](images/OREB.png)

p-value: 3.04422770092005e-12

![](images/FTAR.png)

p-value: 1.4689448438961602e-07


### Acknowledgements

Thanks to Juliana Duncan, Dan Rupp & Kiara Hearn for their help and guidance during this project.

### References
API client package: [nba-api](https://pypi.org/project/nba-api/)
