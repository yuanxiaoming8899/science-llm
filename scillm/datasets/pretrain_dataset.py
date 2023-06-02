import copy
import linecache
from itertools import chain,islice
import os
import json
from tqdm import tqdm
import ipdb
import random
from torch.nn.utils.rnn import pad_sequence
from dataclasses import dataclass, field
from typing import Callable, Dict, Sequence

import torch
import torch.distributed as dist
import transformers
from torch.utils.data import Dataset


def iter_count(file_name):
    from itertools import (takewhile, repeat)
    buffer = 1024 * 1024
    with open(file_name) as f:
        buf_gen = takewhile(lambda x: x, (f.read(buffer) for _ in repeat(None)))
        return sum(buf.count('\n') for buf in buf_gen)


class PretrainDataset(Dataset):

    def __init__(self, **args):
        super(PretrainDataset, self).__init__()
        self.args = args
        self.tokenizer = args['tokenizer'] 
        # cached dataset
        self.cache_f_reader = open(args['data_path'])
        self.cache = []
        self.cache_tokens = []
        self.current_num = 0
        self.instance_num = iter_count(args['data_path'])
        print(f'[!] collect {self.instance_num} samples for training')

    def __len__(self):
        return self.instance_num

    def __getitem__(self, i) -> Dict[str, torch.Tensor]:
        if len(self.cache_tokens) < self.args['max_seq_length']:
            self.cache = list(islice(self.cache_f_reader, self.current_num, self.current_num + self.args['max_dataset_cache_size']))
            self.cache = [json.loads(single_data) for single_data in self.cache]
            self.current_num += self.args['max_dataset_cache_size']
            random.shuffle(self.cache)
            # concatentate
            self.cache_tokens = []
            for item in self.cache:
                self.cache_tokens += item['tokens'] + [self.tokenizer.eos_token_id]
        tokens = self.cache_tokens[:self.args['max_seq_length']]
        del self.cache_tokens[:self.args['max_seq_length']]
        # read a cache of the training instance
        return torch.LongTensor(tokens)

    def collate(self, instances):
        input_ids = torch.nn.utils.rnn.pad_sequence(
            instances,
            batch_first=True,
            padding_value=self.tokenizer.pad_token_id
        )
        labels = torch.nn.utils.rnn.pad_sequence(instances, batch_first=True, padding_value=-100)
        return dict(
            input_ids=input_ids,
            labels=labels,
            attention_mask=input_ids.ne(self.tokenizer.pad_token_id),
        )
