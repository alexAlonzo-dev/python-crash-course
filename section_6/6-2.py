numbers = {
    'alice': 5,
    'alex': 42,
    'amlo': 4,
}

print(f"amlo's favorite number: {numbers.get('amlo', 'Does not exists')}")
print(f"unkowns favorite number: {numbers.get('unkown', 'Does not exists')}")