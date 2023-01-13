import os
import subprocess
import time

input_folder = "mkv_files"
output_folder = "mp4_files/Archive3/"

# Get a list of all the .mkv files in the folder
mkv_files = [f for f in os.listdir(input_folder) if f.endswith(".mkv")]
print(f'Processing {len(mkv_files)} MKV files')

for mkv_file in mkv_files:
    try:
        print(f'Processing: {mkv_file}')

        start_time = time.time()

        input_file = os.path.join(input_folder, mkv_file)
        output_file = os.path.join(output_folder, os.path.splitext(mkv_file)[0] + ".mp4")
        
        # Get the fps of the input file
        result = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate", "-of", "default=noprint_wrappers=1:nokey=1", input_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        fps = result.stdout.decode().strip()
        fps = float(fps.split("/")[0])/float(fps.split("/")[1])
        print(f'fps={fps}')
        
        # Convert the file
        logfile = open("progress.log", "w")
        subprocess.run(["ffmpeg", "-i", input_file, "-r", str(fps), "-c:v", "libx264", "-c:a", "aac", "-strict", "-2", "-map_metadata", "0", "-threads", "8", "-preset", "fast", output_file], stdout=logfile, stderr=logfile)
        logfile.close()

        end_time = time.time()
        total_time = end_time - start_time
        print(f'Time taken to process {mkv_file}: {total_time} seconds')

    except:
        print(f'Error processing {mkv_file}')

print("All files have been converted and saved in the output folder")