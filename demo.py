import os
# microblock: 16*16
# 
centerX = 360
centerY = 120
prefix = '/media/xulzee/备份/'
center_x = [centerX, centerX - 240, centerX, centerX - 240]
center_y = [centerY, centerY, centerY - 120, centerY - 120]
for i in range(1, 5):
    input_yuv = '/media/xulzee/LaCie/xulzee/test_video/2_' + str(i) + '_3840x1920.yuv'
    output_yuv = '/media/xulzee/LaCie/xulzee/test_video/new2_' + str(i) + '_3840x1920.yuv'
    output_264 = prefix + 'test_264/' + str(i) + '.264'
    output_mp4 = prefix + 'test_video/3/new2_' + str(i) + '.mp4'
    if (center_x[i-1] + 65 >= 0) and (center_x[i-1] - 65 <= 240) and (center_y[i-1] + 35 >= 0) and (center_y[i-1] - 35 <= 120):
        os.system('~/Desktop/x264mbMod/x264 --center-x %d --center-y %d -o \
                        %s %s' % (center_x[i - 1], center_y[i - 1], output_264, input_yuv))
        os.system('ffmpeg -i %s %s' % (output_264, output_yuv))
        os.system('ffmpeg -s 3840x1920 -i %s -crf 0 %s' % (output_yuv, output_mp4))
