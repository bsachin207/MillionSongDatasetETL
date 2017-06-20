# -*- coding: utf-8 -*-
"""
Name: Sachin Badgujar
Email: sachin.d.badgujar@gmail.com
Purpose: Million song dataset - Extracting song information from HDF5 file to a CSV

imported helper function to get hdf5 file attributes
Credits - GNU General Public License
"""


import time
start_time = time.time()
import sys
import os
import csv
sys.path.append('/home/sachin/clutter/Scripts/lib')
import hdf5_getters as HDF5



def get_filenames(parent_dir):
    """
    Generator function to yield each file name in parent directory and
    sub directories
    """
    
    if not os.path.isdir(parent_dir):
        print parent_dir,' is Not a directory'
        sys.exit(1)
    
    #return all file names in the parent directory and sub directories
    return [os.path.join(p, name) for p,s,f in os.walk(parent_dir) for name in f ]
   
if __name__=='__main__':
        
    #input the hdf5 parent directory
    if len(sys.argv) != 2:
        print "The only argument should be the parent directory for HDF5 files"
        sys.exit(1)
    
    print "\n################# Starting Extraction #################\n"
    file_directory = get_filenames(sys.argv[1])
    width = len(file_directory)

    out = csv.writer(open("Songs.csv","w"))    
    for i in range(len(file_directory)):
        row = []
        f = HDF5.open_h5_file_read(file_directory[i])
        row.append(HDF5.get_song_id(f))
        row.append(HDF5.get_track_id(f))
        row.append(HDF5.get_title(f))
        row.append(HDF5.get_artist_name(f))
        row.append(HDF5.get_artist_id(f))
        row.append(HDF5.get_year(f))
        row.append(HDF5.get_tempo(f))
        out.writerow(row)
        f.close()
        
        percent = int(((i+1)*100)//width)
        sys.stdout.write(('-' * percent)+(''*(100-percent))+("\r [ %d"%percent+"% ] "))
        sys.stdout.flush()
        
    print "\n Done in ",str(time.time() - start_time) ," seconds\n"
    print "\n################# Starting Hive #######################\n"