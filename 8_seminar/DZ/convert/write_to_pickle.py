import pickle

def write_pickle(data: list = [], name: str = "pickle_data"):
    with open(name, "wb") as f:
        pickle.dump(data,f)


