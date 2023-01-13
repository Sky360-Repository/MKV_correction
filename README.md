# MKV Correction

## Introduction
This python script converts .mkv files to .mp4 files using ffmpeg. All the .mkv files from the input_folder are processed and saved in the output_folder. The script uses ffprobe to get the fps of the input file and then uses ffmpeg to convert the file. The script writes the progress of the conversion in a log file.

## Dependencies
In order to run this script, you will need to have the ffmpeg binaries in your path

## Usage

Set input folder path at the input_folder variable.
Set output folder path at the output_folder variable.
Run ConvertToMP4.py

Note: Make sure the folder paths are correct and the folders exist before running the script.