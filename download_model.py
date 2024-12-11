import os
from modelscope import snapshot_download

model_name = os.environ.get('TARGET_COSY_MODEL')

snapshot_download('iic/{}'.format(model_name))
