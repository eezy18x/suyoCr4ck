#!/bin/bash

# Define the location where the wordlists should be
WORDLIST_DIR="/usr/share/wordlists"
MEGA_URL="https://mega.nz/folder/TxhVDKTD#6bMU0behXeGbMTO_-iZxiA"  

# Check if wordlists exist
if [ -d "$WORDLIST_DIR" ]; then
    echo "Wordlists directory already exists at $WORDLIST_DIR."
else
    echo "Wordlists directory not found. Creating and downloading wordlists..."

    # Create wordlists directory if not exists
    sudo mkdir -p $WORDLIST_DIR

    # Download the wordlists from Mega.nz
    echo "Downloading wordlists from Mega.nz..."
    megadl $MEGA_URL  

    # Unzip wordlists into /usr/share/wordlists (if it's a ZIP)
    if [ -f "wordlists.zip" ]; then
        echo "Unzipping wordlists..."
        sudo unzip -q wordlists.zip -d $WORDLIST_DIR
        rm wordlists.zip
    fi

    # If it's a folder, you don't need to unzip, just move it
    if [ -d "wordlists" ]; then
        sudo mv wordlists/* $WORDLIST_DIR/
        rm -rf wordlists  # Clean up the downloaded folder
    fi

    echo "Wordlists installed successfully!"
fi
