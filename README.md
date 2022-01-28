# Memes on Teams
Overlay memes while screen-sharing. Built with [Zagreus](https://github.com/mariokaufmann/zagreus). Use at your own discretion.

## Usage
### Preparation: Adding Memes
In `template/assets`, create a directory `memes` and place all memes to be displayed into that directory. Preferably, give each meme a meaningful filename, as this name will be used to reference the meme when using the shell.

### Shell & Zagreus Server
- From the root of this repository, run `docker build -t memes-on-teams-shell -f docker/shell/Dockerfile .` to build the image
  - Note: If new memes are added, the image needs to be rebuilt
- Run `docker container run -it --rm -p 58179:58179 memes-on-teams-shell` to start the server and enter the interactive shell

### Optional: Shell & Zagreus Server without Docker (for development)
- Make sure to have Python 3 with `requests=2.26.0` available
- Download the [Zagreus v0.0.4 release bundle from GitHub](https://github.com/mariokaufmann/zagreus/releases/tag/v0.0.4) and unzip it
  - Optional: Add the resulting `zagreus` directory to your PATH, to make `zagreus-server` and `zagreus-generator` available without specifying a path in all further steps
- In the `zagreus` directory, run `./zagreus-server` to start the server
- In `memes-on-teams/template`, run `/path/to/zagreus-generator build -u` to build and upload the template
  - Repeat this step to update the template upon changes, e.g. when adding new memes
  - Run `/path/to/zagreus-generator build --help` for additional information
- From the root of this repository, run `python3 shell.py` to enter the interactive shell

### Using the Shell
- Run `list` to list all available memes
- Run `show <meme_name>` to display the given meme
- Run `hide` to hide the last shown meme
- Note: `show` and `hide` are stateless and should always be used in alternating order
- Press `Ctrl+C` to quit

### Integration Into OBS
- Add add a browser source in OBS, set it to `1920x1080px` and point it to [http://localhost:58179/static/template/memes-on-teams](http://localhost:58179/static/template/memes-on-teams)
- Make sure that it is the top layer in the given OBS scene, since it may otherwise be obscured by some opaque layer (e.g. screen capture)
- In case no memes are displayed, e.g. after running `show <meme_name>` in the interactive shell, highlight the browser source in OBS and click "Refresh"

### Usage in Teams
- Run OBS and set it up as described above
- In the same scene, add a Display Capture source (below the browser source), capturing whatever display and region you wish to screen-share
- Right-click the OBS preview pane and click "Windowed Projector (Preview)"
- Share only this detached window when screen-sharing. Note that this may not work if the projector window is minimized or on a non-focused virtual desktop.
