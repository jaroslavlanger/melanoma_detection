T = 8 # Number of gradient orientations
M = 6 # Number of Excitation bins
# WEIGHTS = (0.2688, 0.0852, 0.0955, 0.1000, 0.1018, 0.3487)
WEIGHTS = [1/M for i in range(M)]
S = 20 # Granularity of excitation per gradient orientation group

def get_image_path(name):
    return f'./data/train_512/{name}.jpg'
    # return f'./data/train/{name}.jpg'

def get_image(name):
    return skimage.io.imread(get_image_path(name))

def make_segment(image: np.array, *, window_size=64) -> np.array:
    y_size, x_size, *_ = image.shape
    x_start = (x_size - window_size) // 2
    x_end = x_start + window_size
    y_start = (y_size - window_size) // 2
    y_end = y_start + window_size
    return image[y_start:y_end, x_start:x_end]

def resize_image(image, size=128):
    image = make_segment(image, window_size=min(image.shape[:2]))
    aa = False # True
    image = skimage.transform.resize(image, (size, size), anti_aliasing=aa)
    image = np.around(image * 255).astype(int)
    return image

def equalize_hist(image):
    return np.array([
        skimage.exposure.equalize_hist(image[:, :, 0]),
        skimage.exposure.equalize_hist(image[:, :, 1]),
        skimage.exposure.equalize_hist(image[:, :, 2])
    ]).transpose((1, 2, 0))

def make_greyscale(image):
    # Y = 0.2125 R + 0.7154 G + 0.0721 B
    return 0.2125*image[:,:,0] + 0.7154*image[:,:,1] + 0.0721*image[:,:,2]
    # return skimage.color.rgb2gray(image)

def apply_f00(matrix):
    f00 = np.array([[1,  1,  1],
                    [1, -8,  1],
                    [1,  1,  1]])
    return signal.convolve2d(matrix, f00, mode='valid')

def apply_f01(matrix):
    return matrix[1:-1, 1:-1]

def apply_f10(matrix):
    f10 = np.array([[0, -1,  0],
                    [0,  0,  0],
                    [0,  1,  0]])
    return signal.convolve2d(matrix, f10, mode='valid')

def apply_f11(matrix):
    f11 = np.array([[0,  0,  0],
                    [1,  0, -1],
                    [0,  0,  0]])
    return signal.convolve2d(matrix, f11, mode='valid')

def get_differential_excitation(matrix):
    v00 = apply_f00(matrix)
    v01 = apply_f01(matrix)
    # return np.divide(v00, v01)
    return np.arctan(np.divide(v00, v01))
    #return np.arctan2(v00, v01)

def arctan2(v11, v10):
    theta = np.arctan(np.divide(v11, v10))
    if v11 > 0 and v10 > 0:
        return theta
    elif v11 > 0 and v10 < 0:
        return np.pi + theta
    elif v11 < 0 and v10 < 0:
        return theta - np.pi
    else:
        return theta

def big_theta_t(v11, v10):
    theta = np.arctan2(v11, v10)
    theta_1 = theta + np.pi
    # return theta_1
    t = np.mod(np.floor(theta_1*T/(2*np.pi) + 1/2), T)
    theta_t = 2*t*np.pi / T
    return theta_t

def get_gradient_orientation(matrix):
    v11 = apply_f11(matrix)
    v10 = apply_f10(matrix)
    return big_theta_t(v11, v10)

def show_excit_and_grad(image):
    fig, axs = plt.subplots(2, 3, figsize=(10, 4))
    axs[0, 0].imshow(image)
    image = make_greyscale(image)
    grad_ori = get_gradient_orientation(image)
    diff_excit = get_differential_excitation(image)

    excit_range=[-np.pi/2, np.pi/2]
    counts, edges, ax = axs[0, 1].hist(diff_excit.flatten(), bins=M*S, range=excit_range)
    
    grad_range=[0, 2*np.pi]
    axs[0, 2].hist(grad_ori.flatten(), bins=T, range=grad_range)

    axs[1, 0].imshow(image)
    axs[1, 1].imshow(diff_excit)
    axs[1, 2].imshow(grad_ori)


def get_wld_histogram(image_name):
    image = get_image(image_name)
    image = resize_image(image, SIZE)
    image = equalize_hist(image)
    image = make_greyscale(image)
    grad_ori = get_gradient_orientation(image)
    diff_excit = get_differential_excitation(image)

    grad_range=[0, 2*np.pi]
    excit_range=[-np.pi/2, np.pi/2]

    h, x, y = np.histogram2d(grad_ori.flatten(),
                             diff_excit.flatten(),
                             bins=[T, M*S],
                             range=[grad_range, excit_range],
                             )

    wld = np.array([h[:, start:start+20].flatten() for start in range(0, M*S, 20)]).flatten()

    chunk = T * S
    for m in range(M):
        start, end = m*chunk, (m+1)*chunk
        wld[start:end] *= WEIGHTS[m]
    wld = wld / wld.sum()
    return wld

def histogram_intersection(h1, h2):
    return np.minimum(h1, h2).sum()

def histogram_distance(h1, h2):
    return 1 - histogram_intersection(h1, h2)
