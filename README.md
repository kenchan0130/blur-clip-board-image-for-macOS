# Blure clip board image for macOS

[![PyPi version][pypi-image]][pypi-url]
[![MIT][mit-image]][mit-url]

[pypi-image]: https://badgen.net/pypi/v/blur-clip-board-image-cli
[pypi-url]: https://pypi.org/project/blur-clip-board-image-cli

[mit-image]: https://badgen.net/pypi/license/blur-clip-board-image-cli
[mit-url]: https://github.com/kenchan0130/blur-clip-board-image-for-macOS/blob/master/LICENSE

Blur clip board image command line tool for macOS.

## Installation

### pip

```sh
pip install blur-clip-board-image-cli
```

### Directly

```sh
curl -sL https://raw.githubusercontent.com/kenchan0130/blur-clip-board-image-for-macOS/master/install.sh | bash
```

It installs on `/usr/local/bin` as default.
If you want to change directory, please set `BLUR_CLIP_BOARD_IMAGE_INSTALL_DIR` like follows.

```sh
export BLUR_CLIP_BOARD_IMAGE_INSTALL_DIR="/path/to/directory"
curl -sL https://raw.githubusercontent.com/kenchan0130/blur-clip-board-image-for-macOS/master/install.sh | bash
```

## Usage

1. Copy image
2. Run this command `blur-clip-board-image`
    - Default blur rate is `8.5`
    - You can also select blur rate with argument like `blur-clip-board-image -r 10`
3. Paste image

## Licence

MIT