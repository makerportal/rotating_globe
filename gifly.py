# Function for making animated rotating globe GIF
import matplotlib
import matplotlib.pyplot as plt
import os,imageio

def gif_maker(gif_name,png_dir,gif_indx,num_gifs,dpi=90):
    # make png path if it doesn't exist already
    if not os.path.exists(png_dir):
        os.makedirs(png_dir)

    # save each .png for GIF
    # lower dpi gives a smaller, grainier GIF; higher dpi gives larger, clearer GIF
    fig = plt.gcf()
    fig_size = fig.get_size_inches()
    bbox = matplotlib.transforms.Bbox([[0.0,0.0],[fig_size[0],fig_size[1]]])
    plt.savefig(png_dir+'frame_'+str(gif_indx)+'_.png',dpi=dpi,facecolor=fig.get_facecolor(),bbox_inches=bbox)
##    plt.close('all')

    if gif_indx==num_gifs-1:
        # sort the .png files based on index used above
        images,image_file_names = [],[]
        for file_name in os.listdir(png_dir):
            if file_name.endswith('.png'):
                image_file_names.append(file_name)       
        sorted_files = sorted(image_file_names, key=lambda y: int(y.split('_')[1]))

        # define some GIF parameters
        
        frame_length = 0.1 # seconds between frames
        end_pause = 0.1 # seconds to stay on last frame
        # loop through files, join them to image array, and write to GIF called 'wind_turbine_dist.gif'
        for ii in range(0,len(sorted_files)):       
            file_path = os.path.join(png_dir, sorted_files[ii])
            if ii==len(sorted_files)-1:
                for jj in range(0,int(end_pause/frame_length)):
                    images.append(imageio.imread(file_path))
            else:
                images.append(imageio.imread(file_path))
        # the duration is the time spent on each image (1/duration is frame rate)
        imageio.mimsave(gif_name, images,'GIF',duration=frame_length)
