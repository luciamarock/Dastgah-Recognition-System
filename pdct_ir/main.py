import os 
#import matplotlib.pyplot as plt
import numpy as np
from predominantMelodyMakam import PredominantMelodyMakam
from pitchDistribution import PitchDistribution
import histquantizer
import cleaner
import peakdet
import tonicext
import sys
''' UNUSED IMPORTS: import json import matplotlib.ticker as ticker import csv'''
CENTS_IN_OCTAVE=1200
#REF_PITCH=440
#num_int=24
history=15  #3 = circa 9 ms
mbid = sys.argv[1]
#mbid = 'Shur_2'
dataDir = './data'
#dataDir = '/home/luciamarock/MTG/pdct_ir/data'
mp3_filename = os.path.join(dataDir, '{}.mp3'.format(mbid))
wav_filename = os.path.join(dataDir, '{}.wav'.format(mbid))
print('found audio file')
#print(mp3_filename)
pitchFile = os.path.join(dataDir, '{}.pitch'.format(mbid))
histFile = os.path.join(dataDir, '{}.pitch_hist.json'.format(mbid))
dataFile = os.path.join(dataDir, '{}.csv'.format(mbid))
tonic_hz = tonicext.Tonicext(wav_filename)
#tonic_hz = 165.9
#print('Tonic: {} Hz'.format(round(tonic_hz, 2)))
#print('CENTS_IN_OCTAVE=', CENTS_IN_OCTAVE)
def compute_pitch(filename):
    extractor = PredominantMelodyMakam(filter_pitch=True)
    results = extractor.run(filename)
    pitch = results['settings']  # collapse the keys in settings
    pitch['pitch'] = results['pitch']  
    return pitch
    # If pitch file exists, read it, if not run extractor and create the pitch file
if not os.path.exists(pitchFile):
    print("Computing pitch distribution")
    pitch = compute_pitch(mp3_filename)
    # you can use the pitch file together with SonicVisualizer to view in sync with the spectrogram of the mp3 file
    pitchSeriesHz = []    
    timeSeries = []
    with open(pitchFile, 'w') as fp:
        for p_triplet in pitch['pitch']:
            fp.write(str(p_triplet[0]) + '\t' + str(p_triplet[1])+'\n')
            pitchSeriesHz.append(p_triplet[1])
            timeSeries.append(p_triplet[0])
    
    pitchSeriesHz = np.array(pitchSeriesHz)
else:
    pitchData = np.loadtxt(pitchFile)
    timeStamps = pitchData[:,0]
    pitchSeriesHz = pitchData[:,1]

'''capire il terzo elemento di pitch'''
#print('Pitch file available, you can use Sonic Visualizer at this step to check pitch extraction quality')
#pitchSeriesHz=quantizer.Quantizer(REF_PITCH,num_int,pitchSeriesHz)
'''
plt.plot(timeSeries,pitchSeriesHz)
plt.title('pitchSeriesHz')
plt.show()
'''
pd_params = {'kernel_width': 10, 'step_size':2.5}
'''# Computing pitch distribution with default reference frequency = REF_PITCH
pitch_distribution = PitchDistribution.from_hz_pitch(pitchSeriesHz, REF_PITCH, **pd_params)
pitch_distribution.to_json(histFile)'''

# Computing pitch distribution with reference frequency = tonic
pitch_distribution_tonicRef = PitchDistribution.from_hz_pitch(pitchSeriesHz, tonic_hz, **pd_params)
hist_file_wrt_tonic = os.path.join(dataDir, '{}.pitch_hist_wrtTonic.json'.format(mbid))
pitch_distribution_tonicRef.to_json(hist_file_wrt_tonic)
print('.csv score created')
'''plt.figure()
plt.plot(pitch_distribution_tonicRef.bins, pitch_distribution_tonicRef.vals)
plt.title('Pitch distribution')
plt.show()'''

intervals = []
intervals = peakdet.peakLocationDetection(pitch_distribution_tonicRef.vals)
for v in range(len(intervals)):
    intervals[v]=pitch_distribution_tonicRef.bins[intervals[v]]
pitchSeriesHz=histquantizer.Histquantizer(tonic_hz,CENTS_IN_OCTAVE,intervals,pitchSeriesHz)
'''
plt.plot(timeSeries,pitchSeriesHz)
plt.title('pitchSeriesHz_quantized')
plt.show()
'''
pitchSeriesHz=cleaner.Cleaner(history,pitchSeriesHz)
'''
#plt.figure()
plt.plot(timeSeries,pitchSeriesHz)
plt.title('pitchSeriesHz_quantized')
plt.show()
'''
'''plt.figure()
plt.plot(timeSeries,pitchSeriesHz)
plt.title('pitchSeriesHz_quantized_cleaned')
plt.show()'''
data = np.array([timeSeries,pitchSeriesHz])
data = data.T
with open(dataFile, 'w+') as datafile_id:
    #writer=csv.writer(datafile_id, delimiter='\t')
    #writer.writerows(zip(timeSeries,pitchSeriesHz))
    np.savetxt(datafile_id, data,fmt=['%.3f','%.3f'],delimiter="\t")