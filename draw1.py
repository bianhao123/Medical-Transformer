# %%
import matplotlib
matplotlib.use('TkAgg') #这一句应该放在 import pyplot前面
import matplotlib.pyplot as plt
from WSI_handling import wsi


i = 0
img_name = '/data/bianhao/PAIP/Training_phase_1/Training_phase_1_001/01_01_0083.svs'
xml_name = '/data/bianhao/PAIP/Training_phase_1/Training_phase_1_001/01_01_0083.xml'
w = wsi(img_name, xml_name)
plt.imshow(w.get_wsi(desired_mpp=8))

# %%
# plt.show(w.get_annotated_region(desired_mpp=8, colors_to_use='other',annotation_idx='largest')[1])
