#!/usr/bin/python3

def tag_bloco(texto, classe="success"):
    return f'<div class="{classe}">{texto}</div>'

if __name__ == '__main__':
    #testes assertions
    assert tag_bloco('incluso com susesso!') ==\
        '<div class="success">incluso com susesso!</div>'
        # '<div class="success">incluso sem susesso!</div>'
        
    assert tag_bloco('Impossivel incluir!', 'error') ==\
        '<div class="error">Impossivel incluir!</div>'

    print(tag_bloco('bloco'))
        