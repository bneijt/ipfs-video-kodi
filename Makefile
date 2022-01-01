
SOURCES=$(shell find . -name '*.py')
OUTPUT_PATH=build/plugin.video.ipfs

clean:
	rm -rf build

build/plugin_video_ipfs.zip: build
	rm -f build/plugin_video_ipfs.zip
	cd build && zip -r plugin_video_ipfs.zip plugin.video.ipfs

build: $(SOURCES) fanart.jpg icon.png addon.xml resources/settings.xml
	poetry build
	mkdir -p $(OUTPUT_PATH)/ipfs
	tar -xzf dist/ipfs-video-kodi-*.tar.gz -C dist --wildcards '*/ipfs_video_kodi'
	cp -r dist/*/ipfs_video_kodi/* $(OUTPUT_PATH)
	cp -r resources $(OUTPUT_PATH)
	cp icon.png $(OUTPUT_PATH)
	cp addon.xml $(OUTPUT_PATH)
	cp fanart.jpg $(OUTPUT_PATH)
	cp LICENSE.txt $(OUTPUT_PATH)
	cp README.md $(OUTPUT_PATH)/README


package: build/plugin_video_ipfs.zip
	unzip -t build/plugin_video_ipfs.zip
