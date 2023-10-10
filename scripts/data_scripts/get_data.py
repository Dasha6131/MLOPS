#!/usr/bin/python3

from catboost.datasets import adult

train, test = adult()

train.to_csv("/home/data-srv-admin/MLOPS/data/raw/train.csv", columns=train.columns)

test.to_csv("/home/data-srv-admin/MLOPS/data/raw/test.csv", columns=test.columns)







