# Título

really safe rsa

# Descrição

Usei números extremamente seguros para implementar a criptografia!

OBS 1: A flag está no formato: HIK_flag

A flag são os 15 ÚLTIMOS dígitos da chave privada `d`

Exemplo: `d = 123456789101112131415161718192021222324`

A flag resultante seria: `HIK_718192021222324`

OBS 2: Aqui no meu computador leva no máximo 2 minutos para calcular tudo. Se a sua solução leva mais tempo do que isso, talvez não esteja correta

# Categoria

Criptografia

# Dificuldade

Fácil se quem for fazer já conhece os números de Sophie Germain e souber RSA.
Média se a pessoa conhecer RSA. Difícil se não conhecer RSA.

# Arquivos

Os arquivos que devem ser disponibilizados no chall são somente o `chall.py` e o `n_value.py`

# Solução

O problema do challenge consiste em perceber que `q = 2*p + 1`. A implementação deveria usar dois safe primes diferentes, mas aqui estamos usando o primo de Sophie Germain e o seu safe prime number associado. O que resulta em `q = 2*p + 1`. Dessa forma, `n` pode ser calculado como:

`n = p*q`

`n = p * (2*p + 1)`

`n = 2*p^2 + p`

Podemos calcular a raiz da equação de segundo grau `2*p^2 + p - n = 0` e achar o valor de `p`. Depois disso podemos facilmente achar o valor de `q` e, consequentemente `phi`.

O que pode elevar a dificuldade é o número bem grande de `p` e `q`. Escolhi números extremamente grandes para impedir fatorações.

o código de solução está no arquivo solve.py

# Flag

`HIK_946339622776025`
