import nibabel as nb
import numpy as np

# function to read volumetric tissue classification and turn into 3D array
def load_volume(mri_vol):
    # if input is a filename, try to load it
    if isinstance(mri_vol, basestring):
    # importing nifti files
        if (mri_vol.endswith('nii') or mri_vol.endswith('nii.gz')):
            img=nb.load(mri_vol)
            img_data=np.array(img.get_data())
            img_affine=img.get_affine()
            img_header=img.get_header()
            # importing mnc files using pyminc, suggest to download if missing
        elif mri_vol.endswith('mnc'):
            try:
                img=nb.minc2.load(mri_vol)
                img_data=np.array(img.get_data())
                img_affine=img.get_affine()
                img_header=img.get_header()
            except ValueError:
                print "loading .mnc files requires h5py, try installing with:"
                print '"sudo pip install h5py"'
# option to add in more file types here, eg analyze
# if volume is already an np array
# elif isinstance(mri_vol,np.ndarray):
# img_data=np.array(mri_vol)
    else:
                raise ValueError('volume must be a either filename or a numpy array')
    return img_data, img_header, img_affine;


# function to save volume data
def save_volume(fname, data, affine, header=None, dtype='float32', CLOBBER=True):
    """
    Function to write volume data to file. Filetype is based on filename suffix
    Input:
        - fname:    you can figure that out
        - data:             numpy array
        - affine:              affine matrix
        - header:        header data to write to file (use img.header to get the header of root file)
        - data_type:        numpy data type ('uint32', 'float32' etc)
        - CLOBBER:          overwrite existing file
    """
    import os
    img = nb.Nifti1Image(data, affine, header=header)
    if (fname.endswith('nii') or fname.endswith('nii.gz')):
        img = nb.Nifti1Image(data, affine, header=header)
        if dtype is not None:  # if there is a particular data_type chosen, set it
        # data=data.astype(data_type)
            img.set_data_dtype(dtype)
        if not (os.path.isfile(fname)) or CLOBBER:
            img.to_filename(fname)
        else:
            print("This file exists and CLOBBER was set to false, file not saved.")
 #    elif full_fileName.endswith('mnc')


# function to make 1D arrays from meshes geometry and data
