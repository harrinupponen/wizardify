import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def main():
    
    main_folder = 'dnd_classes/'
    classes = ['barbarian', 'bard', 'cleric', 'druid',
    'fighter', 'monk', 'paladin', 'ranger', 'rogue',
    'sorcerer', 'warlock', 'wizard']
    data_type = 'train' # In our case data types are 'train', 'valid', 'test'
    image_type = 'jpg' # We used only .jpg images
    number_of_images = 8 # Images per folder
    sets = 9 # 9 sets for training, 5 for valid, 2 for testing in our case
    save_format = 'png'

    # Iterates through all the classes
    for z in range(0, len(classes)):
        
        # This is used in pathing
        character = classes[z]
        
        # These sets increase the values of ImageDataGenerator by every iteration
        for y in range(0, sets):
            
            gen = ImageDataGenerator(
                rotation_range = 10 * y, 
                width_shift_range = 0.1,    
                height_shift_range = 0.1, 
                shear_range = 0.15 * y, 
                zoom_range = 0.1 * y,
                channel_shift_range = 10.0 * y, 
                horizontal_flip = True,
                brightness_range = [0.2,2.0],
                )
            
            # This goes through all the images in the folder
            # Images must be named properly so that the right path can form
            # For example: dnd_classes/samples/wizard/wizard_1.jpeg
            for x in range(1, number_of_images + 1):
                image_path = 'dnd_classes/samples/' + character + '/' + character + '_' + str(x) + '.' + image_type
                image = np.expand_dims(plt.imread(image_path), 0)

                # This saves 5 versions of every picture into given path
                # For example: dnd_classes/train/wizard_1.png
                i = 0
                for batch in gen.flow(
                    image, 
                    batch_size=number_of_images,
                    save_to_dir=main_folder + data_type + '/' + character,
                    save_prefix=character,
                    save_format=save_format
                    ):
                    
                    i += 1
                    if i > 5:
                        print('Set' + str(y +1) + '/' + str(sets) + ' ' + image_path + ' done')
                        print('------')
                        break

    print('All done!')
    
if __name__ == "__main__":
        main()