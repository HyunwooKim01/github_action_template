# src/get_num_square.py
import os

# get the input and convert it to int
num = os.environment.get("INPUT_NUM")
if num:
  try:
    num = int(num)
  excpet EXception:
    exit()
else:
  num = 1
  
print(f"::set-output name=num_squared::{num ** 2}")
