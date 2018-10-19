import numpy as np
import matplotlib.pyplot as plt
import utils.utils as utils


def left_sobel(img):

    """
    Applies left sobel filter to a colored numpy image

    Parameters:
    arg1 (np.array): numpy image matrix

    Returns:
    np.array: filterd left sobel image
    """

    kernel = np.array([[1., 0., -1.],
                   [2., 0., -2.],
                   [1., 0., -1.]])

    img = utils.rgb2gray(img)

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1))

    for ix in range(new_image.shape[0]):
        for iy in range(new_image.shape[1]):
            im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1]]
            h_prod = im_patch * kernel

            new_image[ix, iy] = max(0, h_prod.sum())
    new_image = new_image.astype(np.uint8)
    new_image = utils.InvertGrayImg(new_image)
    return new_image


def right_sobel(img):

    """
    Applies right sobel filter to a colored numpy image

    Parameters:
    arg1 (np.array): numpy image matrix

    Returns:
    np.array: filterd right sobel image
    """

    kernel = np.array([[-1., 0., 1.],
                   [-2., 0., 2.],
                   [-1., 0., 1.]])

    img = utils.rgb2gray(img)

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1))

    for ix in range(new_image.shape[0]):
        for iy in range(new_image.shape[1]):
            im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1]]
            h_prod = im_patch * kernel

            new_image[ix, iy] = max(0, h_prod.sum())
    new_image = new_image.astype(np.uint8)
    new_image = utils.InvertGrayImg(new_image)
    return new_image


def top_sobel(img):

    """
    Applies top sobel filter to a colored numpy image

    Parameters:
    arg1 (np.array): numpy image matrix

    Returns:
    np.array: filterd top sobel image
    """

    kernel = np.array([[1., 2., 1.],
                   [0., 0., 0.],
                   [-1., -2., -1.]])

    img = utils.rgb2gray(img)

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1))

    for ix in range(new_image.shape[0]):
        for iy in range(new_image.shape[1]):
            im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1]]
            h_prod = im_patch * kernel

            new_image[ix, iy] = max(0, h_prod.sum())
    new_image = new_image.astype(np.uint8)
    new_image = utils.InvertGrayImg(new_image)
    return new_image


def gray_scale(img):
    """
    Applies gray scale filter to a colored numpy image

    Parameters:
    arg1 (np.array): numpy image matrix

    Returns:
    np.array: filterd gray scale image
    """
    return utils.rgb2gray(img)


def outline(img):

    """
    Applies Outline filter to a colored numpy image

    Parameters:
    arg1 (np.array): numpy image matrix

    Returns:
    np.array: filtered outlined image
    """

    kernel = np.array([[-1., -1., -1.],
                   [-1., 8., -1.],
                   [-1., -1., -1.]])

    img = utils.rgb2gray(img)

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1))

    for ix in range(new_image.shape[0]):
        for iy in range(new_image.shape[1]):
            im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1]]
            h_prod = im_patch * kernel

            new_image[ix, iy] = max(0, h_prod.sum())
    new_image = new_image.astype(np.uint8)
    new_image = utils.InvertGrayImg(new_image)
    return new_image


def sharpen(img):

    """
    Applies Sharpen filter to a colored numpy image

    Parameters:
    arg1 (np.array): numpy image matrix

    Returns:
    np.array: Sharpened image
    """

    kernel = np.array([[0., -1., 0.],
                   [-1., 5., -1.],
                   [0., -1., 0.]])

    img = utils.rgb2gray(img)

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1))

    for ix in range(new_image.shape[0]):
        for iy in range(new_image.shape[1]):
            im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1]]
            h_prod = im_patch * kernel

            new_image[ix, iy] = max(0, h_prod.sum())
    new_image = new_image.astype(np.uint8)
    return new_image


def emboss(img):

    """
    Applies Emboss filter to a colored numpy image

    Parameters:
    arg1 (np.array): numpy image matrix

    Returns:
    np.array: Filtered Emboss image
    """

    kernel = np.array([[-2., -1., 0.],
                   [-1., 1., 1.],
                   [0., 1., 2.]])

    img = utils.rgb2gray(img)

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1))

    for ix in range(new_image.shape[0]):
        for iy in range(new_image.shape[1]):
            im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1]]
            h_prod = im_patch * kernel

            new_image[ix, iy] = max(0, h_prod.sum())
    new_image = new_image.astype(np.uint8)
    return new_image
