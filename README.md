# APE: Aligning and Prompting Everything All at Once for Universal Visual Perception


<p align="center">
    <img src="./.asset/ape.png" width="96%" height="96%">
</p>


<font size=7><div align='center' > :grapes: \[[arXiv Paper](https://arxiv.org/abs/2312.02153)\] &nbsp; :apple: \[[Online Demo](https://huggingface.co/spaces/shenyunhang/APE)\] </div></font>


---
This repository contains a modified implementation of the CVPR 2024 paper *APE: Aligning and Prompting Everything All at Once for Universal Visual Perception*. You can use a simple command to extract pixel-aligned semantic features from any images.



## :hammer_and_wrench: Install 

1. Clone the APE repository from GitHub:

```bash
git clone https://github.com/Atrovast/APE
cd APE
```

2. Install the required dependencies and APE:

```bash
pip3 install -r requirements.txt
python3 -m pip install -e .
```
You can install the dependencies directly into the GOI environment without conflicts.

3. Download the `APE-L_D` checkpoint (also referred to as `APE-D` in older versions) and place it in the root directory, keeping it named as `model_final.pth`. <a href="https://huggingface.co/shenyunhang/APE/blob/main/configs/LVISCOCOCOCOSTUFF_O365_OID_VGR_SA1B_REFCOCO_GQA_PhraseCut_Flickr30k/ape_deta/ape_deta_vitl_eva02_clip_vlf_lsj1024_cp_16x4_1080k_mdl_20230829_162438/model_final.pth">HF link</a> 


## :arrow_forward: Extract the Pixel-Aligned Semantic Feature for Images
You can run this single command to extract pixel-aligned semantic features for images:
```shell
python demo/demo_lazy.py -i ../datasets/360/bicycle/images_4/* --feat-out ../datasets/360/bicycle/clip_feat/
```
- `-i` or `--input`: Specifies the input images path.
- `--feat-out`: Specifies the output path for the extracted features.

For the -i option, use `*` to process all files in an image folder. Alternatively, you can specify individual images:

```shell
python demo/demo_lazy.py -i img1.png img2.png img3.png --feat-out ../datasets/360/bicycle/clip_feat/
```
**Due to the high dimensionality of pixel-aligned feature encoded by APE, we tend to use lower resolution (< 1.6k) images for encoding (i.e. images_4 folder for Mip360 dataset)**


## :black_nib: Citation

If you find this repo useful, please cite both papers:

```bibtex
@article{goi2024,
    title={GOI: Find 3D Gaussians of Interest with an Optimizable Open-vocabulary Semantic-space Hyperplane},
    author={Qu, Yansong and Dai, Shaohui and Li, Xinyang and Lin, Jianghang and Cao, Liujuan and Zhang, Shengchuan and Ji, Rongrong},
    journal={arXiv preprint arXiv:2405.17596},
    year={2024}
}
```

and

```bibtex
@inproceedings{APE,
  title={Aligning and Prompting Everything All at Once for Universal Visual Perception},
  author={Shen, Yunhang and Fu, Chaoyou and Chen, Peixian and Zhang, Mengdan and Li, Ke and Sun, Xing and Wu, Yunsheng and Lin, Shaohui and Ji, Rongrong},
  journal={CVPR},
  year={2024}
}
```
