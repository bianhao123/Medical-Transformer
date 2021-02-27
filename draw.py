# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %%
import matplotlib.pyplot as plt
from WSI_handling import wsi


# %%
img_fname = r'/data/bianhao/MoNuSegTrainingData/Tissue_Images/*.tif'
xml_fname = r'/data/bianhao/MoNuSegTrainingData/Annotations/*.xml'


# %%
import glob

img_fnames = sorted(glob.glob(img_fname))
xml_fnames = sorted(glob.glob(xml_fname))


# %%
img_fnames


# %%
i = 0
img_name = '/data/bianhao/PAIP/Training_phase_1/Training_phase_1_001/01_01_0083.svs'
xml_name = '/data/bianhao/PAIP/Training_phase_1/Training_phase_1_001/01_01_0083.xml'
w = wsi(img_name, xml_name)
plt.imshow(w.get_wsi(desired_mpp=8))


# %%
plt.imshow(w.mask_out_annotation(desired_mpp=8))




# %%
plt.show(w.get_annotated_region(desired_mpp=8, colors_to_use='other',annotation_idx='largest')[0])

# %%
img, mask = w.get_annotated_region(desired_mpp=8,colors_to_use='green',annotation_idx='largest',mask_out_roi=False)
plt.imshow(img);
plt.show()
plt.figure
plt.imshow(mask);

# %%
