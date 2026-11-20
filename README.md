# Watchlist Random Picker

This project assists your movie choice by picking randomly movie(s) you've marked on your watchlist to watch later on the movie social media Letterboxd, made with Python!

## Theoretical basis

The project came to mind exclusively to solve a personal problem with using `watchlistpicker.com`, a direct option towards randomizing choices of a watchlist. For a while now, it has been showing an error when I tried to use my personal (not private) profile, saying `Sorry, that watchlist is empty, private, or doesn't exist at all.`. Then, I decided to give it a try using Python and some things I studied recently.

The first version of this project was made using simple arrays and iterating them using for loops. This first version of the project can still be found in the file `watchlist_array.py`. A note for those that want to run it: As it says in commentaries on the file's code, it shows only the name of the movie(s) you choose to randomize, not the year nor the Letterboxd link.

After concluding the first version of the project, I wanted to try something more. Recently, I have been studying dictionaries and their usage on Python and I had the idea of pairing it with this project. It just made more sense, since I have all the information at the .csv, but I would have to pair each link and year with the name of the said movie. In dictionaries, it is done because every key has its pair on a value. Let's take Harakiri as an example.
> On the said dictionary,
> 
> dictionary_example { 
> 
>   [movie_name] = ([year], [link])
> 
>   Harakiri = (1962, https://letterboxd.com/film/harakiri/)
> 
> }

That way, information could be accessed easily, such as so:
> dictionary_example[Harakiri][0] = 1962
> dictionary_example[Harakiri][1] = https://letterboxd.com/film/harakiri/

That way, the title of the movie is synced and paired with the title of that same movie title.
I had that idea simply because, when shown the results, you would see the difference:

`From the old code`
> Your movie is Harakiri

`From the new code`

> Your movie is Harakiri (1962) - https://letterboxd.com/film/harakiri/

## Example of usage

In order to show the usage of this project, you'll notice there's a watchlist.csv. This file is an example of the watchlist.csv you can extract directly from Letterboxd. This example shows the first 100 movies of the official Letterboxd list `Letterboxd’s Top 500 Films`.
First, I ran the Python file and chose one single movie as a recommendation. And so, I was recommended of `Harakiri (1962) - https://letterboxd.com/film/harakiri/`
<img width="633" height="57" alt="Captura de tela 2026-11-19 231428" src="https://github.com/user-attachments/assets/a3cc0d9b-3863-4785-97df-b1f77ac8e28b" />

Decided to ask for another movie to showcase the randomization and, this time, got the recommendation of `The Red Shoes (1948) - https://letterboxd.com/film/the-red-shoes/`
<img width="736" height="58" alt="Captura de tela 2026-11-19 231525" src="https://github.com/user-attachments/assets/ddf5a26e-3aa7-4a2e-9943-5cdf1311f55d" />

Now, to test the multiple recommendations, I asked for five movies out of Letterboxd's list and got the movies below.
<img width="758" height="197" alt="Captura de tela 2026-11-19 235146" src="https://github.com/user-attachments/assets/ab274313-eed0-47f6-938b-40294d4a1f38" />

When the code asks you `Would you like to sort it out again?`, it's good to remind it is also case-insensitive! Meaning it could answer to `yes`, `yES`, `YES`, `YEs` or `NO`.
<img width="408" height="270" alt="Captura de tela 2026-11-19 231724" src="https://github.com/user-attachments/assets/84554f84-4ee0-4936-8f3e-4a2fa1bff682" />

Finally, when your recommendation has been complete, the program shuts down and thanks you for utilizing it!
<img width="405" height="38" alt="Captura de tela 2026-11-19 231756" src="https://github.com/user-attachments/assets/afbac8d9-30b2-43f4-aa6f-b840d336a8f6" />

## Project structure

    |
    | - README.md -> `README file explaining theory, examples of usage, requirements and how to use it!`
    |
    | - watchlist_array.py -> `First version of the project made using arrays.`
    |
    | - watchlist_picker.py -> `Final version of the project made using dictionaries for better storage.`
    |
    | - watchlist.csv -> `.csv file used for demonstration!`

## Portuguese brief explanation

Para este projeto pessoal, resolvi por em prática o meu inglês — uma ideia que talvez eu deveria ter tentado mais cedo, honestamente! Mas, para manter as tradições, decidi manter uma seção do README em português, assim como meus outros projetos.
Este projeto tem o intuito de sortear aleatoriamente, usando Python, um filme da sua watchlist pessoal do Letterboxd!
Inicialmente, o projeto foi feito simplesmente utilizando arrays. Entretanto, como estou estudando a utilização de dicionários, e a sincronização de pares de dados com chaves pareceu conveniente e útil para mim quando quis implementar ano e link para cada filme recomendado, reformulei o código para a versão atual! Ambos os códigos estão disponíveis, sendo a versão com arrays nomeada `watchlist_array.py` e a versão principal `watchlist_picker.py`!
A ideia do projeto se originou depois de enfrentar alguns problemas com o `watchlistpicker.com`, um website que eu usava exatamente para este intuito. Decidi tentar resolver esse problema usando Python e acabou funcionando perfeitamente!

Para utilizá-lo, você precisa exportar a sua watchlist do Letterboxd para um arquivo `.csv`. Para fazer isso,
- Acesse o seu perfil do Letterboxd;
- Acesse a sua lista de watchlist (ou coloque seu username em https://letterboxd.com/%your_username%/watchlist);
- Clique em `Export watchlist`;
- Troque o nome do arquivo exportado para `watchlist.csv`;
- Coloque na pasta do projeto, substituindo o arquivo que coloquei padrão para demonstração.

Além disso, é necessário garantir que o Python e a sua biblioteca `pandas` também estão instalados. Para isto, uma breve pesquisa no Google te redireciona para [este link](https://www.python.org/downloads/) (ou digitando este https://www.python.org/downloads/) e basta clicar em `Download the Python install manager`. Garanta que, durante a instalação, a caixa que diz `Add Python to PATH` esteja marcada.
Após isto, abra o terminal e digite `pip install pandas` para garantir que a biblioteca `pandas` do Python também esteja baixada! Assim que a instalação estiver concluída, estará tudo perfeito para execução!

Para executar o projeto:
- Baixe ou clone o repositório digitando `git clone https://github.com/niconsoli/watchlistRandomPicker`
- Acesse e descompacte a pasta do repositório
- Substitua o arquivo `watchlist.csv` para o seu próprio `watchlist.csv`, exportado pelo Letterboxd oficial
- Acesse o terminal dentro da pasta
- Digite `python.exe watchlist_picker.py`
- Divirta-se com seu filme recomendado!

## Requirements and how to install

To run this program you'll need to have:
- Python 3.11 or newer
- Python library `pandas`
- `.csv` of your personal watchlist

To install the latest version of Python, check [this link](https://www.python.org/downloads/) (or use https://www.python.org/downloads/) to go directly to Python's official website and download the Python install manager. Make sure that, during the download process, you check the box `Add Python to PATH` to make some things easier.
To install the Python library `pandas`, open your Terminal and type `pip install pandas` and wait for the process to be done.
To extract your watchlist `.csv`, go to your Letterboxd profile (or to this link, inserting your Letterboxd username: https://letterboxd.com/%your_username%/watchlist/) and click the button `Export watchlist`. After getting the `.csv`, make sure to change its name to `watchlist.csv`, before placing it on the project's folder and replacing the default `.csv` I placed for demonstration purposes.
After that, you should be good to go!

## How to run

- Either download the repository files or clone it using Git by typing `git clone https://github.com/niconsoli/watchlistRandomPicker`.
- Unzip or access the repository folder.
- Replace the `watchlist.csv` to your `.csv` extract from the official Letterboxd website, from your profile. (maintain the file's name identical!)
- Enter the repository folder using the Terminal
- Type `python.exe watchlist_picker.py`
- Have fun watching your recommended movie!
