# TODO

## MVP 1: Frontend Swiper (local-only)

- [x] Build HTML layout with card + buttons
- [x] Add JavaScript to show next item
- [x] Record decisions in-memory
- [x] Style buttons and layout with CSS
- [ ] Add local image switching (optional)
- [ ] Load shows from shows.json (optional)

---

## MVP 2: Backend (C++ + PostgreSQL)

- [ ] Set up C++ web server (Crow or Pistache)
- [ ] Define API routes: `/next`, `/swipe`
- [ ] Connect to PostgreSQL
- [ ] Create schema for users, shows, swipes
- [ ] Test with dummy data and curl/postman

---

## MVP 3: Connect Frontend to Backend

- [ ] Use `fetch()` to get shows from `/next`
- [ ] Use `fetch()` to POST swipes to backend
- [ ] Disable buttons until response received
- [ ] Show loading/error states

---

## MVP 4: Add User Identity

- [ ] Prompt for username on startup
- [ ] Send `user_id` with all swipe actions
- [ ] Store swipe history per user

---

## MVP 5: Recommender System

- [ ] Use Bernoulli Thompson Sampling
- [ ] Track success/failure counts per show
- [ ] Track aggregate stats per genre
- [ ] Simulate regret and visualize results
- [ ] Integrate recommender into `/next` logic

---

## MVP 6: Polish & Deploy

- [ ] Clean up frontend UI with Tailwind or Bootstrap
- [ ] Add placeholder art, real metadata
- [ ] Host backend + DB (Render/Fly.io)
- [ ] Host frontend (Netlify/Vercel)
- [ ] Add README screenshots + demo video
