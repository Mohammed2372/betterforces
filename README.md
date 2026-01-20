# BetterForces

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Litestar](https://img.shields.io/badge/Litestar-green?style=for-the-badge&logo=lightning)
![UV](https://img.shields.io/badge/UV-red?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensource)

## Project Idea

API for analyzing Codeforces profiles that provides useful statistics for improving competitive programming skills.

## Goal

Help competitive programmers and their coaches:
- Identify weak spots in training
- Find knowledge gaps and shortcomings
- Determine strengths
- Track progress and development trends

## Core Features

### 1. Difficulty Progression
Shows growth in the level of solved problems:
- Average rating of solved problems by periods (month, quarter)
- Graph of average problem rating changes over time
- Rate of difficulty growth (how much problem rating increases per month)

### 2. Difficulty Distribution
Analyzes the distribution of solved problems by difficulty levels:
- Groups solved problems into rating bins (800, 900, 1000, 1100, etc.)
- Shows the count of solved problems in each bin
- Helps understand problem-solving patterns across different difficulty ranges

### 3. Abandoned Problems Analysis
Identifies problems user attempted but never solved:
- Groups failed attempts by tags to find problematic topics
- Groups failed attempts by rating bins to identify difficulty thresholds
- Provides insights into knowledge gaps and areas needing more practice

### 4. Average Rating by Tag
For each tag (dp, graphs, greedy, math, etc.) calculates:
- Average rating of all solved problems with this tag
- Median rating for more robust analysis
- Number of solved problems by tag
- Percentile relative to the overall average problem rating

### 5. Weak Tags Detection
Automatically identifies problematic topics:
- Finds tags where the average rating of solved problems is significantly lower (e.g., 200+ points) than the overall average
- Ranks weak tags by degree of lag
- Shows how many problems were solved in weak topics (little practice or actually difficult)

## Technical Approach

RESTful API that receives data through the public Codeforces API and provides processed analytics.

## Architecture

- **Backend-only**: No frontend in this repository
- **Redis storage**: Used for rate limiting, no data persistence for MVP
- **On-demand data fetching**: Fetches fresh data from Codeforces API for each request
- **Clean Architecture**: Separated into layers (api/, domain/, infrastructure/, services/)

## Project Structure

```
betterforces/
├── sources/                      # All source code
│   ├── api/                      # API layer
│   │   ├── app.py                # Litestar application
│   │   ├── routes/               # Route handlers
│   │   ├── schemas/              # Pydantic schemas
│   │   └── deps.py               # Dependencies
│   ├── domain/                   # Business logic layer
│   │   ├── models/               # Data models
│   │   └── services/             # Business services
│   ├── infrastructure/           # Infrastructure layer
│   │   ├── codeforces_client.py  # Codeforces API client
│   │   └── redis_client.py       # Redis cache client
│   ├── services/                 # Application services
│   │   └── codeforces_data_service.py  # Data synchronization service
│   ├── config.py                 # Application configuration
│   └── main.py                   # Entry point
├── tests/                        # Unit and integration tests
├── pyproject.toml                # Python dependencies and project configuration
├── uv.lock                       # UV lock file
├── README.md                     # This file
└── LICENSE                       # License
```

## API Endpoints

Base URL: `/`

### Difficulty Progression
- `GET /difficulty-progression/{handle}` - Get difficulty progression metrics over time, including average ratings by period and growth rates

### Rating Distribution
- `GET /rating-distribution/{handle}` - Get paginated list of user's solved problem submissions with rating and submission time, optionally filtered by date range

### Difficulty Distribution
- `GET /difficulty-distribution/{handle}` - Get problem distribution by difficulty levels (800, 900, 1000...), showing count of solved problems in each bin

### Abandoned Problems
- `GET /abandoned-problems/by-tags/{handle}` - Get analysis of problems user attempted but never solved, grouped by tags
- `GET /abandoned-problems/by-ratings/{handle}` - Get analysis of problems user attempted but never solved, grouped by rating bins

### Tags
- `GET /tags/{handle}` - Get average and median rating by tags, number of solved problems per tag
- `GET /tags/{handle}/weak` - Get weak tags analysis with threshold-based filtering

**Response format**: JSON with analytics data and metadata
