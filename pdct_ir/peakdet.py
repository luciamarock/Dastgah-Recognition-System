# Function definition for automatic scale-interval detection from pitch distribution
import numpy as np

def peakLocationDetection(pcd):
    '''A simple peak detection implementation for demonstration purposes
    Thresholds are manually set for this demo
    '''
    windowSize = 9  # should be odd
    midPointIndex = int(windowSize / 2)
    threshold = np.max(pcd) * 0.05
    peakIndexes = []
    for index in range(len(pcd)-windowSize):
        frame = pcd[index:index+windowSize]
        if np.argmax(frame) == midPointIndex and np.max(frame) > threshold:
            peakIndexes.append(index + midPointIndex)
    
    return peakIndexes