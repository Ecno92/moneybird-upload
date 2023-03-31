# Moneybird upload

Tool to upload individual documents to moneybird by right clicking on them in the nautilus file explorer.

Current state: working prototype

## Screenshots

![select](/images/example-select.png)

![result](/images/example-result.png)

## Dependencies

* Python
  * httpx
* Makefile

## Installation

Just clone this project and install by linking the script to the correct directory.

`$ make link`

## Configuration

Use the command:

`$ make settings`

It will ask you for the API token.
You can create this [here](https://moneybird.com/user/applications/new).
Create a token for personal use.
Give access to incoming documents.

After pressing enter it will ask for the administration id.
You can find the administration ID when looking at the URL of your feed.
For example: `https://moneybird.com/2000000000000000/feed`.
The number in the URL is your administration ID.

## Usage

Right click on a file. The context menu will open.
Click on scripts and press `moneybirdupload`.

The file should be uploaded to the incoming files of your administration.
