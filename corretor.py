import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

nltk.download('punkt')
nltk.download('stopwords')


def corrigir_texto(texto):
    # Tokenização do texto em palavras
    palavras = word_tokenize(texto, language='portuguese')

    # Remoção de stopwords
    palavras_filtradas = [palavra.lower() for palavra in palavras if
                          palavra.lower() not in stopwords.words('portuguese')]

    # Stemming das palavras
    stemmer = RSLPStemmer()
    palavras_stemming = [stemmer.stem(palavra) for palavra in palavras_filtradas]

    # Reconstrução do texto corrigido
    texto_corrigido = ' '.join(palavras_stemming)

    return texto_corrigido


# Leitura do arquivo de texto
with open('audio0.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

# Correção do texto
texto_corrigido = corrigir_texto(texto)

# Imprimir texto corrigido
print(texto_corrigido)
