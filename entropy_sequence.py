import argparse
import os
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from tqdm import tqdm
import torch.nn as nn
from einops import rearrange

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, default='', help='input file', required=True)
    parser.add_argument('--output', '-o', type=str, default='', help='output file')
    parser.add_argument('--model', type=str, default='bert', help='model name')
    parser.add_argument('--model_path', type=str, default='', help='load model locally if specified')
    parser.add_argument('--batch_size', '-bs', type=int, default=32)
    parser.add_argument('--start_batch', type=int, default=0)
    return parser

def load_model(model_name, model_path):
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

def calculate_entropy(logits, labels, mask):
    log_softmax = nn.LogSoftmax(dim=1)
    criterion = nn.NLLLoss(reduction='none')

    logits = rearrange(logits, 'B L V -> B V L')
    shift_logits = logits[..., :, :-1]
    shift_labels = labels[..., 1:]
    mask = mask[..., 1:]

    nll_loss = criterion(log_softmax(shift_logits), shift_labels).squeeze()
    masked_nll_loss = torch.masked_select(nll_loss, mask > 0)
    entropy = masked_nll_loss.mean()

    return entropy

@torch.no_grad()
def process(model, tokenizer, args):
    device = model.device
    with open(args.input, 'r') as fr:
        data = [line.strip() for line in fr.readlines()]
    if len(args.output) > 0:
        output_file = args.output
    else:
        if args.model_path:
            model_name = os.path.basename(args.model_path)
            output_file = f'{args.input}.model={model_name}.nll'
        else:
            output_file = f'{args.input}.model={args.model}.nll'
    num_batches = len(data) // args.batch_size
    if len(data) % args.batch_size > 0:
        num_batches += 1
    with open(output_file, 'w') as fw:
        for i in tqdm(range(args.start_batch, num_batches)):
            batch = data[i*args.batch_size: (i*args.batch_size+args.batch_size)]
            if len(batch) == 0:
                continue
            encoded_input = tokenizer(batch, return_tensors='pt', padding=True, truncation=True).to(device)
            input_ids = encoded_input['input_ids']
            mask = encoded_input['attention_mask']
            output = model(encoded_input, labels=input_ids)
            logits = output.logits.to(device)
            entropy = calculate_entropy(logits, input_ids, mask)
            fw.write(f'{entropy.item()}\n')

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    model, tokenizer = load_model(args.model, args.model_path)
    process(model, tokenizer, args)
