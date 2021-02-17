from io import BytesIO

import comet_ml

class Logger(object):

    def __init__(self, experiment: comet_ml.Experiment):
        self.experiment = experiment

    def scalar_summary(self, name, value, step):
        self.experiment.log_metric(name, value, step)

    def image_summary(self, name, image, step):
        self.experiment.log_image(image, name, step=step)

    def image_list_summary(self, tag, images, step):
        if len(images) == 0:
            return
        for i, img in enumerate(images):
           self.experiment.log_image(img, name=f"{tag}_{i}", step=step)
