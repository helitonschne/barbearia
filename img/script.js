const botao = document.getElementById('btnTema');

function alternarModoEscuro() {

    document.body.classList.toggle('modo-escuro');
    
}

botao.addEventListener('click', alternarModoEscuro);

if (document.body.classList.contains('modo-escuro')) {

    botao.textContent = "Modo Claro";

} else {

    botao.textContent = "Modo Escuro";

}
