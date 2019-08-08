#!/bin/bash

set -e
if [[ -z "$BLUR_CLIP_BOARD_IMAGE_INSTALL_DIR" ]]; then
  BLUR_CLIP_BOARD_IMAGE_INSTALL_DIR="/usr/local/bin"
fi

if [[ ! -d "$BLUR_CLIP_BOARD_IMAGE_INSTALL_DIR" ]]; then
  /bin/echo "Not found $BLUR_CLIP_BOARD_IMAGE_INSTALL_DIR directory. Please specify an existing directory for \\$BLUR_CLIP_BOARD_IMAGE_INSTALL_DIR."
  return 1
fi

binary_name="blur-clip-board-image"
source_url="https://raw.githubusercontent.com/kenchan0130/blur-clip-board-image-for-macOS/master/blur_clip_board_image/app.py"
install_path="${BLUR_CLIP_BOARD_IMAGE_INSTALL_DIR%%/}/$binary_name"
/usr/bin/curl -sL "$source_url" -o "$install_path"
/bin/chmod +x "$install_path"

/bin/echo "Installed $binary_name to ${BLUR_CLIP_BOARD_IMAGE_INSTALL_DIR%%/} directory."
