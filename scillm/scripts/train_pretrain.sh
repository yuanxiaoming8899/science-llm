#!/bin/bash

deepspeed --include localhost:0,1,2,3,4,5,6,7 --master_addr 127.0.0.1 --master_port 28457 train_pretrain.py \
    --model scillm\
    --model_path baichuan-inc/baichuan-7B\
    --train_data_path ../data/pretrain/train \
    --save_path ./ckpt/scillm_baichuan/ \
    --log_path ./rest/scillm_baichuan/
