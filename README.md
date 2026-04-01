# Judah Katrina Rivera — Portfolio Website

Professional one-page portfolio for an Executive Assistant.

## Setup

1. **Add your images** to `assets/images/`:
   - `profile.png` — your profile/headshot photo
   - `portfolio_missive_inbox.png`
   - `portfolio_missive_draft.png`
   - `portfolio_calendar_monthly.png`
   - `portfolio_calendar_schedule.png`
   - `portfolio_slack.png`
   - `portfolio_clickup.png`
   - `portfolio_kommodo.png`
   - `portfolio_sop.png`
   - `portfolio_eod_report.png`

2. **Open `index.html`** in a browser to preview.

## Deploy to GitHub Pages

1. Create a new GitHub repository (e.g., `judahrivera.com` or `portfolio`).
2. Push this folder to the repository:
   ```bash
   cd judah-portfolio
   git init
   git add .
   git commit -m "Initial portfolio site"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```
3. Go to **Settings → Pages** in your GitHub repo.
4. Under **Source**, select `main` branch and `/ (root)` folder, then click **Save**.
5. Your site will be live at `https://YOUR_USERNAME.github.io/YOUR_REPO/`.

## How to Update Content

Everything is in `index.html`. Here's where to find each section:

| Section       | What to search for in the file         |
|---------------|----------------------------------------|
| Hero text     | `class="hero"`                         |
| About bio     | `class="about-text"`                   |
| Services      | `class="service-card"`                 |
| Experience    | `class="timeline-item"`                |
| Tools         | `class="tool-badge"`                   |
| Portfolio     | `class="portfolio-item"`               |
| Testimonials  | `class="video-card"` (YouTube URLs)    |
| Contact       | `class="contact-form"`                 |

### Contact Form

The form uses [FormSubmit.co](https://formsubmit.co/) — a free service that forwards submissions to your email. On the first submission, you'll receive a confirmation email to activate it.

### Adding/Removing Portfolio Images

1. Add the image file to `assets/images/`.
2. Copy an existing `<div class="portfolio-item">` block and update the `data-index`, `src`, and `alt` attributes.
3. Make sure `data-index` values are sequential (0, 1, 2, ...).

### Adding/Removing Testimonial Videos

1. Get the YouTube video ID from the URL (the part after `/shorts/` or `?v=`).
2. Copy an existing `<div class="video-card">` block and replace the video ID in the `src` URL.
