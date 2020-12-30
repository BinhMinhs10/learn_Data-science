from template.preprocess import Preprocess
from template.model import run_model
from template.predict import predict


def main():
    preprocess = Preprocess()
    df = preprocess()
    df = run_model(df)
    df, accuracy = predict(df)


if __name__=='__main__':
    main()