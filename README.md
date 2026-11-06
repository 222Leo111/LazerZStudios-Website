# LazerZStudios website: start here

## What is in this folder
- index.html: the website
- admin.html: your phone admin page (post news, add and manage games)
- games.json: the list of games
- announcements.json: the news posts
- assets/: game cover images
- scripts/ and .github/: the free auto-update from itch.io

Keep all of these together, including the folders.

## Part 1: Put the site online (free)
1. Make a free GitHub account and create a new repository. Make it Public (free GitHub Pages needs a public repo).
2. Upload everything in this folder to the repo, keeping the folders. On a computer, drag the files and folders in. On a phone, you can't upload folders, so use Add file > Create new file, type the full path (for example .github/workflows/update-games.yml) and paste the contents.
3. In the repo go to Settings > Pages. Under Build and deployment choose Deploy from a branch, pick main and / (root), and Save.
4. After a minute or two your site is live at https://YOURNAME.github.io/REPO/

## Part 2: Set up the phone admin (one time)
1. On GitHub go to Settings > Developer settings > Personal access tokens > Fine-grained tokens > Generate new token.
2. Repository access: Only select repositories, and pick your site repo.
3. Permissions: set Contents to Read and write. Generate the token and copy it.
4. Open https://YOURNAME.github.io/REPO/admin.html on your phone. In the setup box enter your repo as YOURNAME/REPO, paste the token, and tap Save setup.
5. Tip: add admin.html to your Home Screen from the browser share menu.
The token is stored only on that device. Set an expiry date and make a new one when it runs out.

## Part 3: Automatic games from itch.io (one time)
1. Logged in as your studio account, go to https://itch.io/user/settings/api-keys and make an API key.
2. In your GitHub repo go to Settings > Secrets and variables > Actions > New repository secret. Name it ITCH_API_KEY and paste the key.
3. Open the Actions tab, choose "Update games from itch.io", and tap Run workflow.
From then on it checks itch.io every hour. New published games, titles, release dates and cover images appear on the site by themselves, and a changed cover on itch.io replaces the old one.
If the run fails with a permissions error, go to Settings > Actions > General > Workflow permissions and choose Read and write.

## Part 4: Label your games (important)
New games from itch.io start as Unsorted and show only under All games, with no AI tag. Open admin.html, scroll to Manage games, and set each one to AI or Non-AI. Any game set to AI shows an AI tag on its card, as your AI Policy promises. The Home box puts a game on the front page and Hide takes it off the site.

## Everyday jobs (all in admin.html)
- Post news: fill in the form and tap Post announcement. You can edit, pin to the banner, or remove posts. The two newest also show on the home page.
- Add a game by hand: title, itch.io link, release date, AI or Non-AI, and an optional cover picked from your phone. Without a cover the site shows "Cover art coming soon". Games added by hand are never removed by the auto-update.
- Changes go live in a minute or two.

## Optional extras
- Contact email: open index.html, find CONTACT_EMAIL and set it, for example to support@yourdomain.com.
- Your own web address: buy a domain, then add it under Settings > Pages > Custom domain.
- Keep the code private: use a private repo and host the site on Cloudflare Pages instead of GitHub Pages (check Cloudflare's current free limits). The admin page and auto-update still work with a private repo.
- Host on itch.io instead: zip the folder and upload it as an HTML game. In index.html set ANN_URL and GAMES_URL to your raw GitHub links, like https://raw.githubusercontent.com/YOURNAME/REPO/main/games.json, so news and games update without re-uploading. Changes can take about 5 minutes to appear.

## If something goes wrong
- A change isn't showing: wait a few minutes and refresh. If games still don't update, set GAMES_URL to the raw GitHub link as above.
- Admin says GitHub refused the token: check the token has Contents Read and write for this repo, and hasn't expired.
- Auto-update stopped: GitHub pauses scheduled runs after 60 days with no repo activity. Tap Run workflow to restart it.
- Make sure your Discord invite is set to never expire.

## Pages and policies
The site has AI Policy, Privacy Policy, Terms of Use and Contact pages, linked in the footer. They are plain-language drafts written for what the site does today. If you add analytics, accounts or ads, update the Privacy Policy first.

## Layouts
The site picks its layout automatically: phone, phone on its side, tablet, desktop, and TV or VR. Nothing to set up.
