import time
import cv2
import threading

class VideoCamera:
    instance = None
    lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if cls.instance is None:
                cls.instance = super(VideoCamera, cls).__new__(cls)
                cls.instance.init_camera(*args, **kwargs)
        return cls.instance

    def init_camera(self, filter_type='none'):
        self.video = cv2.VideoCapture(0)
        self.filter_type = filter_type
        self.grabbed, self.frame = self.video.read()
        if not self.grabbed:
            print("Error: Could not grab initial frame.")
        self.running = True
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.release_camera()

    def release_camera(self):
        self.running = False
        if self.video.isOpened():
            self.video.release()
        VideoCamera.instance = None

    def get_frame(self):
        if not self.grabbed or self.frame is None:
            print("Error: Frame not grabbed.")
            return None
        image = self.frame
        if self.filter_type == 'gray':
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        elif self.filter_type == 'blur':
            image = cv2.GaussianBlur(image, (15, 15), 0)
        elif self.filter_type == 'canny':
            image = cv2.Canny(image, 100, 200)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        
        if image is None or image.size == 0:
            print("Error: Image is empty.")
            return None
        
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while self.running:
            if not self.video.isOpened():
                print("Reopening camera...")
                self.video.open(0)
            
            self.grabbed, self.frame = self.video.read()
            if not self.grabbed:
                print("Error: Could not grab frame.")
                time.sleep(1)  # Add a delay to prevent rapid logging
                continue

def gen(camera):
    while camera.running:
        frame = camera.get_frame()
        if frame is None:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
