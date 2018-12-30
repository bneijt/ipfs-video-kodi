# IPFS video plugin for Kodi

Plugin to browse and play video media from IPFS.

It has a configurable gateway and a configurable root CID that you can browse.

# Build from source

- `make package`
- Copy the `build/plugin_video_ipfs.zip`

# Viewing your own content

- Install IPFS on your media player
- Use `ipfs add -r -w yourdirectory` to insert your directory
- Configure plugin to have gateway point to `http://localhost:8080`
- Use the hash of the directory as the root CID in the plugin configuration

# Develop

- `make venv`
- `make test`
- `make build`

# License information

Source code license: [GPL v.3](http://www.gnu.org/copyleft/gpl.html)

Fanart is from https://pixabay.com/nl/beaded-spinneweb-raagbol-web-dauw-1630493/

Icon is from https://pixabay.com/nl/puzzel-spel-kubus-rubiks-kubus-1243091/
