# Import packages
import os
import skimage.data
import matplotlib.pyplot as plt

# Creating a function to load the data. Returns two lists, one with images and another with the labels
def load_data(data_dir):
    '''
    Loads a data set and returns two lists:
  
    images: a list of Numpy arrays, each representing an image.
    labels: a list of numbers that represent the images labels.
    '''
    
    # list the existent directories in the chosen path
    directories = [d for d in os.listdir(data_dir) 
                   if os.path.isdir(os.path.join(data_dir, d))]
    labels = []
    images = []
    for d in directories:
        # Save in a list the names of each directory
        label_dir = os.path.join(data_dir, d)
        # Save in a list the path to each image in each directory
        file_names = [os.path.join(label_dir, f) 
                      for f in os.listdir(label_dir) if f.endswith(".ppm")]
        for f in file_names:
            # Append to images the image read
            images.append(skimage.data.imread(f))
            # Append to label the label which is represented as directory name
            labels.append(int(d))
    return images, labels

def display_images_and_labels(images, labels):
    '''
    Load images and labels and display a sample of images from the dataset
    '''
    unique_labels = set(labels)
    plt.figure(figsize =(15, 15))
    i = 1
    for label in unique_labels:
        image = images[labels.index(label)]
        plt.subplot(8, 8, i)  
        plt.axis('off')
        plt.title("Label {0} ({1})".format(label, labels.count(label)))
        i += 1
        _ = plt.imshow(image)
    plt.show()

def display_images(images, labels, label):
    '''
    Load images and labels and the label number received
    Display images corresponding to the requested label
    '''
    # Display up to 24 images
    limit = 24 
    plt.figure(figsize=(15, 5))
    i = 1

    start = labels.index(label)
    end = start + labels.count(label)
    for image in images[start:end][:limit]:
        plt.subplot(3, 8, i)  
        plt.axis('off')
        i += 1
        plt.imshow(image)
    plt.show()

