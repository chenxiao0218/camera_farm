
if __name__ == '__main__':
    import cv2

    camera = cv2.VideoCapture(2, cv2.CAP_DSHOW)
    retval, im = camera.read()
    print(retval)
    # codec = 0x47504A4D  # MJPG
    camera.set(cv2.CAP_PROP_FPS, 30.0)
    # camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while (1):

        cv2.imshow("image", im)
        width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = camera.get(cv2.CAP_PROP_FPS)

        print('width = {},height = {},fps = {}'.format(width,height,fps))
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break

    camera.release()
    cv2.destroyAllWindows()