from multiprocessing import Pool
from libs.video_change import Video


class Case:
    def __init__(self):
        self.pool = Pool(10)
        self.video = Video()

    def test_1080(self):
        for i in range(10):
            self.pool.apply_async(self.video.test_stability, args=(i, 1920, 1080, 20,))
        print('Waiting for all subprocesses done...')
        self.pool.close()
        self.pool.join()


    def test_4k(self):
        for i in range(10):
            self.pool.apply_async(self.video.test_stability, args=(i, 3840, 2160, 10,))
        print('Waiting for all subprocesses done...')
        self.pool.close()
        self.pool.join()

if __name__ == '__main__':
    Case().test_4k()