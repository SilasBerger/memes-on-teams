# Memes on Teams
A meme board for Teams using Zagreus and OBS.

## Usage
- Start Zagreus server
- Build and upload template: `cd template && zagreus-generator build -u`
- Add add a browser source in OBS. Set it to 1920x1080px and point it to http://localhost:58179/static/template/memes-on-teams.

## Usage in Teams
- Run OBS and set it up as described above
- In the same scene, add a Display Capture source, capturing whatever display and region you wish to screen-share
- Right-click the OBS preview pane and click "Windowed Projector (Preview)"
- Share only this detached window when screen-sharing. Note that this might not work if the window is minimized or on a non-focused virtual desktop.

## Plans
Add a web application which scans the `assets/memes` directory and displays each meme as a thumbnail. The thumbnails act as buttons to (1) update the image (`POST http://localhost:58179/api/template/memes-on-teams/data/image` with `image-container` as the id and any `memes/<filename>` as the asset) and (2) executes the `ImageIn` animation (`http://localhost:58179/api/template/memes-on-teams/data/animation/ImageIn`).

Likely, users can then either click the meme again or click some "Image Out" button, in order to remove the meme.

