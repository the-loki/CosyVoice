import os
from modelscope import snapshot_download

model_name = os.environ.get('TARGET_COSY_MODEL')

snapshot_download('iic/{}'.format(model_name), local_dir='pretrained_models/{}'.format(model_name))
snapshot_download('iic/CosyVoice-ttsfrd', local_dir='pretrained_models/CosyVoice-ttsfrd')
