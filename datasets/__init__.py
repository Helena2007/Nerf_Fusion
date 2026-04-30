from .nerf import NeRFDataset
from .nsvf import NSVFDataset
from .colmap import ColmapDataset
from .nerfpp import NeRFPPDataset
from .scannet import ScanNetDataset
from ._google_scanned_obj import GoogleScannedDataset
from .superfaces import FlorenceSuperfacesDataset
from .child import Child_aiRenderDataset

dataset_dict = {'nerf': NeRFDataset,
                'nsvf': NSVFDataset,
                'colmap': ColmapDataset,
                'nerfpp': NeRFPPDataset,
                'scannet': ScanNetDataset,
                'google_scanned': GoogleScannedDataset,
                'superfaces': FlorenceSuperfacesDataset,
                'child': Child_aiRenderDataset}
