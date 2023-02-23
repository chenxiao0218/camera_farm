import cv2
from multiprocessing import Pool
import time
import mode_change


class Video:

    def __init__(self):
        self.count = 0
        self.mode = mode_change.Mode()

    def on(self, camera_number):
        """
         video on,start all camera in different process
         once failed,camera light will keep on after the test end

        :param camera_number:
        :return:
        """
        camera = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
        ret, im = camera.read()
        if ret:
            camera.set(cv2.CAP_PROP_FPS, 30.0)
            camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

            while True:
                width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
                height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
                fps = camera.get(cv2.CAP_PROP_FPS)

                # mode change
                self.count += 1
                if self.count % 3 == 0:
                    self.mode.turn_to_manual()
                    self.mode.turn_on_hdr()
                if self.count % 4 == 0:
                    self.mode.turn_to_gallery()
                if self.count % 5 == 0:
                    self.mode.turn_to_autoframing()
                    self.mode.turn_off_hdr()
                time.sleep(2)

                # need change,what will happen if fail
                if int(width) == 1920:
                    pass

                if self.count >= 10000:
                    print('test end')
                    break


if __name__ == '__main__':
    p = Pool(3)
    for i in range(5):
        p.apply_async(Video().on, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
