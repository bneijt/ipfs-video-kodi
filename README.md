# IPFS video plugin for Kodi

Plugin to browse and play video media from IPFS.

It has a configurable gateway and a configurable root CID that you can browse.

# Build from source

- `make package`
- Copy the `build/plugin_video_ipfs.zip`

The main branch in github is _not_ installable as a kodi package, please use the [zip from the releases](https://github.com/bneijt/ipfs-video-kodi/releases) if you want to install a zip directly from github.

# Viewing your own content

- Install IPFS on your media player
- Use `ipfs add -r -w yourdirectory` to insert your directory, remember the resulting CID
- Configure plugin to have gateway point to `http://localhost:8080`
- Enter the CID of the directory as the root CID in the plugin configuration
- Optionally:
    - Use `ipfs name publish <cid>` to create an [IPNS](https://docs.ipfs.io/concepts/ipns/#example-ipns-setup-with-cli) record
    - Enter `ipfs/<resulting ipns url>` as the root CID in the plugin configuration

# Develop

- Create venv for development: `poetry install`
- Run the tests: `poetry run pytest`
- Build a release package: `make build`

# License information

Source code license: [GPL v.3](http://www.gnu.org/copyleft/gpl.html)

Fanart is based upon https://pixabay.com/nl/beaded-spinneweb-raagbol-web-dauw-1630493/
