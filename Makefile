
SOURCES=$(shell find . -name *.py)
OUTPUT_PATH=build/plugin.video.ipfs

venv:
	( \
		virtualenv --python=python3.7 venv
		source venv/bin/activate; \
		pip install -r requirements.txt; \
	)

test: install venv $(SOURCES)
	venv/bin/py.test

install:
	venv/bin/python setup.py develop

clean:
	rm -rf build

build/plugin_video_ipfs.zip: build
	cd build && zip -r plugin_video_ipfs.zip plugin.video.ipfs

build: $(SOURCES) fanart.jpg icon.png addon.xml
	mkdir -p $(OUTPUT_PATH)/ipfs
	cp -r src/*.py $(OUTPUT_PATH)
	cp -r src/ipfs/*.py $(OUTPUT_PATH)/ipfs
	cp -r resources $(OUTPUT_PATH)
	cp icon.png $(OUTPUT_PATH)
	cp addon.xml $(OUTPUT_PATH)
	cp fanart.jpg $(OUTPUT_PATH)

package: build/plugin_video_ipfs.zip
	unzip -t build/plugin_video_ipfs.zip
