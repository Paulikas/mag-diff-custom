from config import PATH_TO_MODEL_1, PATH_TO_MODEL_2
from diff import get_diff

def load_model_data(path):
    pass




if __name__ == "__main__":
         
    pc1 = load_model_data(PATH_TO_MODEL_1)
    pc2 = load_model_data(PATH_TO_MODEL_2)

    diff = get_diff(pc1, pc2)

    