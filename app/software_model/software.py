
def model_pattern():
    #FIXME: convertir en json  fichier txt
    #  fichier stoke sur le repo git en mode texte
    model_pattern_tuple = (
            {"designer":["firefox","vscode"]},#TODO: add MAMP,
            {"coder":["firefox","vscode","git"]},#TODO: github Desktop, git, MAMP
            {"test":["test"]},
            {"test firefox":["firefox"]},
            {"test Vscode":["vscode"]},
            {"test git":["git"]}
            )
    return model_pattern_tuple


if __name__ == "__main__":
    pass