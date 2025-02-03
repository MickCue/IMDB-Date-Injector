# IMDB Date Injector

A Python script that converts IMDB rating data from CSV format to a JavaScript file, making it easy to inject rating dates into the IMDB website.

## Description

This script takes your IMDB ratings export (CSV file) and converts it into a JavaScript file that can be used to display the dates when you rated movies on IMDB. It processes the CSV file, extracts the movie titles and rating dates, and generates a timestamped JavaScript file based on a template.

## Prerequisites

- Python 3.x
- Your IMDB ratings export file (CSV format)
- The `imdbtemplate.js` template file in the same directory
- [Violentmonkey](https://violentmonkey.github.io/) browser extension
  - Compatible with Chrome, Firefox, and other modern browsers
  - Required to inject the generated JavaScript into IMDB pages
  - Install from your browser's extension store:
    - [Chrome Web Store](https://chrome.google.com/webstore/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag)
    - [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/violentmonkey/)

## How to Use

1. Export your IMDB ratings:
   - Go to your IMDB ratings page
   - Click on the "Export" button
   - Save the CSV file

2. Run the script: python createScript.py <ratings.csv>
