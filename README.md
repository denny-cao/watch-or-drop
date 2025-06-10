# Watch or Drop

A "Tinder for shows" web app that lets users swipe right to **Watch** or left to **Drop** TV shows or movies.

Goal is to explore user interaction, database design, recommender systems, and multi-armed bandit (MAB) algorithms.

---

## Project Goals

- Learn C++ and PostgreSQL through backend development
- Build a clean, interactive frontend
- Implement a simple recommender system using Bernoulli bandits (e.g. Thompson Sampling)

---

## Tech Stack

| Layer        | Tool / Language         |
|--------------|--------------------------|
| Frontend     | HTML, CSS, JavaScript    |
| Backend      | C++ (Crow/Pistache)      |
| Database     | PostgreSQL               |
| Recommender  | Thompson Sampling (MAB)  |
| Hosting      | TBD (Render/Fly.io/etc.) |

---

## Project Structure
<pre><code>```bash watch-or-drop/ ├── backend/ # C++ server and API routes ├── db/ # SQL schemas and seed data ├── frontend/ # UI (HTML, CSS, JavaScript) ├── scripts/ # Analytics and recommender algorithms ├── shared/ # Shared constants or mock show data ``` </code></pre>
---

## MVP Roadmap

1. ✅ **MVP 1**: Frontend-only swiper (local array, buttons)
2. ⏳ **MVP 2**: C++ + PostgreSQL backend to store swipes
3. ⏳ **MVP 3**: Connect frontend to backend
4. ⏳ **MVP 4**: Add user identity + swipe tracking
5. ⏳ **MVP 5**: Recommender system (Thompson Sampling)
6. ⏳ **MVP 6**: Polish, deploy, and publish

