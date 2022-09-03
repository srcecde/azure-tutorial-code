import os
import pandas as pd

# get base path
base_dir = "/".join(os.path.realpath(__file__).split("/")[:-1])

def run():
    # read csv
    df = pd.read_csv(os.path.join(base_dir, "data/input/survey.csv"))

    # dropping colums except Industry Name & Code
    df = df[["Industry_name_NZSIOC", "Industry_code_ANZSIC06"]]

    # saving the new file to output dir in AFS
    df.to_csv(os.path.join(base_dir, "data/output/processed.csv"))
