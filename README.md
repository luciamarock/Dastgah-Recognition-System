# Dastgah-Recognition-System

This software implements a Dastgah Recognition System using Python with C++ dependencies. 
This repository enables complete reproducibility of the results presented in our paper "Automatic Dastgah Recognition using Markov Models" published at the 14th International Symposium on Computer Music Multidisciplinary Research (CMMR). 
Paper available at: http://mtg.upf.edu/node/3975

Audio files in MP3 format should be placed in the ./pdct_ir/data directory. The data folder includes annotations.json containing metadata for the audio samples used in our research.

System Requirements and Setup:

1. Programming Environment:
- Python 3.7+ (updated from Python 2.x)
- C++ 14 or later
- Linux-based OS (Ubuntu 18.04+ recommended)
- Bash shell

2. Python Dependencies (with minimum versions):
- essentia >= 2.1.6
- numpy >= 1.19.0
- scipy >= 1.6.0
- matplotlib >= 3.3.0
- soundfile >= 0.10.3
- seaborn >= 0.11.0
- pandas >= 1.2.0

3. C++ Requirements:
- GCC 6.0+
- Essential build tools (build-essential package on Ubuntu)
- Essentia library dependencies:
  - FFTW3
  - libavcodec
  - libavformat
  - libavutil
  - libsamplerate
  - TagLib

4. Directory Structure:
- ./scores/: Contains reference score files (.csv)
  CSV format: [timestamp, pitch, duration, intensity]
- ./pdct_ir/data/: Contains input audio files
- ./pdct_ir/data/annotations.json: Audio metadata file

5. Audio File Requirements:
- Format: MP3
- Sample Rate: 44100 Hz
- Minimum Bitrate: 192 kbps
- Channel: Mono or Stereo
- Duration: 30 seconds to 10 minutes recommended

6. System Resources:
- RAM: Minimum 4GB, 8GB recommended
- Storage: 
  - 1GB for software installation
  - 2GB minimum free space for analysis files
  - Additional space for audio files (~10MB per minute of audio)

7. Performance Considerations:
- Processing time: ~2-3x real-time duration per audio file
- Temporary storage: Up to 100MB per processed file


## Usage Workflow

1. **Prepare Your Audio Files**
   - Place your Iranian classical music MP3 files in `./pdct_ir/data`.
   - Supported Dastgahs: Segah, RastPanjgah, Nava, Mahour, Homayun, Chahargah, Shur.

2. **Update Annotations**
   - Create or update `annotations.json` in `./pdct_ir/data` with your audio metadata:
   - Each entry should follow this format:

   ```json
   {
       "release_mbid": "[optional musicbrainz ID]",
       "recording_mbid": "[recording ID or track number]",
       "local_file_name": "YourAudioFile.mp3",
       "tonic": 120.0,
       "dastgah": "shur"
   }
   ```

3. **Run Pitch Detection**
   - First, process the audio file to extract pitch features:

     ```bash
     python pdct_ir/main.py YourAudioFile
     ```

   - Then, run the Markov model classification:

     ```bash
     cd markov
     ./processing.sh dastgah_name file_number total_files
     ```

     For example:

     ```bash
     python pdct_ir/main.py Shur_1
     cd markov
     ./processing.sh Shur 1 5
     ```

4. **View Results**
   - The program will generate several files:
     - Pitch extraction files in `./pdct_ir/data`.
     - Classification matrices in `./markov/matrices`.
     - Final results in `./markov/matrices/results.log`.

5. **Optional Visualization**
   - Use the following code to visualize the pitch distribution:

     ```python
     plt.figure()
     plt.plot(pitch_distribution_tonicRef.bins, pitch_distribution_tonicRef.vals)
     plt.title('Pitch distribution')
     plt.show()
     ```

   - The program uses a two-step process:
     1. Feature extraction using the predominant melody extraction algorithm.
     2. Dastgah classification using Markov models.

   - The results show the likelihood of the input audio belonging to each Dastgah class, as visualized in the confusion matrix:

     ```python
     plt.figure(figsize=(11, 8))
     plt.title('Bhattacharyya likelihood', size=25)
     sn.heatmap(df_cm, cmap="Greys", annot=True, annot_kws={"size": 15})
     ```