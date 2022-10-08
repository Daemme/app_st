import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt


def main():

    st.write('# Batatinha quando nasce, espalha a rama pelo chão!')

    df = pd.read_csv('~/pythonMineracao/Datasets/wine.data', header=None)

    """
    ## Muito brabo o app, apenas!
        1. Primeiro elemento
        2. Segundo elemento
        
    ## Mostrando a tabela
        
    """

    st.write(df)

    title = int(st.text_input('Valores de divisōes para o histograma', '5'))

    fig, ax = plt.subplots(1, 1)
    ax.hist(np.random.normal(20, 2, 100), bins = title)
    fig
    plt.show()


if __name__ == '__main__':
    main()
