class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/lsw/LSW/2023/new/UAV/ostrack-deit'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/lsw/LSW/2023/new/UAV/ostrack-deit/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/lsw/LSW/2023/new/UAV/ostrack-deit/pretrained_networks'
        self.lasot_dir = '/home/lsw/LSW/2023/new/UAV/data/lasot'
        self.got10k_dir = '/home/lsw/LSW/2023/new/UAV/data/got10k/train'
        self.got10k_val_dir = '/home/lsw/LSW/2023/new/UAV/data/got10k/val'
        self.lasot_lmdb_dir = '/home/lsw/LSW/2023/new/UAV/data/lasot_lmdb'
        self.got10k_lmdb_dir = '/home/lsw/LSW/2023/new/UAV/data/got10k_lmdb'
        self.trackingnet_dir = '/home/lsw/LSW/2023/new/UAV/data/trackingnet'
        self.trackingnet_lmdb_dir = '/home/lsw/LSW/2023/new/UAV/data/trackingnet_lmdb'
        self.coco_dir = '/home/lsw/LSW/2023/new/UAV/data/coco'
        self.coco_lmdb_dir = '/home/lsw/LSW/2023/new/UAV/data/coco_lmdb'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/lsw/LSW/2023/new/UAV/data/vid'
        self.imagenet_lmdb_dir = '/home/lsw/LSW/2023/new/UAV/data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
