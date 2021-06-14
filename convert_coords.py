def worldToVoxelCoord(world_coord, origin, spacing, orientation):
    m = orientation.reshape(3,3)
    m = np.linalg.inv(m)
    m = m.ravel()
    wo = world_coord - origin
    voxel_coord = [
        (m[6]*wo[0]+m[7]*wo[1]+m[8]*wo[2])/spacing[2],
        (m[3]*wo[0]+m[4]*wo[1]+m[5]*wo[2])/spacing[1],
        (m[0]*wo[0]+m[1]*wo[1]+m[2]*wo[2])/spacing[0]
    ]
    return voxel_coord

def parse_itk_image(itk_image):
    numpyImage = sitk.GetArrayFromImage(itk_image)
    numpyOrigin = np.array(list(itk_image.GetOrigin()))
    numpySpacing = np.array(list(itk_image.GetSpacing()))
    numpyOrientation = np.array(list(itk_image.GetDirection()))
    return numpyImage, numpyOrigin, numpySpacing, numpyOrientation


labelmapPath = "/home/sliceruser/work/Documents/3D_slicer/pat16spie/1.nii"

itk_image = sitk.ReadImage(labelmapPath)


volume_orig, origin, spacing, orientation = parse_itk_image(itk_image)


k,j,i = worldToVoxelCoord([-36, 203, 909.9], origin, spacing, orientation)

print(k,j,i)