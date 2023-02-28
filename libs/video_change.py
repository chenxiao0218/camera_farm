import cv2
from multiprocessing import Pool
import time
import camera_control


class Video:

    def __init__(self,camera):

        self.camera = camera

    def test_stability(self, camera_number, width, height, fps, times=60 * 60):
        """
         stability test,start all camera in different process
         once failed,camera light will become yellow
         one time takes 2 second,it will determine your stability test time
        :param camera_number:
        :return:
        """
        camera = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
        ret, im = camera.read()
        width = int(width)
        height = int(height)
        fps = int(fps)
        if ret:
            # cv2.imshow('test',im)
            camera.set(cv2.CAP_PROP_FPS, fps)
            camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            count = 0

            while True:
                real_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
                real_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
                real_fps = int(camera.get(cv2.CAP_PROP_FPS))

                # need change,what will happen if fail
                if real_width != width or real_height != height or real_fps != fps:
                    print('real width is {},test failed'.format(real_width))
                    self.camera.yellow_light_on()
                    return False

                else:
                    print('real width is {},test pass'.format(real_width))

                time.sleep(1)

                if count >= times:
                    print('test end')
                    return True


if __name__ == '__main__':
    p = Pool(3)
    for i in range(5):
        p.apply_async(Video().test_stability, args=(i, 1920, 1080, 20))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
