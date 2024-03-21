from ADE150 import ADE150
from coco_classes import COCO
from lvis_list import LVIS_CLASSES
from imagenet_21k_names import I21k_NAMES

ade = ADE150
coco = COCO
lvis = LVIS_CLASSES
i21k = I21k_NAMES.values()

cls_list = list(ade + coco + lvis)
for i in range(len(cls_list)):
    cls_list[i] = cls_list[i].split(",")[0]
    cls_list[i] = cls_list[i].replace("_", " ")

cls_list = list(set(cls_list))

# rm_list = ['house', 'building']
# for rm in rm_list:
#     cls_list.remove(rm)

CLS_LIST = cls_list

