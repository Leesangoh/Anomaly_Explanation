import argparse
import os

from torch.backends import cudnn

<<<<<<< HEAD
=======
from src.data_factory.dbsherlock.utils import anomaly_causes
>>>>>>> bedb50b2573e5646126f903507d057b6aaee2c2a
from src.solver import Solver
from utils.utils import *


def str2bool(v):
    return v.lower() in ("true")


def main(config):
    cudnn.benchmark = True
    if not os.path.exists(config.model_save_path):
        mkdir(config.model_save_path)
    solver = Solver(vars(config))

    if config.mode == "train":
        solver.train()
    elif config.mode == "test":
        solver.test()

    return solver


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--num_epochs", type=int, default=20)
    parser.add_argument("--k", type=int, default=3)
    parser.add_argument("--win_size", type=int, default=25)
    parser.add_argument("--input_c", type=int, default=200)
    parser.add_argument("--output_c", type=int, default=200)
    parser.add_argument("--batch_size", type=int, default=1024)
    parser.add_argument("--pretrained_model", type=str, default=None)
    parser.add_argument("--dataset", type=str, default="DBS")
    parser.add_argument("--mode", type=str, default="train", choices=["train", "test"])
    parser.add_argument("--data_path", type=str, default="./dataset/dbsherlock/processed/tpce_3000")
    parser.add_argument("--model_save_path", type=str, default="checkpoints")
    parser.add_argument("--anormly_ratio", type=float, default=4.00)
    parser.add_argument("--step_size", type=int, default=25)
    parser.add_argument("--find_best", type=bool, default=True)
    parser.add_argument(
        "--cause", type=str, default="all", choices=["all"] + anomaly_causes
    )

    config = parser.parse_args()

    args = vars(config)
    print("------------ Options -------------")
    for k, v in sorted(args.items()):
        print("%s: %s" % (str(k), str(v)))
    print("-------------- End ----------------")
    main(config)
