# Dota 2 Team Performance Analysis

This project analyzes professional Dota 2 matches to understand what actually drives winning — from team performance and hero meta to comeback dynamics.

The focus is not just on statistics, but on extracting meaningful insights from real match data.

---

## Why This Project

Dota 2 is a complex game where outcomes are influenced by many factors — strategy, hero selection, and team decision-making.

This project was built to explore whether common assumptions (like popular heroes = strong heroes) actually hold true in real data.

---

## Project Highlights

* Built a custom "mental score" to measure team resilience (comeback vs throw)
* Identified gaps between hero popularity and actual win performance
* Analyzed team consistency across multiple tournaments
* Explored how gameplay pace changes over time and across events

---

## Key Questions Answered

* Do popular heroes actually have higher win rates?
* Which teams are the most consistent across tournaments?
* Are longer games more aggressive or just more controlled?
* Which teams perform well under pressure situations?

---

## Project Overview

Instead of just looking at win rates, the analysis goes deeper into:

* how teams perform under different conditions
* whether popular heroes are actually effective
* how often teams throw or make comebacks
* how gameplay changes across tournaments

---

## Dataset

The data used in this project includes:

* Match results (duration, kills, win/lose)
* Team information
* Hero picks
* Throw & comeback metrics

---

## Tools Used

* Python (Pandas)
* Matplotlib & Seaborn (for static visualizations)
* Plotly (for interactive charts)

---

## What I Did

### Team Performance

* Calculated win rate, average duration, and kills per team
* Compared performance when winning vs losing
* Identified the most consistent teams

### Hero Analysis

* Found the most picked heroes
* Compared pick rate vs win rate
* Identified underrated heroes with high win rates

### Throw & Comeback

* Measured how often teams throw games or make comebacks
* Created a simple metric:

  * mental_score = comeback_rate - throw_rate

### Tournament Analysis

* Compared match duration and kills across tournaments
* Looked at how gameplay style changes between events

### Trend Analysis

* Analyzed how performance changes over time
* Compared top teams across multiple tournaments

---

## Sample Visualization

![Hero Meta](images/hero_scatter.png)

---

## Key Takeaways

* Popular heroes are not always the most effective
* Some rarely picked heroes actually perform very well
* Teams with high comeback rates tend to be more consistent
* Longer games usually have more kills
* Gameplay style changes across tournaments (some are slower, some more aggressive)
* Not all teams perform consistently — some depend heavily on the tournament

---

## Why This Matters

Understanding team performance and hero effectiveness can help:

* Teams improve drafting strategy
* Analysts identify meta trends
* Fans better understand competitive gameplay dynamics

---

## Limitations

* Data is limited to selected tournaments
* No player-level or draft order data included
* Hero synergy and in-game coordination are not fully captured

---

## Insight I Found Most Interesting

Some heroes are consistently picked despite having average win rates, suggesting that popularity is influenced more by perception than actual performance.

---

## How to Run

```bash
git clone https://github.com/yourusername/dota2-analysis.git
cd dota2-analysis
pip install -r requirements.txt
jupyter notebook
```

---

## Final Notes

This project demonstrates how data can be used to move beyond assumptions and uncover real patterns in competitive gameplay.

---

## Author

Choki Armando
